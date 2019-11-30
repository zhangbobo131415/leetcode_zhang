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

# class Solution:
#     def removeElement(self, nums, val: int) -> int:
#         i = 0
#         j = nums.__len__() - 1
#         while i < j:
#             while nums[i] != val and i < j:
#                 i += 1
#             while nums[j] == val and j > i:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
#         return i

# class Solution:
#     def search(self, nums, target: int) -> int:
#         last_index_nums=len(nums)-1
#         first_indeex_nums=0
#         mid_index=int((last_index_nums+first_indeex_nums)/2)
#         while True:
#             if nums[mid_index]>nums[first_indeex_nums]:
#                 first_indeex_nums=mid_index
#                 mid_index=int((last_index_nums+first_indeex_nums)/2)
#             else:
#                 last_index_nums=mid_index
#                 mid_index=int((last_index_nums+first_indeex_nums)/2)

#leetcode 329
# class Solution:
#     def longestIncreasingPath(self, matrix) -> int:

#         col_matrix = len(matrix)
#         if col_matrix == 0:
#             return 0

#         row_matrix = len(matrix[0])
#         if row_matrix == 0:
#             return 0
#         res_matrix = [[0 for i in range(row_matrix)]
#                       for j in range(col_matrix)]
#         res_matrix[0][0] = 1
#         result=1
#         #先获得递减子序列
#         for i in range(1, col_matrix):
#             if matrix[i][0] < matrix[i - 1][0]:
#                 res_matrix[i][0] = res_matrix[i - 1][0] + 1
#             else:
#                 res_matrix[i][0] = 1
#         for i in range(1, row_matrix):
#             if matrix[0][i] < matrix[0][i - 1]:
#                 res_matrix[0][i] = res_matrix[0][i - 1] + 1
#             else:
#                 res_matrix[0][i] = 1
#         tem1 = tem2 = 0
#         for i in range(1, col_matrix):
#             for j in range(1, row_matrix):
#                 if matrix[i][j] < matrix[i - 1][j]:
#                     tem1 = res_matrix[i - 1][j] + 1
#                 if matrix[i][j] < matrix[i][j - 1]:
#                     tem2 = res_matrix[i][j - 1] + 1
#                 res_matrix[i][j] = max(tem1, tem2, 1)
#                 result=max(result,res_matrix[i][j])
#                 tem1 = tem2 = 0

#         for i in range(1, col_matrix):
#             if matrix[i][0] > matrix[i - 1][0]:
#                 res_matrix[i][0] = res_matrix[i - 1][0] + 1
#             else:
#                 res_matrix[i][0] = 1
#         for i in range(1, row_matrix):
#             if matrix[0][i] > matrix[0][i - 1]:
#                 res_matrix[0][i] = res_matrix[0][i - 1] + 1
#             else:
#                 res_matrix[0][i] = 1
#         tem1 = tem2 = 0
#         for i in range(1, col_matrix):
#             for j in range(1, row_matrix):
#                 if matrix[i][j] > matrix[i - 1][j]:
#                     tem1 = res_matrix[i - 1][j] + 1
#                 if matrix[i][j] > matrix[i][j - 1]:
#                     tem2 = res_matrix[i][j - 1] + 1
#                 res_matrix[i][j] = max(tem1, tem2, 1)
#                 tem1 = tem2 = 0
#                 result=max(result,res_matrix[i][j])

#         return result

#test = Solution()

# class Solution:
#     def permuteUnique(self, nums):
#         res = []
#         tem = []
#         nums.sort()
#         res.append(nums.copy())
#         tem = nums.copy()
#         tem.sort(reverse=True)
#         while nums != tem:
#             self.nextPermutation(nums)
#             res.append(nums.copy())
#         print(res)

#     def nextPermutation(self, nums) -> None:
#         # maxtem = nums.copy()
#         # maxtem.sort(reverse=True)
#         # if maxtem == nums:
#         #     nums.sort()
#         # else:
#         for i in range(nums.__len__() - 1, 0, -1):
#             if nums[i] > nums[i - 1]:
#                 qianzhuilist = nums[0:i - 1]
#                 houzhuilist = nums[i - 1:nums.__len__()]
#                 houzhuilist.sort(reverse=True)
#                 weizhi = houzhuilist.index(nums[i - 1])
#                 qianzhuilist.append(houzhuilist.pop(weizhi - 1))
#                 houzhuilist.sort()
#                 qianzhuilist.extend(houzhuilist)
#                 for tem in range(qianzhuilist.__len__()):
#                     nums[tem] = qianzhuilist[tem]
#                 break

