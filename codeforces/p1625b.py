t = int(input())
for ts in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    last = {}
    mn = n

    for i in range(n):
        if a[i] in last and i-last[a[i]] < mn:
            mn = i-last[a[i]]
            if mn == 1:
                break
        last[a[i]] = i
    
    if mn == n:
        print(-1)
    else:
        print(n-mn)