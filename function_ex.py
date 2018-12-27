# import hello

# hello.hellotest()
#
# def printme(str):
#     print(str)
#     return
#
# printme('aaa')
# printme('bbbbb')
#
# sum = lambda arg1, arg2: arg1 + arg2


Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)