n, k = map(int, raw_input().split())
#def mapRYG(s):
#    d = { 'R'
q = raw_input().split()

tq = []
x = min(n, k - 1)

'''
if x < 20:
    for _ in range(0, min(n, x + 1)):
        tq.append(q.pop(0))
else:
    tq = q[0 : x]
    q = q[x:]
    '''

d = { 'R' : 'Y', 'Y' : 'G', 'G' : 'R'}    
d2 = { 'R' : 2, 'Y' : 1, 'G' : 0}    

def change_sig(s, c):
    o = s
    while c > 0:
        o = d[o]
        c -= 1
    return o


changes = 0

'''while len(tq) > 0:
    while tq[0] != 'G':
        print len(tq)
        changes += 1
        for i in range(0, len(tq)):
            tq[i] = d[tq[i]]
    tq.pop(0)
    if len(q) != 0:
        tq.append(q.pop(0))'''


#while len(tq) > 0:
a = 0
for i in range(0, len(q)):
    if i >= x:
        ch = d2[q[i - x]]
        q[i-x+1] = change_sig(q[i-x+1], (a+ch)%3)
        print ch
        changes -= ch
        a += ch

    s = q[i]
    t = change_sig(s, changes % 3)

    if t == 'G':
        continue
    elif t == 'R':
        changes += 2
    else:
        changes += 1

    '''tq.pop(0)
    if len(q) != 0:
        tq.append(q.pop())'''


print changes + a

