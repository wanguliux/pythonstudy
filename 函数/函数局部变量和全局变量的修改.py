#函数外部不能访问函数内部的变量

#函数内部可以访问函数外部的变量，但是不能修改外部变量，用global可以修改全局变量
x=123
def fn():
    global x
    x=x+1
    print(x)
fn()

def f1():
    b=100
    def f2():
        nonlocal b
        b=b+1
        print(b)
    f2()
f1()
#闭包函数存在函数的嵌套
#常用内置函数
# 绝对值：abs()
# 判断是否全为真：all(可迭代对象)，可迭代对象是空则为真
# 判断是否存在真：any(可迭代对象)，可迭代对象是空则为假
# 求最大值：max()
# 求最小值：min()
# 求和:sum()
# ascii英文字符编码
# 把字符转换成编码：ord()
# 把编码转换成字符：chr()
# 拉链函数：zip
t1=['a','b','c','d']
t2=[1,2,3,4]
print(list(zip(t1,t2)))
#执行字符串里的代码exec
