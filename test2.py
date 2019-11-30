nums = [int(i) for i in input().split()]
if len(nums) <= 2:
    print('Yes')
else:
    length = len(nums)
    zonghe = sum(nums)
    xiaoming = 0
    daming = 0
    i = 1
    while len(nums) > 0:
        if len(nums) == 1:
            if i&1==1:
                xiaoming += nums[0]
            else:
                daming += nums[0]
            break
        if max(nums[1], nums[-1]) < max(nums[0], nums[-2]):
            if i&1==1:
                xiaoming += nums[0]
            else:
                daming += nums[0]
            nums.pop(0)
        elif max(nums[1], nums[-1]) > max(nums[0], nums[-2]):
            if i&1==1:
                xiaoming += nums[-1]
            else:
                daming += nums[-1]
            nums.pop(-1)
        else:
            if nums[-1] > nums[0]:
                index = -1
            else:
                index = 0
            if i&1==1:
                xiaoming += nums[index]
            else:
                daming += nums[index]
            nums.pop(0)

        i += 1
    if xiaoming >= daming:
        print('Yes')
    else:
        print('No')     
            