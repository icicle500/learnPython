#用generator写一个杨辉三角

def triangles():
      L = [1]
      while True:
          yield L
          L = [1]+[L[i-1]+L[i] for i in range(len(L)) if i>0]+[1]

x = 0
for a in triangles():
    print(a)
    x+=1
    if x==3:
        break