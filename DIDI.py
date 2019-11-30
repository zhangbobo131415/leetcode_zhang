# n, m = (int(i) for i in input().split())
# data = []
# res = [1 for i in range(n)]
# for j in range(m):
#     data.append([int(i) for i in input().split()])
#     res[data[-1][0]] = 0
#     res[data[-1][1]] = 0
    

# a = {}
# b = {}
# for index,j in enumerate(data):
#     if j[1] not in a:
#         a[j[0]] = 0
#         res[j[0]] = 0
        
#     if j[0] not in b:
#         b[j[1]] = 0
#         res[j[1]] = 0

# len_a = len(a)
# len_b = len(b)
# if abs(len_a - len_b) <= sum(res):
#     print(n // 2)
# else:
#     print(min(len_a,len_b)+sum(res))



# n, m = (int(i) for i in input().split())
# data = (int(i) for i in input().split())
# dp = data.copy()
# length = [1 for i in range(n)]
# for j in range(1, m):
#     dp[]
# for i in range(1, len(data)):
#     if dp[i - 1] + data[i] < data[i]:
#         dp[i] = dp[i - 1] + data[i]
#         length[i] = length[i - 1] + 1
#     else:
#         dp[i] = data[i]
#         length[i] = 1
# print(min(dp))

n, m = (int(i) for i in input().split())
data = [int(i) for i in input().split()]
dp = data.copy()
for i in range(n):
    if i == 0:
        dp[i] = data[i]
    else:
        dp[i] = dp[i - 1] + data[i]
front = 0
ans = dp[m - 1]
for i in range(n):
    front +=data[i]
    if i > m - 1:
        min_ = dp[i]
        for j in range(i):
            if i - j >= m:    
                min_ = min(min_, dp[i] - dp[j])
        ans = min(ans, min_)
print(ans)
            


