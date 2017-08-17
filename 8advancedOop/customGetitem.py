class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L

# 实现__getitem__后可以使用下标取出元素
# __getitem__实现了简单的切片操作
