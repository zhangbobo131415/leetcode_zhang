# n = int(input())
# data = [int(i) for i in input().split()]
# dp = [0] * n
# ans = 0
# for index, i in enumerate(data):
#     dp[index] = data[index]
#     for j in range(index - 1, -1, -1):
#         if data[index] > data[j]:
#             dp[index] = max(dp[index], dp[j] + data[index])
#     ans = max(ans, dp[index])
# print(ans)

data = input()
#data = 'AACTGTGCACGACCTGA'

sub_len = int(input())

if len(data) <= sub_len:
    print(data)
else:
    sub_count = 0
    ratio = 0
    start = 0
    
    for index, c in enumerate(data):
        if c == 'C' or c == 'G':
            sub_count += 1
            
        if index >= sub_len - 1:
            
            if (sub_count / sub_len) > ratio:
                ratio = sub_count / sub_len
                start =index - sub_len + 1
            
            if data[index - sub_len + 1] == 'C' or data[index - sub_len + 1] == 'G':
                sub_count -= 1
            
    print(data[start:start+sub_len])



        

    
                
            


