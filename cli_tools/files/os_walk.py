import os
import fnmatch


def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)
                for d in exclude_dirs:
                    if d in dirnames:
                        dirnames.remove(d)


# 查找目录下所有文件
for item in find_specific_files('.'):
    print(item)

# 查找目录下所有图片或者txt
patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.txt']
for item in find_specific_files('.', patterns):
    print('>>>>', item)

print('*' * 100)
# 获取当前文件或者文件所在目录的绝对路径
print(os.path.abspath(__file__))
print(os.path.abspath('.'))
print(os.path.dirname(os.path.abspath(__file__)))

print('*' * 100)

# 查找目录下最大的十个文件，find_specific_files已经能找到某个目录下的所有文件，只要获取文件大小并按大小排序，输出最大的十个文件即可
files = {name: os.path.getsize(name) for name in find_specific_files('.')}
result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
for i,t in enumerate(result, 1):
    print(i, t[0], t[1])
