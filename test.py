# leetcode 38
# class Solution:
#     def tongji(self, zifuchuan):
#         mylen = len(zifuchuan)
#         jieguo = []
#         count = 1
#         for firstindex in range(mylen-1):
#             if zifuchuan[firstindex] == zifuchuan[firstindex+1]:
#                 count += 1
#             else:
#                 jieguo.append(str(count))
#                 jieguo.append(zifuchuan[firstindex])
#                 count = 1
#         jieguo.append(str(count))
#         jieguo.append(zifuchuan[mylen-1])
#         return jieguo

#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return "1"
#         if n == 2:
#             return "11"
#         temlist=['1','1']
#         for firstindex in range(3,n+1):
#             temlist=self.tongji(temlist)
#         res2=""
#         for j in range(len(temlist)):
#             res2=res2.__add__(temlist[j])
#         return res2
# test = Solution()
# print(test.countAndSay(6))

# s = "dsfaff"
# s=s.replace("f","ww")
# m=[3,4,5,6]
# a=m.reverse()
# tem={}
# tem=tem.fromkeys(m,1)
# print(tem.items())
# print(tem.__len__())
# print(6 in tem.keys())
# print(5%2)

# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         if n<=0:
#             return
#         if n==1:
#             return 0
#         if n==2:
#             return 1
#         if n%2==0:
#             return self.integerReplacement(int(n/2))+1
#         if n%2==1:
#             return min(self.integerReplacement(int(n+1))+1,self.integerReplacement(int(n-1))+1)

# test=Solution()

# print(test.integerReplacement(86))

# def myfun(tem):
#     tem.append("5656")

# mylist=[]
# myfun(mylist)
# print(mylist)

# s="fsdfsfsa"
# m=s[0:3]
# print(id(m),id(s))
# l=[]
# l.append(s[0:3])
# print(l)

#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (42.73%)
# Total Accepted:    5.7K
# Total Submissions: 13.2K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#
# class Solution:

#     def __init__(self):
#         self.mylist=[]
#     def hefa(self,s):
#         if int(s)<=255 and str(int(s))==s:
#             return True
#         else:
#             return False
#     def myfunction(self,s,listbiao,cengshu,jieguolist):
#         #print(s)
#         if len(s)==0 and cengshu <=4:
#             return
#         if cengshu ==4 :
#                 listbiao.append(s)
#                 if self.hefa(s):
#                     tem=listbiao.copy()
#                     jieguolist.append(tem)

#                     listbiao.pop()
#                     return
#                 else:
#                     listbiao.pop()
#                     return
#         for firstindex in range(1,4):
#             if self.hefa(s[0:firstindex]):
#                 listbiao.append(s[0:firstindex])
#                 self.myfunction(s[firstindex:s.__len__()],listbiao,cengshu+1,jieguolist)
#                 listbiao.pop()
#             else:
#                 return
#     def restoreIpAddresses(self, s: str) :
#         temlist=[]
#         self.myfunction(s,temlist,1,self.mylist)
#         reslist=[]
#         for temm in self.mylist:
#             reslist.append('.'.join(temm))
#         print(reslist)

# test=Solution()
# test.restoreIpAddresses("25525511135")

# def f1(func):
#     def f2(*args, **kwargs):

#         print('有火眼金睛了')
#         return func(*args, **kwargs)
#     return f2()

# def f3(func):
#     def f4(*args, **kwargs):
#         print('有金箍棒了')
#         return func(*args, **kwargs)
#     return f4

# def f5(func):
#     def f6(*args, **kwargs):
#         print('学会飞、72变了')
#         return func(*args, **kwargs)
#     return f6

# # @f1
# # @f3
# # @f5
# def f7():
#    print('吃桃子')

# f7()

# class Solution:
#     def findDuplicates(self, nums):
#         nums_len = nums.__len__()
#         reslist = []
#         if nums_len == 0:
#             return reslist
#         for tem in nums:
#             if tem < 1 or tem > nums_len:
#                 return False
#         for firstindex in range(nums_len):
#             while firstindex != (nums[firstindex] - 1):
#                 if nums[firstindex] == nums[nums[firstindex]-1]:
#                     break
#                 else:
#                     nums[nums[firstindex]-1], nums[firstindex] = nums[firstindex], nums[nums[firstindex]-1]
#         for firstindex in range(len(nums)):
#             if firstindex !=(nums[firstindex]-1):
#                 reslist.append(nums[firstindex])
#         return reslist

