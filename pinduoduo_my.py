import sys
class solution:
    def __init__(self):
        self.min_step = sys.maxsize
    def rescurve(self, x: int, y: int, count:int):
        if x == y:
            if self.min_step > count:
                self.min_step = count
            return
        if x > y:
            return
        self.rescurve(2 * x, y, count + 1)
        self.rescurve(10 * x + 1, y, count + 1)

t = int(input())

res = []
test = solution()
for i in range(t):
    a, b = [int(i) for i in input().split()]
    if a==0 and b>=0:
        res.append(b)
        continue
    if b == 0 and a != 0:
        res.append(-1)
        continue
    if a * b < 0:
        res.append(-1)
        continue
    a = 
    test.rescurve(a, b, 0)
    if test.min_step == sys.maxsize:
        res.append(-1)
    else:
        res.append(test.min_step)
    test.min_step = sys.maxsize
for i in res:
    print(i)    



# data = input()
# stack = []
# tmp={')':'(',']':'['}
# if len(data) == 0:
#     print(0)

# for index, i in enumerate(data):
#     if len(stack) == 0 or i not in tmp :
#         stack.append(i)
#     else:
#         stack.pop(-1)
# print(len(data) - len(stack))
        

# def max_m(s):
#     if not s:
#         return 0
#     res =0
#     stack=[-1]
#     for i in range(len(s)):
#         if s[i] in "([":
#             stack.append(i)
#         elif s[i] == ']' and s[stack[-1]] == '[':
#             stack.pop(-1)
#             res = max(res, i -stack[-1])
#         elif s[i] == ')' and s[stack[-1]] == '(':
#             stack.pop(-1)
#             res = max(res, i - stack[-1])
#         else:
#             stack.append(i)
#     return res
# a = input()
# print(max_m(a))   

def fib(n):
    a = 0.02
    b = 0.02
    
    for i in range(1, n + 1):
        a, b = b, a + b
    return b

print(fib(48))
    