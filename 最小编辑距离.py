# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 下午11:31
# @Author  : xiaoxue liu
# @File    : 最小编辑距离.py
# @Descript:

a = "asdfghjk"
b = "sddfghjeft"

"""
get the shortest edit distance

if i=0 and j=0:
    dis[i][j] = 0

if i >0; j = 0;
    dis[0][j] = j

if j > 0; i = 0;
    dis[i][0] = i;
    
if i>0, j > 0
    dis[i][j] = min(dis[i-1][j]+1, dis[i][j-1]+1, dis[i-1][j-1]+flag)
    #flag 表示两个字符是否是相同的字符
"""

def getEditDistance(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    matrix = [[i+j for j in range(len2+1)] for i in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):

            if str1[i-1] == str2[j-1]:
                flag=0
            else:
                flag=1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+flag)

    print("the min edit distance is %d" % (matrix[len1][len2]))


getEditDistance(a, b)






