#include <arpa/inet.h>
#include <dirent.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <unistd.h>

#include <cerrno>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

namespace fs = std::filesystem;

static bool sendAll(int sock, const void *data, size_t len) {
    const char *p = static_cast<const char *>(data);
    while (len > 0) {
        ssize_t n = send(sock, p, len, 0);
        if (n <= 0) return false;
        p += n;
        len -= static_cast<size_t>(n);
    }
    return true;
}

static bool recvAll(int sock, void *data, size_t len) {
    char *p = static_cast<char *>(data);
    while (len > 0) {
        ssize_t n = recv(sock, p, len, 0);
        if (n <= 0) return false;
        p += n;
        len -= static_cast<size_t>(n);
    }
    return true;
}

static bool sendMessage(int sock, const std::string &msg) {
    uint32_t len = htonl(static_cast<uint32_t>(msg.size()));
    return sendAll(sock, &len, sizeof(len)) && sendAll(sock, msg.data(), msg.size());
}

static bool recvMessage(int sock, std::string &msg) {
    uint32_t netLen = 0;
    if (!recvAll(sock, &netLen, sizeof(netLen))) return false;
    uint32_t len = ntohl(netLen);
    msg.assign(len, '\0');
    return len == 0 || recvAll(sock, msg.data(), len);
}

static std::string baseName(const std::string &path) {
    return fs::path(path).filename().string();
}

static bool isInsideRoot(const fs::path &root, const fs::path &candidate) {
    fs::path rel = fs::relative(candidate, root);
    return rel.empty() || rel.native().rfind("..", 0) != 0;
}

static fs::path resolvePath(const fs::path &root, const fs::path &cwd, const std::string &arg) {
    fs::path p = fs::path(arg).is_absolute() ? root / fs::path(arg).relative_path() : cwd / arg;
    return fs::weakly_canonical(p);
}

static std::string displayPath(const fs::path &root, const fs::path &cwd) {
    fs::path rel = fs::relative(cwd, root);
    if (rel.empty() || rel == ".") return "/";
    return "/" + rel.generic_string();
}

static std::string listDirectory(const fs::path &cwd) {
    std::ostringstream out;
    for (const auto &entry : fs::directory_iterator(cwd)) {
        out << (entry.is_directory() ? "[D] " : "[F] ")
            << entry.path().filename().string() << '\n';
    }
    std::string s = out.str();
    return s.empty() ? "(empty)\n" : s;
}

static bool sendFileBytes(int sock, const fs::path &path) {
    std::ifstream in(path, std::ios::binary);
    char buf[8192];
    while (in) {
        in.read(buf, sizeof(buf));
        std::streamsize n = in.gcount();
        if (n > 0 && !sendAll(sock, buf, static_cast<size_t>(n))) return false;
    }
    return true;
}

static bool recvFileBytes(int sock, const fs::path &path, uint64_t size) {
    std::ofstream out(path, std::ios::binary);
    if (!out) return false;

    char buf[8192];
    while (size > 0) {
        size_t chunk = static_cast<size_t>(std::min<uint64_t>(sizeof(buf), size));
        if (!recvAll(sock, buf, chunk)) return false;
        out.write(buf, static_cast<std::streamsize>(chunk));
        size -= chunk;
    }
    return static_cast<bool>(out);
}

