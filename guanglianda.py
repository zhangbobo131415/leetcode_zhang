# peopele = [3,2,2,1]
# limit = 5
peopele = [int(i) for i in input().split()]
limit = int(input())
peopele.sort()
i = 0
j = len(peopele) - 1
res = 0
visited = [0] * len(peopele)
for i in range(len(peopele)):
    if visited[i] == 0:
        j = len(peopele) - 1    
        while i < j:
            if visited[j] == 0 and visited[j] == 0:
                if peopele[i] + peopele[j] > limit:#若不能乘坐，则寻找下一个体重较轻的
                    j -= 1
                elif peopele[i] + peopele[j] <= limit:  #两人可以乘坐一条船则总船数加一，
                                                        #同时标记i，j为已访问过，同时结束本次循环
                    res += 1
                    visited[i] = visited[j] = 1
                    break
            else:
                j -= 1
res += len(peopele) - sum(visited) #剩下的人每人一条船，最后相加
print(res)
                
        
        
    