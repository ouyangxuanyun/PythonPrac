origin = 0


# 闭包方式
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(2))
print(tourist(2))

print('------------------------------')


#  原始方式
def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(3))
print(go(3))
print(go(3))
