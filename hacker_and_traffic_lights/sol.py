n, k = map(int, raw_input().split())
q = raw_input().split()

tq = []
x = min(n, k - 1)

for _ in range(0, min(n, x + 1)):
    tq.append(q.pop(0))

def change_sig(s):
    if s == 'R':
        return 'Y'
    elif s == 'Y':
        return 'G'
    else:
        return 'R'

changes = 0

while len(tq) > 0:
    while tq[0] != 'G':
        #print tq, q
        changes += 1
        for i in range(0, len(tq)):
            tq[i] = change_sig(tq[i])
    tq.pop(0)
    if len(q) != 0:
        tq.append(q.pop(0))

print changes

