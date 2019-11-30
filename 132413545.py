# from collections import defaultdict
n = int(input())
nums = list(map(int,input().split()))
# dic1 = defaultdict(list)
dic1 = {}
for i in range(1,n+1):
    dic1[i] = [i]
f = 1
count = 0
while f:
    count +=1
    # dic2 = defaultdict(list)
    dic2 = {}
    for i in range(1,n+1):
        # 
        l = dic1.get(i,[])
        if nums[i-1] in l:
            f = 0
            break
        # dic2[nums[i-1]].extend(dic1[i])
        dic2[nums[i-1]]=l
    dic1 = dic2
print(count)