#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.11%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    44.2K
# Total Submissions: 106.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        if length < 3:
            return
        sum_output = nums[0]+nums[1]+nums[-1]
        for i in range(length-2):
            left = i + 1
            right = length - 1
            while left < right:
                ans = nums[i] + nums[left] + nums[right]
                if abs(target - ans) < abs(target - sum_output):
                    sum_output = ans
                if ans - target < 0:
                    left += 1
                elif ans - target > 0:
                    right -= 1
                else:
                    return target
        return sum_output
                        
if __name__ == '__main__':
    test = Solution()
    a = test.threeSumClosest([0,2,1,-3],1)
    print(a)
        

