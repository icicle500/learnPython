print([x*x for x in range(1,11)])

print('\n',[x*x for x in range(1,11) if x%2==0]) 
#加了if判断，这样可以筛选出仅有偶数的平方

print('\n',[m+n for m in 'ABC' for n in 'XYZ'])
#两层循环可以生成全排列