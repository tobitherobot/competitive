# solved

def solve():
    n = int(input())
    lst = [int(s) for s in input().split(" ")]
    lst.sort()
    
    ct = 0
    for i in range(n):
        if ct+1 <= lst[i]:
            ct += 1
    return ct

t = int(input())
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve()))