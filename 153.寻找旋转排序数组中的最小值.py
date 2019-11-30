#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (48.74%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 26.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 你可以假设数组中不存在重复元素。
# 
# 示例 1:
# 
# 输入: [3,4,5,1,2]
# 输出: 1
# 
# 示例 2:
# 
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 
#
class Solution:
    # 如果nums[start_index]==nums[end_index]，就需要在这二者之间使用线性查找
    def findMin(self, nums) -> int:
        if len(nums) <= 0:
            return None
        return self.find(0, len(nums) - 1, nums)
    def find(self, start_index, end_index, nums):
        if start_index < end_index:
            pass
        else:
            return nums[start_index]
        mid = (start_index + end_index) // 2
        if nums[mid] <= nums[end_index] and nums[mid] >= nums[start_index]:
            return nums[start_index]
        elif nums[mid] >= nums[start_index]:
            result = self.find(mid + 1, end_index, nums)
        elif nums[mid] <= nums[end_index]:
            result = self.find(start_index, mid, nums)
        else:
            print("额外情况")
        return result
if __name__ == "__main__":    
    test = Solution()
    print(test.findMin([3,1,2]))
            
        

