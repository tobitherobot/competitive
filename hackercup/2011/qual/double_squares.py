
with open('2011/qual/double_squares_input.txt') as f:
    n = int(f.readline())
    lines = [int(x.strip()) for x in f.readlines()]
out = []

sq = []
lim = 2147483647
x = 0
while x*x <= lim:
    sq.append(x*x)
    x += 1
c = 1

for l in lines:
    sm = 0
    for s in sq:
        if 2*s > l:
            break
        elif l-s in sq:
            sm += 1
    o = 'Case #{}: {}'.format(c, sm)
    out.append(o)
    print(o)
    c += 1

with open('output.txt', 'w+') as f:
    for o in out:
        f.write(o + '\n')