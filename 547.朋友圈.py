#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m_len = len(M)
        mark_list = [0 for i in range(m_len)]
        start_point = self.first_zero(mark_list)
        num_penyouquan = 0
        while start_point != -1:
            self.pengyouquan(start_point, mark_list, M)
            num_penyouquan += 1
            start_point = self.first_zero(mark_list, start_point)
        return num_penyouquan

    def first_zero(self, mark_list, point=0):
        for i in range(point, len(mark_list)):
            if mark_list[i] == 0:
                return i
            else:
                pass
        return - 1

    def pengyouquan(self, point, mark_list, M):
        tem_queque = []
        tem_queque.append(point)
        mark_list[point] = 1
        while len(tem_queque) > 0:
            root = tem_queque.pop(0)
            for point, value in enumerate(M[root]):
                if mark_list[point] == 0 and value == 1 and point != root:
                    tem_queque.append(point)
                    mark_list[point] = 1
