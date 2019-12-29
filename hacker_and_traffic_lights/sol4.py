n, k = map(int, raw_input().split())
q = raw_input().split()

cq = []
x = min(n, k - 1)

d = { 'R' : 'Y', 'Y' : 'G', 'G' : 'R'}    
d2 = { 'R' : 2, 'Y' : 1, 'G' : 0}    

def change_sig(s, c):
    o = s
    while c > 0:
        o = d[o]
        c -= 1
    return o

tch = 0
wch = 0

for i in range(0, len(q)):
    s = q[i]
    s = change_sig(s, wch % 3)
    c = d2[s]
    cq.append(c)
    wch += c
    
    if len(cq) > x:
        a = cq.pop(0)
        tch += a
        wch -= a

print tch + wch
    
