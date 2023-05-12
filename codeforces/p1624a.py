t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split(' ')]
    a.sort()
    print(a[-1]-a[0])