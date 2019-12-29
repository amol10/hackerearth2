n, k = map(int, raw_input().split())
q = raw_input().split()

tq = []
x = min(n, k - 1)

if x < 20:
    for _ in range(0, min(n, x + 1)):
        tq.append(q.pop(0))
else:
    tq = q[0 : x]
    q = q[x:]

d = { 'R' : 'Y', 'Y' : 'G', 'G' : 'R'}    

def change_sig(s, c):
    o = s
    while c > 0:
        o = d[o]
        c -= 1
    return o


changes = 0

for s in tq:
    t = change_sig(s, changes % 3)

    if t == 'G':
        continue
    elif t == 'R':
        changes += 2
    else:
        changes += 1

print changes