static bool handleClient(int client, const fs::path &root) {
    fs::path cwd = root;
    sendMessage(client, "OK: connected. Type help for commands.");

    std::string cmdline;
    while (recvMessage(client, cmdline)) {
        std::istringstream iss(cmdline);
        std::string cmd;
        iss >> cmd;

        if (cmd == "quit") {
            sendMessage(client, "Bye.");
            break;
        } else if (cmd == "help") {
            sendMessage(client, "Commands: ls, pwd, cd <dir>, get <file>, put <file>, mkdir <dir>, rm <file>, rmdir <dir>, quit");
        } else if (cmd == "pwd") {
            sendMessage(client, displayPath(root, cwd));
        } else if (cmd == "ls") {
            sendMessage(client, listDirectory(cwd));
        } else if (cmd == "cd") {
            std::string arg;
            iss >> arg;
            if (arg.empty()) {
                sendMessage(client, "ERR: usage: cd <dir>");
                continue;
            }
            fs::path next = resolvePath(root, cwd, arg);
            if (!isInsideRoot(root, next) || !fs::is_directory(next)) {
                sendMessage(client, "ERR: directory does not exist or is outside server root");
                continue;
            }
            cwd = next;
            sendMessage(client, "OK: current directory changed to " + displayPath(root, cwd));
        } else if (cmd == "mkdir" || cmd == "rmdir" || cmd == "rm") {
            std::string arg;
            iss >> arg;
            if (arg.empty()) {
                sendMessage(client, "ERR: missing path argument");
                continue;
            }
            fs::path target = resolvePath(root, cwd, arg);
            if (!isInsideRoot(root, target)) {
                sendMessage(client, "ERR: path is outside server root");
                continue;
            }
            std::error_code ec;
            if (cmd == "mkdir") {
                bool ok = fs::create_directory(target, ec);
                sendMessage(client, ok && !ec ? "OK: directory created" : "ERR: cannot create directory");
            } else if (cmd == "rmdir") {
                bool ok = fs::remove(target, ec);
                sendMessage(client, ok && !ec ? "OK: directory removed" : "ERR: cannot remove directory");
            } else {
                if (!fs::is_regular_file(target)) {
                    sendMessage(client, "ERR: target is not a regular file");
                } else {
                    bool ok = fs::remove(target, ec);
                    sendMessage(client, ok && !ec ? "OK: file removed" : "ERR: cannot remove file");
                }
            }
        } else if (cmd == "get") {
            std::string arg;
            iss >> arg;
            fs::path target = resolvePath(root, cwd, arg);
            if (arg.empty() || !isInsideRoot(root, target) || !fs::is_regular_file(target)) {
                sendMessage(client, "ERR: file does not exist");
                continue;
            }
            uint64_t size = fs::file_size(target);
            sendMessage(client, "OK " + std::to_string(size) + " " + baseName(arg));
            if (!sendFileBytes(client, target)) return false;
        } else if (cmd == "put") {
            std::string name;
            uint64_t size = 0;
            iss >> name >> size;
            if (name.empty()) {
                sendMessage(client, "ERR: usage: put <file>");
                continue;
            }
            fs::path target = resolvePath(root, cwd, baseName(name));
            if (!isInsideRoot(root, target)) {
                sendMessage(client, "ERR: path is outside server root");
                continue;
            }
            sendMessage(client, "OK: ready");
            bool ok = recvFileBytes(client, target, size);
            sendMessage(client, ok ? "OK: uploaded " + baseName(name) : "ERR: upload failed");
        } else {
            sendMessage(client, "ERR: unknown command");
        }
    }
    return true;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <port> <server_root>\n";
        return 1;
    }

    int port = std::stoi(argv[1]);
    fs::path root = fs::weakly_canonical(argv[2]);
    if (!fs::exists(root)) fs::create_directories(root);
    root = fs::canonical(root);

    int server = socket(AF_INET, SOCK_STREAM, 0);
    if (server < 0) {
        std::perror("socket");
        return 1;
    }

    int yes = 1;
    setsockopt(server, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(static_cast<uint16_t>(port));

    if (bind(server, reinterpret_cast<sockaddr *>(&addr), sizeof(addr)) < 0) {
        std::perror("bind");
        close(server);
        return 1;
    }
    if (listen(server, 5) < 0) {
        std::perror("listen");
        close(server);
        return 1;
    }

    std::cout << "Server listening on port " << port << ", root: " << root << '\n';
    while (true) {
        sockaddr_in clientAddr{};
        socklen_t len = sizeof(clientAddr);
        int client = accept(server, reinterpret_cast<sockaddr *>(&clientAddr), &len);
        if (client < 0) {
            std::perror("accept");
            continue;
        }
        std::cout << "Client connected\n";
        handleClient(client, root);
        close(client);
        std::cout << "Client disconnected\n";
    }
}
