#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
import sys
import numpy as np
class Solution:
    def increasingTriplet(self, nums) -> bool:
        nums_len = len(nums)
        if nums_len < 3:
            return False
        #保存当前位置左侧最小值
        list_min = [sys.maxsize for i in range(nums_len)]
        #保存当前位置右侧最大值
        list_max = [-sys.maxsize for i in range(nums_len)]
        for i in range(1, nums_len):
            list_min[i] = min(list_min[i - 1], nums[i - 1])
        for i in range(nums_len - 2, -1, -1):
            list_max[i] = max(nums[i + 1], list_max[i + 1])
        for i in range(1, nums_len - 1):
            if list_min[i] < nums[i] < list_max[i]:
                return True
        return False
        
# test = Solution()
# test.increasingTriplet([5,1,5,5,2,5,4])
            
        
        

