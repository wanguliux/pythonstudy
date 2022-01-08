# 本质是自定义的迭代器
# 一般与for循环连用
# 只能在函数内使用，保存了函数的暂停状态

# def fun ():
#     print('===')
#     yield 1
#     print('===')
#     yield 2
#     print('===')
#     yield 3
#
# g=fun()
# print(g)
#
# # res=next(g)
# # # 会触发函数的执行，知道碰到一个yield停下来，并且将yield后的值，当做本次next的结果返回
# # print(res)
# # print(next(g))
# #或者
# for i in g:
#     print(i)

#定义斐波那契数列的生成器
def run (n):#n代表数列个数
    i,a,b=0,1,1
    while i<n:
        yield a
        a,b=b,a+b
        i+=1

# my_run=run(10)
# print(my_run)
# for i in my_run:
#     print(i)
#计算阶乘之合
def jc (n):
    i,s,sn,k=0,0,1,1
    while i<n:
        sn*=k
        s+=sn
        k+=1
        i+=1
        yield s
#     return s
# print(jc(5))
myjc=jc(5)
for i in myjc:
    print(i)
