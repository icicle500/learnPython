def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print(b)
        yield(b) #print改成yield这就成了一个generator
        a,b = b,a+b #注意赋值语句
        n = n+1
    return 'done'

for x in fib(10):
    print(x)