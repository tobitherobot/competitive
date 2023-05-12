t = int(input())
for ts in range(t):
    a, b, c = map(int, input().split())
    d1 = b-a
    d2 = c-b
    d3 = (c-a) // 2
    if d1==d2 or (b+d1)%c==0 and c<(b+d1) or (b-d2)%a==0 and a<(b-d2) or (a+d3)%b==0 and b<(a+d3) and (c-a)%2==0:
        print('YES')
    else:
        print('NO')