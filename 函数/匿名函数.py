#没有名字的函数，用于使用一次的场景，没有重复使用的需求

# print((lambda x,y:x+y)(1,2))

n={
    'a':4,
    'b':3,
    'c':2,
    'd':1
}

# max(字典,key=函数名)默认去比较key的，通过函数名改名key
print(max(n,key=lambda v:n[v]))

