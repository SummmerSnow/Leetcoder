出现次数超过一半的数字

# -*- coding:utf-8 -*-
class Solution:
    """
    solution:
    如果某个数字出现的次数超过一半，那么其出现的次数必定比所有其他数组出现的次数之和要多；
    所以最后一次次数为0的那个数字就是数组超过一半的数字
    需要两个变量，一个保存最后设置数组为0的变量，一个表示次数；
    """
    def MoreThanHalfNum_Solution(self, numbers):
        count = 0
        result = numbers[0]
        
        for item in numbers:
            if count == 0:
                result = item
                count = 1
            elif item == result:
                count += 1
            else:
                count -= 1
        if not (self.CheckIfMoreThanHalf(result, numbers)):
            result = 0
        return result
    
    def CheckIfMoreThanHalf(self, result, numbers):
        count = 0
        for item in numbers:
            if item == result:
                count += 1
        
        half_length = len(numbers) // 2
        
        if count > half_length:
            return True
        else:
            return False
                
            