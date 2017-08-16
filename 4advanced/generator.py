g = (x*x for x in range(10))
#把[]变成()就成了生成器
#可以使用next(g)来一点点推算g的值，但是还是使用for迭代比较好

for a in g:
    print(a)