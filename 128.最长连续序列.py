#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (42.17%)
# Total Accepted:    6.3K
# Total Submissions: 14.7K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#


# 使用一个字典保存nums[i]和它的索引i。
# 使用mark数组表示mark[i]是否被访问过。
# res保存连续序列的长度
# 对于nums[i]，需要向上查找nums[i]+1是否在字典中，
# 如果在(参考注释[1])；然后向下寻找nums[i]-1(参考注释[2])
class Solution:
    def longestConsecutive(self, nums) -> int:
        res=[ i for i in range(nums.__len__())]
        tem_dict = dict(zip(nums, res))
        mark = [ 1 for i in range(nums.__len__())]
        if res.__len__()==0:
            return 0
        for (i, j) in enumerate(nums):
            tem = j 
            res[i] = 0
            if mark[i]:
                while (j in tem_dict) and mark[tem_dict[j]]:
                    #注释[1]
                    mark[tem_dict[j]] = 0
                    res[i]+=1
                    j = j + 1
                j = tem -1
                while (j in tem_dict) and  mark[tem_dict[j]]:
                    #注释[2]
                    mark[tem_dict[j]] = 0
                    res[i]+=1
                    j = j - 1
        return max(res)
# if __name__=="__main__":
#     import time
#     test1 = Solution()
#     data = [x for x in range(-999,9001)]
#     start = time.time()
#     test1.longestConsecutive(data)
#     print("fdasfa")
#     print(time.time()-start)
            

