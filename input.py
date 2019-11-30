# a = [(1, 3), (2, 2), (3, 1), (3, 1)]
# #max函数会将里面的每一项即(1, 3), (2, 2), (3, 1), (3, 1)按照字典序排列
# # 因此最大的自然就是(3, 1)!!!!!!!!!!!!!
# for i in a:
#     print(i)
# print(max(a))
# nums = input()
# tem = []
# for i in range(nums):
#     a, b = input()
#     tem.append([int(a), int(b)])
nums = 4
tem = [[1,1],[1,3],[2,2],[3,2]]
tem.sort()
res = []
start_index = 0
def jian(d_i,d_j):
    return d_i[0] - d_j[0], d_i[1] - d_j[1]
    
count = 0
for i in range(nums):
    count = 0
    for j in range(nums):
        if j !=i:
            cha_a, cha_b = jian(tem[j], tem[i])
            if cha_a < 0 or cha_b < 0:
                count += 1
    res.append(count)

for i in range(nums):
    tem[i].append(res[i])
tem.sort(key=lambda x: x[2])
start = tem[0]
count = 1
print(tem)
tem_dic= {}
for i in tem:
    if i[2] not in tem_dic:
        tem_dic[i[2]] = [i]
    else:
        tem_dic[i[2]].append(i)
tem = [i for i in tem_dic.keys()]
tem.sort()
count = 0 
def suanhu(cengshu, tem, start):
    count = 0 
    if cengshu == len(tem):
        return -1
    for content in tem_dic[tem[cengshu]]:
        if content[0] >= start[0] and content[1] >= start[1]:
            start = content
            count = max(suanhu(cengshu + 1, tem, start) + 1, count)
    return count
print(suanhu(0, tem, (0,0)))

    
# for i in range(1, nums):
#     if tem[i][0] >= start[0] and tem[i][1] >= start[1]:
#         count += 1
#         start = tem[i]

print(count)



    



        

