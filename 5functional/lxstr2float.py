# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(a):
    pos =   a.find('.')
    s1  =   a[:pos]
    s2  =   a[pos+1:]
    m1  =   map(lambda ch:ord(ch) - ord('0'), list(s1))
    m2  =   map(lambda ch:ord(ch) - ord('0'), list(s2))
    n1  =   reduce(lambda x, y : x * 10 + y, m1)
    n2  =   reduce(lambda x, y : x * 10 + y, m2) / (10 ** (len(a) - pos - 1))
    return n1 + n2

print(str2float('123.456'))