import sys
m = 3
n = 3
max_num = sys.maxsize

test = [[1, 3, 4], [2, 1, 2], [4, 3, 1]]
dp = [[max_num for i in range(n)] for j in range(m)]
dp[0][0] = test[0][0]

def legal(i, j, m, n):
    if 0 <= i <= m - 1 and 0 <= j <= n - 1:
        return True
    else:
        return False


def daixuanze(i, j, dp):
    res = []
    if legal(i + 1, j,m,n):
        res.append(dp[i + 1][j])
    if legal(i - 1, j,m,n):
        res.append(dp[i-1][j])
    if legal(i, j+1,m,n):
        res.append(dp[i][j+1])
    if legal(i, j-1,m,n):
        res.append(dp[i] [j- 1])
    return res


for i in range(m):
    for j in range(n):
        if i != 0 or j != 0:
            dp[i][j] = min(daixuanze(i, j, dp)) + test[i][j]
print(dp)
print(dp[m-1][n-1])

# data = [3, 6, 3, 5, 6, 4, 3, 2]
# dp_l = data.copy()
# dp_r = data.copy()
# dp_l[0] = 1
# dp_r[-1] = 1

# for i in range(1, len(data)):
#     if data[i] > data[i - 1]:
#         dp_l[i] = dp_l[i - 1] + 1
#     else:
#         dp_l[i] = 1
# print(dp_l)
# for i in range(len(data) - 2, -1, -1):
#     if data[i] > data[i + 1]:
#         dp_r[i] = dp_r[i + 1]+1
#     else:
#         dp_r[i] = 1
# print(dp_r)
# res = []
# for i in range(0, len(data)):
#     res.append(max(dp_l[i], dp_r[i]))
# print(res)
