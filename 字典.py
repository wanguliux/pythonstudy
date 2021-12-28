info={'name':'大海','name2':2,}
print(info['name'])
#前面是key，不可变类型，不能取，元组也可以，但通常应该为字符串。
#字典的定义方式2
dic=dict(x=1,y=2)


info['name3']=True#字典的增加
info['name4']=6
print(info)
#字典的len是查询键值对的个数
#字典成员运算in和not in是判断key值
#clear 清空字典
dic.clear()
print(dic)
del info['name']
print(info)
#pop,拿走的是value
res=info.pop('name2')#pop取得是key对应的value值
print(res,info)
res2=info.popitem()#popitem取得是最后一个个键值对,返回一个元组
#字典修改
print(res2,info)
info['name3']=9
print(info)
info.update({'name3': 7})
print(info)
#有则不动返回原值，无则添加返回新值
res3=info.setdefault('name3',0)
print(res3)
res4=info.setdefault('name5',0)
print(res4)
#查
print(info['name3'])
#不会报错的get
print(info.get('xxx'))
#取出所有key
res5=info.keys()
print(res5)
print(list(res5))
#取出所有value
res5=info.values()
print(res5)
print(list(res5))
#取出所有键值对
res5=info.items()
print(res5)
print(list(res5))#直接list会只把key装到列表