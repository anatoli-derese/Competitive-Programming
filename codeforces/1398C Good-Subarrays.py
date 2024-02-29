from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, list(input())))
    acc = 0
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    for i, num in enumerate(arr):
        acc += num         
        d[acc-1-i] +=1
        ans += d[acc-1-i] -1
    print(ans)


    