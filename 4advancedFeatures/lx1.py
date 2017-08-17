#修改列表生成式，使其正确执行
L1 = ['Hello', 'World', 18, 'Apple', None]
# print(s.lower() for s in L1)
print([s.lower() for s in L1 if isinstance(s,str)])