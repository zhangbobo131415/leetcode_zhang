
n, m = (int(i) for i in input().split())
data = [int(i) for i in input().split()]
data.sort()
min_he = 0
for i in range(m):
    min_he += data[i] * data[2 * m - 1 - i]
print(min_he)


    