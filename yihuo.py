一个数组都是两个数字成对出现，只有两个数字是单独出现，求出这两个数字

solution1： 直接存在数组里面，如果有就删除，没有就加入数组
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        #tmp = set()
        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp


        
solution2： 抑或解法
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    """

    """

    def FindNumsAppearOnce(self, array):
        # first step：  xor all numbers in array
        xo = 0
        for item in array:
            xo = xo ^ item
        # second step:  find the first 1's index in the result of xor

        if xo == 0:
            return [0, 0]
        index = 0
        while ((xo & 1) == 0):
            xo >> 1
            index += 1
        # xor each array with index position of xor result

        number1 = 0
        number2 = 0

        for item in array:
            if self.Split(item, index):
                number1 = number1 ^ item
            else:
                number2 = number2 ^ item
        # the you can divided the different numbers into only one numbers
        return (number1, number2)

    def Split(self, data, index):

        data = data >> index

        return (data & 1)