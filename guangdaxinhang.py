# n, k = [int(i) for i in input().split()]
# def my_pow(n, k):
    
#     if k == 1:
#         return n
#     if k == 0:
#         return 1
#     tmp = my_pow(n, k // 2)

#     if k & 1 == 1:
#         return tmp * tmp * n
#     else:
#         return tmp * tmp


# data = [i for i in input()]
# data=input()
# mark=1
# # for i in range(len(data)):
# #     if data[i] == '0':
# #         mark =i
# #     else:
# #         break
# data = data[(mark - 1):len(data)]
# mark = 1
# stack=[]
# if len(data) <= 2:
#     print([])
# else:
#     i = 2
#     stack.append(data[0])
#     stack.append(data[1])
#     print(type(data))

#     while i < (len(data) - 1):
#         res_two = str((int(stack[-1])) + int(stack[-2]))
#         tmp = data.find(res_two, i)
#         # print(res_two,tmp)
#         if tmp != -1:
#             i = tmp  + len(res_two)
#             stack.append(res_two)
#             if (i) == len(data):
#                 data = [int(i) for i in data]
#                 print(data)
#         else:
#             if i + len(res_two) == len(data):
#                 pass
#             else:
#                 mark = 0
#                 print([])
#                 break
         

data = input()
data =data[1:-1]
data = [int(i) for i in data.split(',')]

def jump_game(nums):
    if len(nums) == 0:
        return False
    if nums[0] == 0 and len(nums) !=1:
        return False
    if nums[0] == 0 and len(nums) == 1:
        return True
    dp = nums.copy()
    for i in range(1, len(nums)):
        dp[i] = max(i + nums[i], dp[i - 1])
        if dp[i] <= i:
            if i < len(nums) - 1:
                return False
            else:
                return True
    return True

res = jump_game(data)
print(res)