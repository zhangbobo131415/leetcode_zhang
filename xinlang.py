# a = '1,2,3,4,5'
# a= a.split(',')
# b = [int(i) for i in a]
# b.sort()
# nums_dict = {}
# for num in b:
#     if num not in nums_dict:
#         nums_dict[num] = 1
#     else:
#         nums_dict[num] += 1
# tem = list(nums_dict.keys())
# sum_step = 0

# for index in range(len(tem) - 1):
#     if nums_dict[tem[index]] <= (tem[index + 1] -tem[index]) and nums_dict[b[index]]!=1:
#         sum_step +=  sum(range(1,nums_dict[b[index]]))
#     else:
#         pass
# print(sum_step)
# print(tem)


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    print('-------------------')
    while True:
        new_num = yield average
        print("=============")
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    a = next(calc_average)  # 预激下生成器s
    print(a,"=a")
    print('begin')
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    n=int(input())
    have_sized = [int(j) for j in input().split()]
    have_all = sum(have_sized)
    size = [int(j) for j in input().split()]
    lianhe = [i for i in zip(have_sized, size)]
    lianhe.sort(key=lambda x: x[1], reverse=True)
    sum_lianhe = 0
    for i, num in enumerate(lianhe):
        sum_lianhe += num[1]
        if sum_lianhe >= have_all:
            break
    cost = 0
    last = []
    for j in lianhe:
        if num[1] == lianhe[j][1]:
            last.append(j)
    index = 0
    for k in range(len(have_sized)):
        if lianhe[k][1] >= num[1]:   
            cost += lianhe[k][0]
        else:
            index += 1
    last.sort(reverse=True)

    print(i+1,cost+sum(last[index:][0]))

    