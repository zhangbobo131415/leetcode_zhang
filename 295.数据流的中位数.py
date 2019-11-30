#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_max = []
        self.heap_min = []
        self.data_length = 0
    def addNum(self, num: int) -> None:
        if self.data_length & 1 == 0:
            if len(self.heap_min) - len(self.heap_max) == 1:
                heapq.heappush(self.heap_max, -heapq.heappushpop(self.heap_min,num))
            else:
                heapq.heappush(self.heap_min, num)
        else:
            if len(self.heap_max) - len(self.heap_min) == 1:
                heapq.heappush(self.heap_min, -heapq.heappushpop(self.heap_max, -num))
            else:
                heapq.heappush(self.heap_max, -num)
        self.data_length += 1
        print(self.heap_max)
        print(self.heap_min)
 
    def findMedian(self) -> float:
        if len(self.heap_max) < len(self.heap_min):
            return self.heap_min[0]
        elif len(self.heap_max) == len(self.heap_min):
            return (self.heap_min[0] - self.heap_max[0]) / 2
        else:
            return -self.heap_max[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

