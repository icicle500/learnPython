#从上一级目录开始搜索包含特定字符的文件
import os


def lxlistdir(name):
    l = [x for x in os.listdir('../.') if not '.' in x] #名字里带点的不要
    ll = []
    for x in l:
        ll = [xx for xx in os.listdir('../%s' % x) if ('%s' % name) in xx] #名字里得带要求的字符
        print(('%s :' % x), ll)


lxlistdir('lx')