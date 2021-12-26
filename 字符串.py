msg ='hello world'
print(msg[0])
# msg[1]='a' 字符串不能通过索引进行修改
print(msg[0:4])# 顾头不顾腚
print(msg[0:6:2])
print(msg[6:0:-1])
print(len(msg))# 字符串长度计算
print('hello'in msg)#字符串逻辑判断
print('hello'not in msg)
#字符串方法
# 增加，拼接
print('a'+'b')
#format
print('my name is {}'.format(msg))
print('my name is {1},my age is {0}'.format(18,'sb'))
print('my name is {name},my age is {age}'.format(name='sb',age='18'))
# join
s1='我'
s2='爱'
s3='你'
print(''.join([s1,s2,s3]))
print('!'.join([s1,s2,s3]))
# 改大小写
msg2='aBc'
msg3=msg2.upper()
msg4=msg2.lower()
print(msg3,msg4)
# 单词首字母变大写capitalize
letter='hello world'
print(letter.capitalize())# 首个单词
print(letter.title())# 每个单词
# 切分单词，默认按空格切split
msg5='hello my world'
print(msg5.split())
msg6='H0M0W'
print(msg6.split('0'))

mm='密码:123456'
key=mm.split(':')
print(key[1])

# 去掉字符串两边的字符，不写默认空格，不管中间字符
user='      sb     '
print('sb'==user.strip())
# 多余添加自己需要的字符
print('sb'.center(10,'*'))
print('sb'.rjust(10,'*'))
print('sb'.ljust(10,'*'))
# 查子字符串的位置（起始索引）
t='hello world'
print(t.find('ll'))
print(t.find('ll',3,6))# 找不到返回-1
#判断一个字符串里的数据是不是都是数字isdigit
num='1818'
print(num.isdigit())
#判断是不是都是字母isalpha
print(num.isalpha())
# 比较开头元素是否相同startswith,比较结尾enswith
hello='hello world'
print(hello.startswith('he'))
print(hello.startswith('e'))
print(hello.endswith('d'))
print(hello.endswith('l'))
#判断是否全是小写/大写，islower/isupper

#字符串的转义
#加'\'的字符不再表示它原本的含义
print('hello\nworld')#换行
print('hello\tworld')#tab 4个空格
#字符串的反转义，\n就是\n
print(r'hello\nworld')


