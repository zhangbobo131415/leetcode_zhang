#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (42.77%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 18.8K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.

class Solution:
    def canPartition(self, nums) -> bool:
        # size = len(nums)
        # s = sum(nums)
        # if s & 1 == 1:
        #     return False

        # # 从第 2 行以后，当前行的结果参考了上一行的结果，因此使用一维数组定义状态就可以了
        # target = s // 2
        # dp = [False for _ in range(target + 1)]

        # # 看看第 1 个数是不是能够刚好填满容量为 target
        # for j in range(target + 1):
        #     if nums[0] == j:
        #         dp[j] = True
        #         # 如果等于，后面就不用做判断了，因为 j 会越来越大，肯定不等于 nums[0]
        #         break

        # # 注意：因为后面的参考了前面的，我们从后向前计算
        # for i in range(1, size):
        #     for j in range(target, -1, -1):
        #         if j >= nums[i]:
        #             dp[j] = dp[j] or dp[j - nums[i]]
        #         else:
        #             # 后面的容量越来越小，因此没有必要再判断了，退出当前循环
        #             break

        # return dp[-1]



        zonghe = sum(nums)
        if zonghe & 1 == 1 or len(nums) == 1:
            return False
        tem = [False for i in range(zonghe // 2 + 1)]
        tem[0] = True
        length = zonghe // 2
        for k in nums:
            if k<=length:
                tem[k] = True
                break
                
        
        for index, num in enumerate(nums):
            if index == 0:
                continue
            if num > length:
                break
            for j in range(length, num-1, -1):
                tem[j] = tem[j] or tem[j-num]
            print(tem)
        return tem[-1]
                    






        # 字典加速不行
        # tem = {0:2}
        # zonghe = sum(nums)
        # if zonghe & 1 == 1 or len(nums) == 1:
        #     return False
        # for i in nums:
        #     for j in range(i,max(tem)+i+1):
        #         if (j - i) in tem:
        #             if j in tem:
        #                 tem[j] += 1
        #             else:
        #                 if j % i == 0:
        #                     if tem[j - i] >= j // i:
        #                         tem[j] = 1
        #                 else:
        #                     tem[j] = 1
                    
                    
        #     print(repr(tem))
        # # print(max(tem))
        # if zonghe // 2 in tem:
        #     return True
        # else:
        #     return False



    #     if len(nums) == 0:
    #         return True
    #     elif len(nums) == 1:
    #         return False
    #     nums.sort()
    #     zonghe = sum(nums)
    #     print(zonghe)
    #     max_num = nums[-1]
    #     nums.pop(-1)
    #     dict_1 = {}
    #     dict_2={max_num:1,0:1}
    #     if max_num > sum(nums) or abs(max_num - sum(nums)) & 1 == 1:
    #         return False
    #     else:
    #         if abs(zonghe - max_num * 2) == 0:
    #             return True
    #         for i in nums:
    #             if i in dict_1:
    #                 dict_1[i] += 1
    #             else:
    #                 dict_1[i] = 1
    #         return self.chazhao(dict_1,dict_2,abs(zonghe-max_num*2)//2,nums)
    # def chazhao(self,set_1, set_2, chazhi,nums):
    #     for i in set_2.keys():
    #         if (i + chazhi) in set_1:
    #             return True
    #     i = len(nums) - 1
    #     while i >= 0:
    #         if nums[i] < chazhi:
    #             set_2[nums[i]] = 1
    #             if set_1[nums[i]] == 1:
    #                 set_1.pop(nums[i])
    #             else:
    #                 set_1[nums[i]] -= 1
    #             print(chazhi)
    #             chazhi = chazhi - nums[i]
    #             print(nums)
    #             print(sum(nums))
    #             if chazhi == 0:
    #                 return True
    #             nums.pop(i)
    #             i = len(nums) - 1
    #             for j in set_2.keys():
    #                 if (j + chazhi) in set_1:
    #                     return True
    #         else:
    #             i-=1
    #             # return self.chazhao(set_1,set_2,chazhi,nums)
                
    #     return False
if __name__ == '__main__':
    test = Solution()
    a = test.canPartition([1,3,6])
    print(a)
