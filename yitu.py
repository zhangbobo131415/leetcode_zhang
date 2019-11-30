# import numpy as np
# n, m = (int(i) for i in input().split())
# # data = [[int(i) for i in input().split()] for k in range(m)]
# # data_b = [[int(i) for i in input().split()] for k in range(m)]
# data = [[2,2],[2,2]]
# data_b = [[2,2],[2,2]]
# a = np.array(data)
# b = np.array(data_b)
# c = np.dot(np.dot(a.T, b), np.dot(b.T, a))
# res = c.T.tolist()
# print(c)



# num = int(input())
# tem = 0
# res = []
# dianji = []
# for i in range(num):
#     n, m = (int(i) for i in input().split())
#     data = [int(i) for i in input().split()]
#     dianji.append(data.copy())
#     rs = dict(zip(data,[0 for i in range(n)]))
#     for k in range(m):
#         left, right = (int(i) for i in input().split())
#         for point in rs.keys():
#             if left <= point <= right:
#                 rs[point] += 1
#     res.append(rs.copy())

# for i in range(num):
#     print("Case #{}:".format(i+1))
#     for m in dianji[i]:
#         print(res[i][m])

def dot(a, b):
    c=[[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] =c[i][j] %1009
    return c
def zhuanzhi(a):
    b = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]
    return b
# print(dot(data,zhuanzhi(data)))
# print(zhuanzhi(data))




# n, m = (int(i) for i in input().split())
# data_a = [[int(i) for i in input().split()] for k in range(m)]
# data_b = [[int(i) for i in input().split()] for k in range(m)]
# res = dot(dot(zhuanzhi(data_a), data_b), zhuanzhi(data_b))
# res = zhuanzhi(res)
# print(n, m)
res = [[2,2],[2,2]]
for i in res:
    for j in i:
        print(j, end=' ')
    print('\n', end='')



