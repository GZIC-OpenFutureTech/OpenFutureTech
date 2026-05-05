from pathlib import PurePosixPath


def on_files(files, config):
    for file in files:
        src_uri = file.src_uri

        # docs/index.md 在 MkDocs 内部通常表现为 index.md
        # 目标：/edit/main/README.md
        if src_uri == "index.md":
            file.edit_uri = "README.md"
            continue

        path = PurePosixPath(src_uri)

        # 生成页：
        #   01-基础必修课/C++编程基础.md
        #
        # 原始源文件：
        #   01-基础必修课/C++编程基础/README.md
        if path.suffix == ".md" and len(path.parts) >= 2:
            course_group = path.parts[0]
            course_name = path.stem
            file.edit_uri = f"{course_group}/{course_name}/README.md"

    return files
