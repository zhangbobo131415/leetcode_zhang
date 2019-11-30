n, s = (int(i) for i in input().split())
data = [int(i) for i in input().split()]
sum_sub = 0
i = 0
j = 0
lenth = 0
max_lenth = 0
for index, num in enumerate(data):
    sum_sub += num
    j += 1
    lenth += 1
    max_lenth=max(lenth,max_lenth)
    
    if sum_sub > s:
        while sum_sub>s:
            sum_sub -= data[i]
            i += 1
            lenth -= 1
        max_lenth=max(lenth,max_lenth)
    else:
        pass
print(max_lenth -1)

        