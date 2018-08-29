连续子数组最大和

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        sum = 0
        Best = array[0]
        start = 0
        end = 0
        
        for i in range(len(array)):
            if sum < 0:
                sum = array[i]
                start = i
            else:
                sum += array[i]
            
            if sum >= Best:
                Best = sum
                end = i
        
        return Best
                

需要注意的是，sum的开始取值是0；
需要注意边界值条件