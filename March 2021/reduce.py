from functools import reduce
L = [1,2,3,4,5]
min_num = reduce(lambda x,y: x+y,L)
print(min_num)