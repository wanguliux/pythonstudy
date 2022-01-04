f = open(r"test.txt", encoding='utf-8')#一定要在程序结束前关闭打开的文件
s = f.read()
print(s)
f.close()
#上下文管理