# 为了保证无论是否出错都能正确地关闭文件，可以使用try
'''
try:
    f=open('test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
''' # 这么写过于繁琐，可以用with语句

with open('test.txt', 'r') as f:
    for line in f.readlines():  # 按行返回list
        print(line.strip())  # 去掉末尾的'\n'