# test = Solution()
# print(test.findDuplicates([4,3,2,7,8,2,3,1]))

# class Solution:
#     def searchMatrix(self, matrix, target) -> bool:
#         firstindex = matrix.__len__() - 1
#         if firstindex<0:
#             return
#         maxrow = len(matrix[0])
#         j = 0  #从矩阵的左下角开始
#         while firstindex >= 0 and (j < maxrow):
#             print(matrix[firstindex][j])
#             if matrix[firstindex][j] == target:
#                 return True
#             if matrix[firstindex][j] < target:
#                 j += 1
#             else:
#                 firstindex-=1
#         return False

# test = Solution()
# print(test.searchMatrix([], 13))

#python 传参解析！！！！！
# def f (m):
#     m=[]
#     print(id(m))

# test= [1,2,3]
# print(id(test),test)
# f(test)
# print(id(test),test)
# def f2(k):
#     print(id(k),k)
#     k=k+1
#     print(id(k),k)
#     k=k+1
#     print(id(k),k)

# tem =5
# print(id(tem))
# tem+=1
# print(id(tem))
# f2(tem)
# print(tem)

#最长不重复子串
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         fuzhudic={}
#         fuzhudic[s[0]]=0
#         changdu=[1]
#         for firstindex in range(1,len(s)):
#             if s[firstindex] not in fuzhudic.keys():
#                 fuzhudic[s[firstindex]]=firstindex
#                 changdu.append(changdu[firstindex-1]+1)
#             else:
#                 weizhi = fuzhudic[s[firstindex]]
#                 changdu.append(firstindex-weizhi)
#                 fuzhudic.clear()
#                 for tem in range(weizhi+1,firstindex+1):
#                     fuzhudic[s[tem]]=tem
#         print(changdu)

#反转整数
# class Solution:
#     def reverse(self, x: int) -> int:
#         fanwei=[-pow(2,31),pow(2,31)-1]
#         tem=abs(x)
#         resversnum=0
#         while tem:
#             resversnum=resversnum*10+tem%10
#             tem=int(tem/10)
#             if resversnum<fanwei[0] or resversnum>fanwei[1]:
#                 break
#         return resversnum

# class Solution:
#     def myAtoi(self, str: str) -> int:
#         len_str = len(str)
#         if len_str == 0:
#             return 0
#         firstindex = 0
#         res = 0
#         fanwei = [-pow(2, 31), pow(2, 31) - 1]
#         mark = 1

#         for i in range(len_str):
#             if str[i] != ' ':
#                 firstindex = i
#                 break
#         if str[firstindex] == '-' or str[firstindex].isdigit() or str[firstindex]=='+':
#             pass
#         else:
#             return 0
#         firstindex = 0

#         for i in range(len_str):
#             if str[i] == '-' or str[i].isdigit() or str[i]=='+':
#                 firstindex = i
#                 break
#         if str[firstindex] == '-':
#             firstindex += 1
#             mark = -1
#         elif str[firstindex]=='+':
#             firstindex+=1
#         shujubiaoji=1

#         for i in range(firstindex, len_str):
#             if i==firstindex:
#                 if not str[i].isdigit():
#                     return res

#             if str[i].isdigit():
#                 shujubiaoji=0
#                 res = res * 10 + int(str[i])
#                 if mark * res < fanwei[0]:
#                     return fanwei[0]
#                 elif mark * res > fanwei[1]:
#                     return fanwei[1]
#             else:
#                 if str[i]==' ' and shujubiaoji:
#                     pass
#                 else:
#                     return res*mark
#         return res * mark


class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        j = nums.__len__() - 1
        while i < j:
            while nums[i] != val and i < j:
                i += 1
            while nums[j] == val and j > i:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return i 


test = Solution()
print(test.removeElement([3, 2, 2, 3], 3))
