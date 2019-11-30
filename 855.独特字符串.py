#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 独特字符串
#
# https://leetcode-cn.com/problems/exam-room/description/
#
# algorithms
# Medium (24.91%)
# Total Accepted:    369
# Total Submissions: 1.5K
# Testcase Example:  '["ExamRoom","seats","seats","seats","seats","leave","seats"]\n[[10],[],[],[],[],[4],[]]'
#
# 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
#
#
# 当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在
# 0 号座位上。)
#
# 返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seats() 会返回一个 int
# （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用
# ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。
#
#
#
# 示例：
#
# 输入：["ExamRoom","seats","seats","seats","seats","leave","seats"],
# [[10],[],[],[],[],[4],[]]
# 输出：[null,0,9,4,2,null,5]
# 解释：
# ExamRoom(10) -> null
# seats() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
# seats() -> 9，学生最后坐在 9 号座位上。
# seats() -> 4，学生最后坐在 4 号座位上。
# seats() -> 2，学生最后坐在 2 号座位上。
# leave(4) -> null
# seats() -> 5，学生最后坐在 5 号座位上。
#
#
#
#
# 提示：
#
#
# 1 <= N <= 10^9
# 在所有的测试样例中 ExamRoom.seats() 和 ExamRoom.leave() 最多被调用 10^4 次。
# 保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
#
#
#
class ExamRoom:
    def __init__(self, N: int):
        self.len = N
        self.res = [] #保存1的索引位置，有1的索引位置和长度可以得到一个座位序号
    def seat(self) -> int:
        if self.res.__len__() == 0:
            self.res.append(0)
            return 0
        if self.res.__len__() == self.len:
            return -1
        #head保存开头0的长度
        head = self.res[0] - 0
        #tail保存结尾0的长度
        tail = self.len - 1 - self.res[-1]
        mid = 0
        mid_index = self.res[0]
        for i in range(1, self.res.__len__()):
            real_len = self.res[i] - self.res[i - 1] - 1
            if real_len > 0:
                if real_len & 1 == 1:
                    real_len = (real_len >> 1) + 1
                else:
                    real_len = real_len >> 1
                if real_len > mid:
                    mid = real_len
                    mid_index = self.res[i - 1] + mid
        ouput = [(tail, self.len - 1), (mid, mid_index),
                 (head, 0)]
        ouput.sort(key=lambda x: x[0])
        #ouput[-1][1]即为seat的返回值，也就是要插入self.res中的值
        #在self.res中寻找插入位置
        mark_charu = False
        for index,value in enumerate(self.res):
            if value>ouput[-1][1]:
                self.res.insert(index, ouput[-1][1])
                mark_charu = True
                break
        if mark_charu==False:
            self.res.append(ouput[-1][1])
        return ouput[-1][1]

    def leave(self, p: int) -> None:
        for index,value in enumerate(self.res):
            if value == p:
                self.res.pop(index)
                break
        return
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seats()
# obj.leave(p)
