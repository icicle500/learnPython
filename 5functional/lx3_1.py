# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按姓名排序

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)