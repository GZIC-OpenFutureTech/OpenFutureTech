#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

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

static void printHelp() {
    std::cout << "Commands: ls, pwd, cd <dir>, get <file>, put <file>, mkdir <dir>, rm <file>, rmdir <dir>, quit\n";
}

int main(int argc, char **argv) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <server_ip> <port>\n";
        return 1;
    }

    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        std::perror("socket");
        return 1;
    }

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(static_cast<uint16_t>(std::stoi(argv[2])));
    if (inet_pton(AF_INET, argv[1], &addr.sin_addr) <= 0) {
        std::cerr << "Invalid server IP\n";
        close(sock);
        return 1;
    }

    if (connect(sock, reinterpret_cast<sockaddr *>(&addr), sizeof(addr)) < 0) {
        std::perror("connect");
        close(sock);
        return 1;
    }

    std::string response;
    if (recvMessage(sock, response)) std::cout << response << '\n';

    std::string line;
    while (std::cout << "ftp> " && std::getline(std::cin, line)) {
        std::istringstream iss(line);
        std::string cmd;
        iss >> cmd;
        if (cmd.empty()) continue;

        if (cmd == "help") {
            printHelp();
            continue;
        }

        if (cmd == "put") {
            std::string path;
            iss >> path;
            if (path.empty() || !fs::is_regular_file(path)) {
                std::cout << "ERR: local file does not exist\n";
                continue;
            }
            uint64_t size = fs::file_size(path);
            std::string request = "put " + baseName(path) + " " + std::to_string(size);
            if (!sendMessage(sock, request) || !recvMessage(sock, response)) break;
            if (response.rfind("OK", 0) != 0) {
                std::cout << response << '\n';
                continue;
            }
            if (!sendFileBytes(sock, path) || !recvMessage(sock, response)) break;
            std::cout << response << '\n';
            continue;
        }

        if (!sendMessage(sock, line) || !recvMessage(sock, response)) break;

        if (cmd == "get" && response.rfind("OK ", 0) == 0) {
            std::istringstream rs(response);
            std::string ok;
            uint64_t size = 0;
            std::string name;
            rs >> ok >> size >> name;
            if (name.empty()) name = "downloaded.file";
            bool saved = recvFileBytes(sock, baseName(name), size);
            std::cout << (saved ? "OK: downloaded " : "ERR: download failed ") << baseName(name)
                      << " (" << size << " bytes)\n";
        } else {
            std::cout << response << '\n';
        }

        if (cmd == "quit") break;
    }

    close(sock);
    return 0;
}
