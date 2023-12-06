class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7 # get the numbers of mondays
        remDays = n % 7 # get the numbers of days that don't fufill a week
        days = 0
        for i in range(weeks):
            days += sum(range(i+1, i+7+1)) 
        x = sum(range(weeks+1,weeks+remDays+1))
        days += sum(range(weeks+1, weeks + 1 + remDays))
        return days