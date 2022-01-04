# 文件的打开模式
#     r：只读模式（默认）
#     w：只写模式
#     a：只追加写模式
# 控制读写文件单位的方式（必须与r、a、w连用）
#     t：文本模式，一定要指定encoding参数，只对文本文件有效
#     b：二进制模式，一定不能指定encoding参数
with open('test.txt',mode='rt',encoding='utf-8')as f:#上下文操作，在with 外就关闭了
    pass
    # print('是否可读',f.readable())#f.writable()判断是否可写
    # #防止
    # res1=f.read()
    # print(res1)
    # 或者
    # for line in f:
    #     print(line,end='')
    #或者
    # L=[]
    # for line in f:
    #     L.append(line)
    # print(L)
    # 或者
    # print(f.readlines())
with open('test2.txt',mode='wt',encoding='utf-8')as f2:


    print(f2.writable())
    f2.write('写入操作\n')
    #无则创建，有则清空