import os
from urllib.parse import quote

# 排除的目录列表，不包括在文件遍历中
EXCLUDE_DIRS = ['.git', 'docs', '.vscode']
# 需要特别处理的 README.md 文件
README_MD = ['README.md']

# 支持的文本文件扩展名，文本文件会生成文本链接
TXT_EXTS = ['md', 'txt']
# 不纳入资源列表的文件扩展名，主要是LaTeX等工具的编译中间产物
IGNORE_EXTS = ['aux', 'log', 'out', 'toc', 'synctex', 'fls', 'fdb_latexmk', 'bbl', 'blg']
# GitHub上文本文件的访问URL前缀
TXT_URL_PREFIX = 'https://github.com/OpenFuTech/SCUT-FT-Guide/blob/main/'
# GitHub上二进制文件的访问URL前缀
BIN_URL_PREFIX = 'https://github.com/OpenFuTech/SCUT-FT-Guide/raw/main/'


def IsIgnoredFile(filename: str):
    """
    判断文件是否为系统垃圾文件或编译中间产物，这类文件不应出现在资源列表中
    """
    # 以点开头的隐藏文件，例如macOS的.DS_Store、._xxx，或Windows的desktop.ini等
    if filename.startswith('.'):
        return True
    # 无扩展名的文件不会被误判，因为rsplit会返回文件名本身
    return filename.rsplit('.', 1)[-1].lower() in IGNORE_EXTS


def GenerateFileList(courseGroup: str, course: str):
    """
    遍历指定课程组和课程目录，生成文件列表的 Markdown 格式内容
    """
    # 用于存储所有文件的Markdown格式内容
    filelistTexts = '## 资源列表\n'
    # 用于存储README.md文件的路径
    readmePath = ''
    
    # 遍历课程目录及其子目录
    for root, dirs, files in os.walk(os.path.join(courseGroup, course)):
        # 跳过隐藏目录，避免其中的内容被收录进资源列表
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # 排序文件名
        files.sort()
        # 计算当前目录层级，根目录为1
        level = root.replace(courseGroup, '').count(os.sep)
        # 根据层级决定缩进量，根目录不个缩进，根目录下的文件夹0个缩进
        indent = ' ' * 4 * (level - 2)
        # 添加当前目录名到文件列表，跳过根目录
        if (level > 1):
            filelistTexts += '{}- {}\n'.format(indent, os.path.basename(root))
        # 文件的缩进量（比目录多一级）
        subindent = ' ' * 4 * (level - 1)
        for f in files:
            # 排除系统垃圾文件和编译中间产物
            if IsIgnoredFile(f):
                continue
            # 排除README.md文件
            if f not in README_MD:
                # 如果是md、txt等文本文件，生成GitHub页面链接
                if f.split('.')[-1] in TXT_EXTS:
                    filelistTexts += '{}- [{}]({})\n'.format(subindent, f, TXT_URL_PREFIX + quote('{}/{}'.format(root, f)))
                # 如果是其他文件（如二进制文件），生成raw内容链接
                else:
                    filelistTexts += '{}- [{}]({})\n'.format(subindent, f, BIN_URL_PREFIX + quote('{}/{}'.format(root, f)))
            # 如果是README.md文件，且该文件是课程根目录中的README.md
            elif root == os.path.join(courseGroup, course) and readmePath == '':
                # 保存README.md文件路径
                readmePath = '{}/{}'.format(root, f)
    return filelistTexts, readmePath


def GenerateMarkdown(courseGroup: str, course: str, filelistTexts: str, readmePath: str):
    """
    生成并保存课程的Markdown文件，包含课程标题、README.md、文件资源列表
    """
    # 组合最终的文本内容，先添加文件列表，然后如果有README.md，添加它
    finalTexts = ['\n\n', filelistTexts]
    
    if readmePath:
        # 如果存在README.md，读取其内容
        with open(readmePath, 'r') as file:
            # 将README.md的内容添加到文件列表前
            finalTexts = file.readlines() + finalTexts

    # 将课程文件夹标题添加在开头
    titleText = ['# {}\n\n'.format(course)]
    finalTexts = titleText + finalTexts

    # 将最终的内容写入到docs/{courseGroup}/{course}.md文件
    os.makedirs(f'docs/{courseGroup}', exist_ok=True)
    with open(f'docs/{courseGroup}/{course}.md', 'w') as file:
        file.writelines(finalTexts)


if __name__ == '__main__':
    """
    1. 若docs目录不存在则创建
    2. 遍历根目录中的所有课程组目录
    3. 生成每个课程的Markdown文件
    4. 将主README.md复制到docs/index.md
    """
    # 如果docs目录不存在，创建它
    if not os.path.isdir('docs'):
        os.mkdir('docs')

    # 遍历当前目录，筛选出所有有效的课程组目录（不包括排除目录EXCLUDE_DIRS）
    courseGroups = list(filter(lambda x: os.path.isdir(x) and (
        x not in EXCLUDE_DIRS), os.listdir('.')))

    # 对每个课程组目录，生成文件列表并保存为Markdown文件
    for courseGroup in courseGroups:
        # 遍历课程组目录，筛选出所有有效的课程目录
        courses = list(filter(lambda x: os.path.isdir(os.path.join(courseGroup, x)), os.listdir(courseGroup)))
        for course in courses:
            # 获取文件列表和README.md路径
            filelistTexts, readmePath = GenerateFileList(courseGroup, course)
            # 生成并保存课程的Markdown文件
            GenerateMarkdown(courseGroup, course, filelistTexts, readmePath)

    # 读取根目录下的README.md文件
    with open('README.md', 'r') as file:
        mainreadmeLines = file.readlines()

    # 将根目录README.md的内容复制到docs/index.md
    with open('docs/index.md', 'w') as file:
        file.writelines(mainreadmeLines)