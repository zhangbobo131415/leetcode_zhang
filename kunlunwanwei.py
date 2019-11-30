# n = int(input())
# data = [int(i) for i in input().split()]
# res = sum(data) - n*(n-1)//2
# print(res)

n = int(input())
data = [[0 for i in range(n)] for j in range(n)]
viseted = [0 for i in range(n)]
m, n = 0, 0
stack=[]

while True:
    try:
        a = input()
        if a == '':
            break
    except EOFError:
        break
    m, n = [int(i) for i in a.split()]
    data[m][n] = 1
def neibor(data, viseted, point):
    res =[]
    for index,j in enumerate(data[point]):
        if j == 1:
            res.append(index)
    return res
 
def dfs(data, viseted, start,stack):
    neibor_start = neibor(data, viseted, start)
    zuihou =False
    #print(neibor_start)
    for j in neibor_start:
        if j in stack:
            return True
        if data[start][j] == 1:
            stack.append(j)
            viseted[j] = 1
            zuihou = dfs(data, viseted, j, stack)
            stack.pop(-1)
            viseted[j] = 0
    return zuihou
stack.append(m)
viseted[m]=1
# print(m)
print(dfs(data, viseted, m,stack))




# def dfs(v):
#     vis[v] = -1
#     flag = 0
#     for i in range(n):
#         if a[v][i] != 0 and vis[i] != -1:
#             dfs(i)
#             vis[i] = 1
#         else:
#             pass
#         if a[v][i] != 0 and vis[i] == -1:
#             print(True)
#             global swi
#             swi = True
#             exit()
#             return
#         else:
#             pass
#     return False
# global swi
# swi = False
# n = int(input())
# if n <=1:
#     print(False)
# else:
#     m = []
#     while True:
#         try:
#             a = list(map(int,input().split()))
#             if a:
#                 m.append(a)
#         except EOFError:
#             break
#     c = len(m)
#     a = [([0] * n) for i in range(n)]
#     vis = [0] * (n)
#     for i in range(c):
#         s, t = m[i][0:2]
#         s = int(s)
#         t = int(t)
#         a[s][t] = 1
#     dfs(0)
#     if not swi:
#         print(False)
#     else:
#         print(True)





            
            
            



    
    

    
    
