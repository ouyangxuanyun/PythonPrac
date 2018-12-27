num = 5
if num == 3:  # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('roadman')  # 条件均不成立时输出

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


def hellotest():
    for letter in 'Python':
        if letter == 'h':
            continue
        print('当前字母：', letter)
    return
