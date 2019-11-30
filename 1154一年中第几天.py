#%%
# 一年中的第几天
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(i) for i in date.split('-')]
        month_days = [0] * 13
        for i in range(13):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                month_days[i] = 31
            else:
                month_days[i] = 30
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_days[2] = 29
        else:
            month_days[2] = 28
        toal_day = 0
        print(month_days)
        
        for i in range(1, month):
            toal_day += month_days[i]        
        toal_day += day
        return toal_day
test = Solution()
a = test.dayOfYear('2018-5-3')
print(a)
#%%
from functools import cmp_to_key