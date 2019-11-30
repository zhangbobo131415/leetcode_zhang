#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
class Solution:
    # 简单的回溯算法时间复杂度太高！！
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) == 0:
    #         return False
    #     if nums[0] == 0 and len(nums) !=1:
    #         return False
    #     if nums[0] == 0 and len(nums) == 1:
    #         return True
    #     return self.back(nums, 0)

    # def back(self, nums, loc):
    #     if loc >= len(nums) - 1:
    #         return True
        
    #     for index in range(nums[loc], 0, -1):
    #         if self.back(nums, loc + index) == True:
    #             return True
    #     return False
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if nums[0] == 0 and len(nums) !=1:
            return False
        if nums[0] == 0 and len(nums) == 1:
            return True
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(i + nums[i], dp[i - 1])
            if dp[i] <= i:
                if i < len(nums) - 1:
                    return False
                else:
                    return True
        return True
            
 


