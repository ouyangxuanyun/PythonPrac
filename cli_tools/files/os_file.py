import os

res = os.getcwd()
print(res)

print(os.listdir('.'))

path = os.path.abspath(__file__)
print(path, __file__,os.path.dirname(path))
print("parent directory of current file : ", os.path.abspath(os.path.join(os.path.dirname(path))), os.path.pardir)

print('*'*100)

print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(os.path.join(os.path.expanduser('~'),item))])

print({item: os.path.realpath(item) for item in os.listdir(os.path.expanduser('~'))})