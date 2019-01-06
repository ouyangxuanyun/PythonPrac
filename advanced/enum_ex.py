from enum import Enum
from enum import IntEnum,unique

# 枚举好处：定义后不可更改，枚举变量不能重复
# 枚举不支持大小比较，只能做身份比较 == ，is
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4

@unique
class VIP1(IntEnum):
    YELLOW = 1
    YELLOW_ALIAS = 1 # unique 限定不能重复， IntEnum 限定值必须是数字
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.BLACK)

for v in VIP:
    print(v)

for v in VIP.__members__.items():
    print(v)

for v in VIP.__members__:
    print(v)

a = 1

print(VIP(a))
print(1 == VIP.YELLOW) # 这样无法比较
print(VIP(a) == VIP.YELLOW) # 正确的比较方式