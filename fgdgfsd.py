target = int(input())
def combinationSum(target):  
    candidates = [i+1 for i in range(target)]
    res = []
    tem = []
    candidates.sort()
    backtrack(candidates, target, 0, tem, res, 0)
    return res
def backtrack(candidates, target, start_index, tem, res, sum_):
    if sum_ == target:
        res.append(tem.copy())
        return
    for i in range(start_index, len(candidates)):
        tem.append(candidates[i])
        # 剪枝加速运算
        if sum_ + candidates[i] > target:
            tem.pop(-1)
            break
        # 在解空间搜索的时候可以只遍历子节点大于等于父节点的节点这样可以有效消除重复解
        # 例如在本例中，5为父节点时，子节点只能为5、7。3为父节点时，子节点只能是3、5、7
        # 这样可以去重
        backtrack(candidates, target, i, tem, res, sum_ + candidates[i])
        tem.pop(-1)
    return

a = combinationSum(target)
for i in a:
    for index, num in enumerate(i):
        if index == 0:
            print(i[index],end='')
        else:
            print('+', i[index],end='',sep='')        
    print('')
            