#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (35.65%)
# Total Accepted:    2.1K
# Total Submissions: 5.9K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         tmp = {0:1}
#         pre_sum = []
#         count = 0
#         for index, num in enumerate(nums):
#             if index == 0:
#                 pre_sum.append(num)
#             else:
#                 pre_sum.append(pre_sum[-1] + num)

#             if (pre_sum[-1] - k) in tmp:
#                 count += tmp[pre_sum[-1] - k]

                
#             if pre_sum[-1] in tmp:
#                 tmp[pre_sum[-1]] += 1
#             else:
#                 tmp[pre_sum[-1]] = 1
#         return count

import collections             
import heapq
class Solution_:
    def topKFrequent(self, nums, k: int):
        count = collections.Counter(nums)  
        return heapq.nlargest(k, count.keys(), key=count.get) 
        # return nums

data = [1, 1, 1, 2, 2, 3]
test = Solution_()
res = test.topKFrequent(data, 2)
print(res )
        

