import sys
from functools import cmp_to_key
# n, m = (int(i) for i in input().split())
# data = [[int(i) for i in input().split()] for i in range(m)]
def copare(x, y):
    a = x[0] * x[1]
    b = y[0] * y[1]
    s = (x[0] + y[0]) / 2 * min(x[1], y[1])
    if a <s:
        return -1
    elif  a==s:
        return 0
    else:
        return 1
test = [[2, 2], [3, 7]]
test.sort(key=cmp_to_key(copare))
print(test)
def my_dfs():
  


