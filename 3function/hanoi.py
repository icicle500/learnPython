i = 0
def move(n,a,b,c):
    global i
    if n==1:
        print(a,'-->',c)
        i+=1
        return
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(10,'A','B','C')
print(i)