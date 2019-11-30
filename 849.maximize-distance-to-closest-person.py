#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode-cn.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (34.76%)
# Total Accepted:    3.2K
# Total Submissions: 9.1K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
#
# 至少有一个空座位，且至少有一人坐在座位上。
#
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
#
# 返回他到离他最近的人的最大距离。
#
# 示例 1：
#
# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
#
#
# 示例 2：
#
# 输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
#
#
# 提示：
#
#
# 1 <= seats.length <= 20000
# seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
#
#
#
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = []
        mid =0 
        for j, i in enumerate(seats):
            if i == 1:
                #保存1的索引位置，有这些索引位置可以计算0的长度
                res.append(j)
        #head保存开头0的长度
        head = res[0] - 0
        #tail保存结尾0的长度
        tail = seats.__len__() - 1 - res[-1]
        for i in range(1, res.__len__()):
            mid = max(mid, res[i] - res[i - 1] - 1)
        if mid & 1 == 1:
            mid = (mid >> 1) + 1
        else:
            mid = mid >> 1
        return max(head, mid , tail)
