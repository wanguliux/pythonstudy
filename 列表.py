# print('hello %s %d'%('world',123))
L=[1,'二',True,2.1,3.1,[3,4]]
print(L)
print(L[0])
print(L[-1])# 反向取
print(L[-1][1])
#计算列表元素个数总数
print(len(L))
#成员运算in， not in
print('二'in L)
print(1 not in L)
#查看某个元素的个数count
print(L.count(1))
#查询元素，起始位置，结束位置，index
print(L.index('二'))#不存在会报错
#增加
#append(元素)忘列表末尾追加一个元素
L.append(9)
print(L)
#insert(元素，位置)往指定位置插入一个元素
L.insert(0,'hell0')
print(L)
#extend()往末尾添加多个元素，括号里放列表，末尾追加
L.extend([8,8])
print(L)
# 删除del[索引]
L.remove(8)#从后往前删第一个
print(L)
res=L.pop(2)
print(res,L)
# 改
L[0]=9
print(L)
# 清空列表
#L.clear()
# 反序
L.reverse()
print(L)
# 排序(纯数字列表）
lm=[1,3,2,4,7,6]
lm.sort(reverse=True)
print(lm)
lm.sort(reverse=False)
print(lm)