# test = Solution()
# test.permuteUnique([1, 1, 2])

# yingshe_dic={}
# yingshe_dic[2]=['a','b','c']
# print(yingshe_dic[2].__len__())

# a=[1,2,3]
# b=str(a)
# print(type(b))
# print(b)
# m=['1','2']
# print(m)
# import re
# print(re.match(".*","ab12123"))
# p=[1]
# print(5//2)

# import time
# a=[]
# b=[]
# count=10000000
# for i in range(count):
#     a.append(i)
#     b.append(i)
# start=time.time()
# for i in range(count):
#     pass
# end=time.time()
# print(end-start)
# start=time.time()
# for i in range(count):
#     a.pop()
# end=time.time()
# print(end-start)
# start=time.time()
# for i in range(count):
#     del(b[-1])
# end=time.time()
# print(end-start)
# print(a,b)

# class person(object):
#     def __init__(self,x):
#         self.age=x
#     def fuckkk(self):
#         print(self.age)

# def fuck(self,x):
#     print(self.age<x.age)
# def __le__(self,x):
#     return self.age<x.age

# person.fuck=types.MethodType(fuck,person)

# person.num=110
# test=person(20)
# test2=person(15)
# print(test.age,test.num,test2.age,test2.num)
# test2.num=210
# print(test.age,test.num,test2.age,test2.num)
# person.fuck=types.MethodType(fuck,test)
# test.__le__=types.MethodType(__le__,test)
# test.__le__=types.MethodType(__le__,test2)
# print(test>test2)

# import re
# a=re.match('.*','abgsfdg')
# b=re.match('a','aa')
# print(a.span()[1])
# print(b)

#关键时去寻找一个映射，一个将有相同字母组成的单词映射为同一个值的映射。
#这里主要是将字符串专为列表，然后进行字典排序，这样具有相同字母组成的字符串就对应同一个列表了
# class Solution:
#     def groupAnagrams(self, strs):
#         strslen = strs.__len__()
#         res = []
#         #tem用来存放字典排序后的列表
#         tem = []
#         if strslen <= 0:
#             return []
#         for i in range(0, strslen):
#             tem_root = self.str_to_list(strs[i])
#             tem_root.sort()
#             #判断当前字符串的字典排序列表是否存在于tem中
#             if tem_root in tem:
#                 index_root = tem.index(tem_root)
#                 res[index_root].append(strs[i])
#             else:
#                 #否则tem和res均append一下
#                 res.append([strs[i]])
#                 tem.append(tem_root)
#         print(res)
#         return res

#     def str_to_list(self, strs):
#         res = []
#         for i in range(len(strs)):
#             res.append(strs[i])
#         return res

# test = Solution()
# test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         len_haystack = len(haystack)
#         len_needle = len(needle)
#         next = [0 for i in range(len_needle)]
#         if len_needle == 0:
#             return 0
#         for i in range(1, len_needle):
#             if needle[i] == needle[next[i - 1]]:
#                 next[i] = next[i - 1] + 1
#             else:
#                 temmm=next[i-1]-1
#                 while temmm:
#                     if needle[i] == needle[next[temmm]]:

#                         next[i] = next[temmm]+1
#                         break
#                     temmm=next[temmm]-1

#         print(next)
#         next.insert(0,-1)
#         next.pop()
#         print(next)
#         haindex=neindex=0
#         while haindex<len_haystack:
#             if haystack[haindex]==needle[neindex]:
#                 haindex,neindex=haindex+1,neindex+1
#             else:
#                 if neindex==0:
#                     haindex+=1
#                 else:
#                     neindex=next[neindex]
#             if neindex==len_needle:
#                 return haindex-neindex
#         return -1

# test = Solution()
# test.strStr("aabaaabaaac","aabaaac")

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         lenofs = len(s)
#         tem_res = [0 for i in self.dingyihanshu(0, lenofs, 0.5)]
#         mid = [i for i in self.dingyihanshu(0, lenofs, 0.5)]
#         for j in mid:
#             if int(j) == j:
#                 j = int(j)
#                 for k in range(1, j + 1):
#                     if j + k <= lenofs - 1 and s[j + k] == s[j - k]:
#                         tem_res[j * 2] += 2
#                     else:
#                         break
#                 tem_res[j * 2] += 1
#             else:
#                 for k in range(int(j), -1, -1):
#                     if int(j * 2 - k) <= lenofs - 1 and s[k] == s[int(j * 2 -
#                                                                       k)]:
#                         tem_res[int(j * 2)] += 2
#                     else:
#                         break
#         print(tem_res)
#         maxlen = max(tem_res)
#         index = tem_res.index(maxlen)
#         if mid[index] == int(mid[index]):
#             return s[int(mid[index]) - maxlen // 2:int(mid[index]) +
#                      maxlen // 2 + 1]
#         else:
#             return s[int(mid[index]) - maxlen//2 + 1:int(mid[index]) + maxlen//2 + 1]

