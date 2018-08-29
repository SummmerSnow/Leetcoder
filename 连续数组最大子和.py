# coding: utf8
"""
给定一个数字，找出连续数组的最大子和
"""

def ContinuousmaxSum(array):

    bestSum = array[0]
    sum = array[0]

    for i in range(1, len(array)):
        if sum > 0:
            sum += array[i]
        else:
            sum = array[i]

        if sum > bestSum:
            bestSum = sum

    print(bestSum)


"""
找出连续数组最大，要求数组序列是不相邻的
"""
def findMaxSumSeq(array):
    b = []
    b.append(array[0])
    b.append(array[1])

    if len(array) == 2:
        return max(b)

    for index in range(2, len(array)):
        temp_sum = max(b[:index-1])
        if temp_sum < 0:
            b.append(array[index])
        else:
            b.append(temp_sum + array[index])

    print(max(b))



"""
找到值递增的子序列
比如[100, 4, 200, 1, 3, 2]
值递增最大子序列是： [1, 2, 3, 4]
"""


def findSeq(array):
    # solution1: 利用一个集合set，然后用前后指针遍历集合，遍历完之后就删除集合
    res = 0
    ss = array.copy()

    for item in array:
        if item not in ss:
            continue
        pre = item - 1
        next = item + 1

        while pre in ss:
            ss.remove(pre)
            pre -= 1
        while next in ss:
            ss.remove(next)
            next += 1

        res = max(res, next-pre-1)
    print(res)
    return res

# solution2: 利用一个hash表，依然是利用前后指针，但是这种方法就需要更新整个列表
