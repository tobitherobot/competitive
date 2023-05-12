t = int(input())
for ts in range(t):
    n, l = map(int, input().strip().split(' '))
    xs = [int(y) for y in input().strip().split(' ')]

    m = [0]*l
    for x in xs:
        s = bin(x)[::-1]
        for i in range(l):
            if len(s)-2<=i:
                m[i] -= 1
            elif s[i]=='1':
                m[i] += 1
            else:
                m[i] -= 1
    tmp = ''
    for x in m:
        if x<=0:
            tmp += '0'
        else:
            tmp += '1'
    res = int(tmp[::-1], 2)
    print(res)