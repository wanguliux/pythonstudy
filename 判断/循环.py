#continue之后的代码不走，直接走下一次循环

#while + else
# n=1
# while n<9:
#     n=n+1#n+=1
#     print(n)

#for循环打印列表
# name2=['q','w','e','r']
# for i in name2:
#     print(i)

# for循环打印字典，默认遍历key值
# name={'n1':1,'n2':2,'n3':3}
# for q in name:
#     print(q)
#     print(name[q])
# for w in name.values():
#     print(w)


#range(起始索引，结束索引，步长）,是一个迭代器#range(结束索引，步长）不写起始索引相当于从0开始
print(range(0,10000))#因为不会直接变成列表，所以不会浪费内存
#一般和for连用，循环一次取一次
for k in range(0,10):
    print(k)

#print默认有一个参数end，默认为‘\n’
print(1,end='')
print(1,end='')