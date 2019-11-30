#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (49.05%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 23.9K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
#
#


class Solution:
    # 最有解法需要利用数学中的四平方和定理

    # 贪心算法无法找到最优解，因此错误
    # def numSquares(self, n: int) -> int:
    #     res = []
    #     tem = []
    #     for i in range(1, n):
    #         if i ** 2 <= n:
    #             tem.append(i ** 2)
    #         else:
    #             break
    #     while n > 0:
    #         _, n = self.firstindex(len(tem) - 1, tem, n, res)
    #     return len(res)
    # def firstindex(self, index, temlist, n, res):
    #     for ii in range(index, -1, -1):
    #         if temlist[ii] <= n:
    #             res.append(temlist[ii])
    #             return ii, n - temlist[ii]

    def numSquares(self, n: int) -> int:
        # 深度优先遍历
        import math,sys
        fanwei = int(math.sqrt(n))
        self.count = sys.maxsize
        self.backtrack(n, fanwei, 0)
        return self.count

    def backtrack(self, num, fanwi, count):
        if count > self.count:
            return
        for i in range(fanwi, 0, -1):
            if i ** 2 > num:
                pass
            elif i ** 2 == num:
                count += 1
                if count < self.count:
                    self.count=count
                return
            else:
                self.backtrack(num-i**2,i,count+1)


        # 动态规划时间会超
        import math
        res = [i for i in range(0, n+1)]
        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                res[i] = min(res[i], res[i - j * j] + 1)
        # print(res)
        return res[n]
        ######################

        #广度优先试试 时间也会超，还不如动态规划
        ###############
        # import math
        # depth = int(math.sqrt(n))
        # tem = [(n,0)]
        # while len(tem) > 0:
        #     curr, count = tem[0]
        #     tem.pop(0)
        #     for i in range(depth,0,-1):
        #         next_curr = curr - i * i
        #         if next_curr > 0:
        #             tem.append((next_curr, count + 1))
        #         elif next_curr == 0:
        #             return count + 1
                
            
if __name__ == "__main__":
    test = Solution()
    a = test.numSquares(7168)
    print(a)
