
n = input()
n = int(n)
nums = [int(i) for i in input().split()]
sumsum = 0
for i in range(n):
    tem = [0 for k in range(n)]
    tem[i]=nums[i]
    for j in range(i+1,n):
        if i < j:
            tem[j] = max(tem[j - 1], nums[j]) 
    sumsum += sum(tem)
print(sumsum)         
