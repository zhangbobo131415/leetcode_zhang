#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if k >= 1:
            pass
        else:
            return
        self.k = k
        self.nums = nums.copy()
        self.nums_len = len(self.nums)
        heapq.heapify(self.nums)
        if self.nums_len > self.k:
            for _ in range(len(self.nums) - self.k):
                heapq.heappop(self.nums)
            self.nums_len = len(self.nums)    

    def add(self, val: int) -> int:
        if self.nums_len < self.k:
            heapq.heappush(self.nums, val)
            self.nums_len += 1
        else:
            if val <= self.nums[0]:
                pass
            else:
                heapq.heappushpop(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