#     def dingyihanshu(self, start, end, step):
#         end = end - 1
#         while start <= end:
#             yield start
#             start = start + step

# test = Solution()

# print(test.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

#leetcode 199 左子树先进队列，判断条件很麻烦，层次遍历取层的最后#一个节点
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         tem = []
#         res = []
#         depth = 0
#         if root:
#             tem.append((root, depth))
#         else:
#             return res
#         while tem.__len__() >= 1:
#             top = tem[0][0]
#             depth = tem[0][1]
#             if top.left:
#                 tem.append((top.left, depth + 1))
#             if top.right:
#                 tem.append((top.right, depth + 1))
#             tem.pop(0)
#             if tem.__len__() > 0 and depth != tem[0][1]:
#                 res.append(top.val)
#         if res.__len__() == 0 or depth != res.__len__() - 1:
#             res.append(top.val)
#         return res

#leetcode 199 右子树先进队列写起来果然简单很多
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         tem = []
#         res = []
#         depth = 1
#         if root:
#             tem.append((root, depth))
#         else:
#             return res
#         while tem.__len__() >= 1:
#             top = tem[0][0]
#             depth = tem[0][1]
#             if top.right:
#                 tem.append((top.right, depth + 1))
#             if top.left:
#                 tem.append((top.left, depth + 1))
#             if res.__len__() < depth:
#                 res.append(top.val)
#             tem.pop(0)
#         return res

# leetcode 3
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         fuzhu_dic = {s[0]:0}
#         changdu = [1]
#         for i in range(1, len(s)):
#             if s[i] not in fuzhu_dic:
#                 fuzhu_dic[s[i]] = i
#                 changdu.append(changdu[i-1]+1)
#             else:
#                 end_weizhi = fuzhu_dic[s[i]]
#                 start_weizhi = i - changdu[-1]
#                 changdu.append(i - end_weizhi)
#                 fuzhu_dic[s[i]] = i
#                 for tem in range(start_weizhi, end_weizhi):
#                     fuzhu_dic.pop(s[tem])
#         return max(changdu)

# class mytest:
#     def __init__(self):
#         self.x = 25

#     def __iter__(self):
#         print("mydata")
#         return self.x

# from collections import Iterable

# test = mytest()
# hehee = [1, 2, 3]
# print(sum(test))
if __name__ == "__main__":

    import time


    def time_cost(func):
        def warrper(x):
            print(func.__name__, "is runing")
            start = time.time()
            func(x)
            end = time.time()
            print(end - start)
        return warrper

    @time_cost
    def chuyi2(x):
        for i in range(x):
            i // 2
        return

    @time_cost
    def weiyunxuan(x):

        for i in range(x):
            i & 1
        return

    @time_cost
    def testtt(x):
        print(x)

    # 结果出错
    # testtt(500)
    # chuyi2(1000000)
    # weiyunxuan(1000000)


    #vscode 输出结果
    # testtt is runing
    # 500
    # 0.0070743560791015625
    # chuyi2 is runing

    #pycharm输出结果：
    # testtt is runing
    # 500
    # 0.0
    # chuyi2 is runing
    # 0.10937356948852539
    # weiyunxuan is runing
    # 0.10937738418579102
    class Solution:
        def longestConsecutive(self, nums) -> int:
            tem_dict = dict()
            res=[ 0 for i in range(nums.__len__())]
            if res.__len__()==0:
                return 0
            for j in nums:
                tem_dict[j] = j + 1
            for (i, j) in enumerate(nums):
                while j in tem_dict:
                    res[i]+=1
                    j = j + 1
            print( max(res))

    # test1 = Solution()
    # data = [x for x in range(-999,9001)]

    # test1.longestConsecutive(data)

    # class KthLargest:
    #     def __init__(self, k: int, nums: List[int]):
    #         self.k = k
    #         self.nums = nums.copy()
    #     def add(self, val: int) -> int:
    #         pass
    you_kuohao = dict(zip([')', ']', '}'],['(', '[', '{']))
    print(you_kuohao)
    
   

    