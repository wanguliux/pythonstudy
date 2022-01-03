#函数定义
#只检测函数体语法，不执行函数体代码

def factory():
    print('这是个函数')

factory()
#函数三大特性：功能，参数，返回值

def factory2():
    pass#用来占位，防止报错

def factory3(a,b=2):#在定义阶段就已赋值，意味着使用时可不为其赋值，也可以对其重新赋值。
   c=a+b
   print(c)
factory3(9)

#可变长度的参数(不定长参数）
#在形参中带*：会将调用函数时溢出位置实参保存成元组的形式，然后赋值*号以后的变量名
def foo(a,b,*c):
    print(a,b,c)

foo(1,2,3,33,333)

def fn(x,y,z):
    print(x,y,z)

#实参打
fn(1,*(2,3))#只能打散序列类型
fn(*('abc'))

#在形参中带**，会将调用函数时溢出关键字实参保存成字典的形式，然后赋值**后的变量名
# def fn2(*args,**kwargs):#接受的是0到多个位置参数
#     print(args)
#     print(kwargs)
#转嫁函数格式
def bar(x,y,z):
    print(x,y,z)

def fn2(*args,**kwargs):
    bar(*args,**kwargs)

fn2(1,2,3)

#命名关键字参数
def fn3(x,y,*args,m,n,**kwargs):
    print(x,y)
    print(args)
    print(m,n)
    print(kwargs)
fn3(1,2,3,4,5,6,m=3,n=4,a=1,b=2,c=3)