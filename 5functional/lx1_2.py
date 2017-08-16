# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def pord(L):
    return reduce(lambda x,y:x*y,L)

print('3*5*7*9=',pord([3,5,7,9]))
#暂时还不清楚到底咋回事…lambda需要传入两个参数，那么哪儿来的两个参数呢…