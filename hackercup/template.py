
with open('.txt') as f:
    n = int(f.readline())
    lines = [int(x.strip()) for x in f.readlines()]
out = []

for l in lines:
    c = 1
    o = 'Case #{}: {}'.format(c, len(o))
    out.append(o)
    print(o)
    c += 1

with open('output.txt', 'w+') as f:
    for o in out:
        f.write(o + '\n')