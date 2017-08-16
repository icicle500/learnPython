import random

correct = 0
incorrect = 0 #这俩变量用来存储答对和答错的次数

def rd(): #获取随机数
    x = random.randint(1,31)
    y = random.randint(1,31)
    return x,y
def judgment(resulf,uinput): #判断结果
    if(resulf == uinput):
        global correct #全局变量
        correct+=1
        print('对')
    else:
        global incorrect #全局变量
        incorrect+=1
        print('错')

def jia():
    (x,y) = rd(); #调用rd()给x,y赋值随机数
    resulf = x+y
    uinput = int(input('%d+%d = ' % (x,y)))
    judgment(resulf,uinput) #调用judgment()判断对错
def jian():
    (x,y) = rd();
    resulf = x-y
    uinput = int(input('%d-%d = ' % (x,y)))
    judgment(resulf,uinput)
def cheng():
    (x,y) = rd();
    resulf = x*y
    uinput = int(input('%d*%d = ' % (x,y)))
    judgment(resulf,uinput)
def chu():
    (x,y) = rd();
    resulf = round(x/y,2) #取两位小数
    uinput = float(input('(保留2位小数)%d/%d = ' % (x,y)))
    judgment(resulf,uinput)
def quyu():
    (x,y) = rd();
    resulf = x%y
    uinput = int(input('%d%%%d = ' % (x,y)))
    judgment(resulf,uinput)
def ex():
    if correct+incorrect==0:
        print('\n未答题')
    else:
        print('\n总共答题%d道\n正确率为：%.2f%%'
        % (correct+incorrect,float(correct/(correct+incorrect)*100)))
    exit()

dict = {1:jia,2:jian,3:cheng,4:chu,5:quyu,6:ex}
def start(a):
    dict.get(a)()

print('选一种吧：\n1.+\n2.-\n3.*\n4./\n5.%\n6.exit')
while(True):
    z = int(input('你的选择：'))
    if 1<=z<=6:
        start(z)
    else:
        print('不在范围内')