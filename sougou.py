# n, m = (int(i) for i in input().split())
# # data = [[0, 0] for i in range(m)]
# code = [0 for i in range(n)]   
# for i in range(m):
#     l, r = (int(i) for i in input().split())
#     for j in range(l, r + 1):
#         code[j] = i + 1
# res = 0
# for i in range(n):
#     res += i * code[i]
# print(res%100000009)



# def eqa(s, p):
#     if s == '*' or p == '*':
#         return True

# def(s):
#     s = s.split()
#     for i in range(4)
#     if s[i]

# n, m = (int(i) for i in input().split())
# guize = []
# for i in range(n):
#     p = input()
#     if p.startwith('*'):
#         tem = ['*', '*', '*', '*']
#         p = p.split()
#         for i in range(len(p)):
#             tem[3 - i] = p[i]
#         guize.append(tem.copy())
#     elif i.endswith('*'):
#         tem = ['*', '*', '*', '*']
#         p = p.split()
#         for i in range(len(p)):
#             tem[i] = p[i]
#         guize.append(tem.copy())
#     else:
#         guize.append(i.split('.'))



# def countPrimes(n: int) -> int:
#     res =[]
#     if n < 2: return 0
#     isPrimes = [1] * n
#     isPrimes[0] = isPrimes[1] = 0
#     for i in range(2, int(n ** 0.5) + 1):
#         if isPrimes[i] == 1:
#             isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
#     for i in range(n):
#         if isPrimes[i] == 1:
#             res.append(i)
#     return res
# res = countPrimes(500000)

# print(len(res))


# test = []
# for i in range(3):
#     def testst(x): print(x + i)
#     test.append(testst)
# for num in test:
#     num(2)
def jisuan_v(tem_data, cishu):
    if len(tem_data) == 1:
        return tem_data[0]
    for i in range(len(tem_data) // 2):  
        p, q = tem_data[0], tem_data[1]
        tem_data.pop(0)
        tem_data.pop(0)
        if cishu & 1 == 1:
            tem_data.append(p | q)
        else:
            tem_data.append(p ^ q)
    return jisuan_v(tem_data,cishu+1)

# res = jisuan_v([4,2,3,4],1)

n, m = (int(i) for i in input().split())
data = [int(i) for i in input().split()]
res=[]
for j in range(m):
    a, b = (int(i) for i in input().split())
    data[a-1] = b
    tem_data = data.copy()
    res.append(jisuan_v(tem_data, 1))

for i in res:
    print(i)

# a = jisuan_v([1, 2, 3, 4], 1)
# print(a)
    




