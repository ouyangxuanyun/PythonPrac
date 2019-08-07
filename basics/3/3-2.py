# Time : 2019/8/4 16:29
# Author : Fu
# Software: PyCharm
import os
import stat

fn = 'aaa.py'

fn.endswith(('.py', '.sh'))

d = os.listdir('./')


def my_chmod():
    if fn.endswith(('.py', '.sh')):
        fs = os.stat(fn)
        os.chmod(fn, fs.st_mode | stat.S_IXUSR) # 所属用户增加执行权限
