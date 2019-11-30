
n, m = (int(i) for i in input().split())
data = [int(i) for i in input().split()]

# n,m=10, 6
# data=[6, 4, 2, 10, 3, 8, 5, 9, 4, 1]
import sys
    
pingjun_m = sum(data[0:m])

pingjun_list = [-sys.maxsize for i in range(n)]
pingjun_list[0] = pingjun_m
length = m

for i in range(1, n - m + 1):
    length += 1

    #pingjun_m = pingjun_m + data[m + i - 1] - data[i - 1]
    pingjun_m = pingjun_m + data[m + i - 1]
    tem = pingjun_m/length
    while length > m:
        pingjun_m = pingjun_m - data[i - length]
        if :

        

    if pingjun_m / m > pingjun_m + data[i - 1] / (length + 1):
        length = m
        pingjun_list[i] = pingjun_m
    else:
        length += 1 
        pingjun_list[i] = pingjun_m + data[i - 1]

print(format(max(pingjun_list)/m,'.3f'))

# n = int(input())
# data = [[0, 0] for i in range(n)]
# for i in range(n):
#     data[i][0], data[i][1] = (int(i) for i in input().split())
# data.sort(key=lambda x: x[0] + x[1], reverse=True)
# l_sum = 0
# v0 = 0

# for a_and_t in data:
#     l_sum += v0 * a_and_t[1] + 0.5 * a_and_t[0] * a_and_t[1]** 2
#     v0 += a_and_t[0] * a_and_t[1]
# print(format(l_sum,'.1f'))


# n = int(input())
# n1 = n
# mm = []
# tsum = 0
# while n1>0:
#     m = list(map(int,input().split()))
#     tsum +=m[1]
#     mm.append(m)
#     n1 -=1
# mm.sort(key=lambda x: x[0], reverse=True)
# v = 0
# res = 0
# for i in range(n):
#     res +=v*mm[i][1]
#     res +=0.5*mm[i][0]*mm[i][1]*mm[i][1]
#     v +=mm[i][0]*mm[i][1]
# print('%.1f'%(res))
    
