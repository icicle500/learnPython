# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
import functools
def be(*args,**kw):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            func(*args,**kw)
            print('end call')
        print('begin call')
        return wraper
    return decorator

@be()
def now():
    print('test')

now()
