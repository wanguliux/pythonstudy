#集合内元素是无序的
s1={1,2,3}
s2={2,3,4}
print(s1&s2)# 取交集
print(s1|s2)# 取并集
print(s1-s2)# 取差集
#集合每个值必须为不可变类型
s1.add(5)#加
#删
print(s1)
s1.pop()
print(s1)
s1.remove(5)
print(s1)
#改
s2.update([6,9])
print(s2)
#集合去重，无法保证原数据的顺序
#强制数据转换的时候必须为不可变类型