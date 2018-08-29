# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 下午8:03
# @Author  : xiaoxue liu
# @File    : 切绳子.py
# @Descript:

"""
题目描述：  一段长为n的绳子，切成m段，m和n都是大于1的整数，
           求用动态规划求解，切成多少段的时候，各段长度的乘积最大？
"""

def maxAfterCutting(n):

    f = []
    f.append(0)
    if n < 4:
        return n
    f.append(1)
    f.append(2)
    f.append(3)

    for i in range(4, n+1):
        max_length = 0
        for j in range(1, 1+i//2):
            temp = f[j]*f[i-j]
            if temp > max_length:
                max_length = temp
        f.append(max_length)
    print(f[n])
    return f[n]

maxAfterCutting(8)
