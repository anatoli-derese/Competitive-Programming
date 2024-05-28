# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n =  int(input())
lst = list(map(int,input().split()))
ans = 1
left = 0
for right in range(1,n):
    if lst[right] <= lst[right-1]:
        left = right
    wind = right- left +1
    ans = max(wind, ans)
print(ans)