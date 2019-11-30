#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (45.01%)
# Likes:    547
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 52.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#
class Solution:
    def trap(self, height) -> int:
        sum = 0
        stack_tem = []
        current = 0
        while current < len(height):
            while len(stack_tem) > 0 and height[current] > height[stack_tem[-1]]:
                h = height[stack_tem[-1]]
                stack_tem.pop(-1)
                if len(stack_tem) == 0:
                    break
                #相当于横向一层一层的计算雨水量
                distance = current - stack_tem[-1] - 1
                min_h = min(height[current], height[stack_tem[-1]])
                sum += distance * (min_h - h)
            stack_tem.append(current)
            current += 1
        return sum
if __name__=='__main__':
    test = Solution()
    test.trap([0,1,0,2,1,0,1,3,2,1,2,1])
