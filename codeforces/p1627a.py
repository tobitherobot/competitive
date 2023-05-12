t = int(input())
for ts in range(t):
    n, m, r, c = map(int, input().split())
    isblack = False
    almostblack = False
    hasblack = False
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j]=='B':
                hasblack = True
                if i+1==r or j+1==c:
                    almostblack = True
                    if i+1==r and j+1==c:
                        isblack = True
    if isblack:
        print(0)
    elif almostblack:
        print(1)
    elif hasblack:
        print(2)
    else:
        print(-1)