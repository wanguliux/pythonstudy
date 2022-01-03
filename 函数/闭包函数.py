# 闭包函数
# 闭：指该函数是一个内部函数
# 包：该内部的函数名字在外部被引用
# def outer():
#     print('外部函数在运行')
#     def inner():
#         print('内部函数在运行')
#     return inner
# # outer()
# inner=outer()
# inner()
#闭包传值方式
def outer(x,y):

    def inner():
        print(x+y)
    return inner
# inner=outer(1,2)
# inner()
# outer(1,2)()
