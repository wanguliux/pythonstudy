tag=1
if tag:
    print('条件满足')
elif not tag:
    print('no')
else:
    print('no')
#逻辑运算符

print(1 and 0)
print(1 or 0)
print(not 0)
# not优先级最高和其后的条件不可分割
# 如果既有and又有or，用括号把and左右两边的条件括起来进行运算

t2=10
if 1<t2<=10:
    print(1)
else:
    print(0)