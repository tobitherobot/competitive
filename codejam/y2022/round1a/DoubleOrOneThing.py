# unsolved

def solve():
    s = input()
    n = ""

    for i in range(len(s) - 1):
        n += s[i]
        if ord(s[i]) <= ord(s[i+1]):
            n += s[i]
    n += s[-1]

    return n    

t = int(input())
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve()))

"""

aab = aaaab
bba = bba

"""