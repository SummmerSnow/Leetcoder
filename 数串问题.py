
"""
题目描述:
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。

++solution++
本题可以直接使用字符串比较大小，本来想着直接排序就行了，但其实不行，需要注意到一个问题：
比如12 123， 前两位一样，会导致123比123大，但其实还需要比较那个放在前面。

本题主要是在考察把问题转换为字符串比较大小的问题，需要比较 x+y 和 y+x的大小！！！
"""


import sys
from functools import cmp_to_key
def cmp(x, y):
    if x+y > y+x:
        return 1
    elif x==y:
        return 0
    else:
        return -1

for i, line in enumerate(sys.stdin.readlines()):
    if i % 2 == 1:
        arrays = [item  for item in line.strip().split(' ')]
        arrays.sort(key=cmp_to_key(cmp), reverse=True)
    
        s = ""
        for item in arrays:
            s += item
        print(s)
