#异常包括三部分
# 1，异常的追踪信息
# 2，异常的类型
# 3，异常的信息
# 错误分为两大类
# 语法上的错误
# 逻辑上的错误

# 异常处理
'''
try:
    代码1
    代码2
    。。。
except NameError:
    #当抛出的异常是NameError时执行的子代码模块
except ...:
    pass
else ....:#无异常走else
    pass
finally:#无论有没有异常，都会走finally
    pass

'''
try:
    a
except (NameError,TypeError) as e:
    print('兄弟你检查一下代码')
    print(e)
else:
    print('代码正确')
finally:
    #无论有没有异常都会执行
    print('完成异常捕获')

#万能捕获
try:
    a
except Exception as e:
    print('兄弟你检查一下代码')
    print(e)
else:
    print('代码正确')
finally:
    #无论有没有异常都会执行
    print('完成异常捕获')

# 断言——自定义异常
l=[1,2,3,4,5]
if len(l)!=5:
    raise TypeError('列表长度必须为5')
assert len(l)!=5#必须不等于5，否则AssertionError