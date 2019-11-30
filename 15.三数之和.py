#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (21.50%)
# Total Accepted:    42.1K
# Total Submissions: 196K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums):
        length=len(nums)
        if len(nums) <= 2:
            return None
        res = []
        nums.sort() 
        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num:
                continue
            if num > 0:
                break
            left = index + 1
            right = length - 1
            taget = num
            while left < right:
                if taget + nums[left] + nums[right] > 0:
                    right -= 1
                elif taget + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([taget, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                        right -= 1
                        left += 1
        return res 
                    



        # if len(nums) <= 2:
        #     return
        # res=[]
        # tem={}
        # nums.sort()
        # start_2 = -1
        # if start_2 == -1 and nums[-1]>0:
        #     return []
        # if nums[-1] < 0:
        #     return []

        # for index, num in enumerate(nums):
        #     if num not in tem:
        #         tem[num] = 1
        #     else:
        #         tem[num] += 1
        #     if num < 0:
        #         start_2 = index
        # for index_1, num_1 in enumerate(nums):
        #     if nums[index_1] > 0:
        #         break
        #     tem[nums[index_1]] -= 1
        #     for index_2 in range(start_2 + 1, len(nums)):
        #         tem[nums[index_2]] -= 1
        #         if (0 - nums[index_1] - nums[index_2]) in tem and tem[0 - nums[index_1] - nums[index_2]] > 0:
        #             tem_list = [nums[index_1], nums[index_2], 0 - nums[index_1] - nums[index_2]]
        #             tem_list.sort()
        #             if tem_list not in res:
        #                 res.append(tem_list)
        #         tem[nums[index_2]] += 1
        # return res 
if __name__ == '__main__':
    data =[-1, 0, 1, 2, -1, -4]
    test = Solution()
    a = test.threeSum(data)
    print(a)
