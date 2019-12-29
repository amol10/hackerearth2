n = int(raw_input())

a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = map(int, raw_input().split())

combos = []
c3 = []

def combo(arr, cmb, l, cb):
    if l == 0:
        print cmb
        #c3.append(cmb[:])
        cb(cmb)
        return

    for e in arr:
        if not e in cmb:
            cmb.append(e)
            combo(arr, cmb, l - 1, cb)
            cmb.pop(-1)

def cb1(cmb):
    c3.append(cmb[:])

for i in range(0, n):
    combo([a[i], b[i], c[i]], [], 3, cb1)
    combos.append(c3[:])
    del(c3)
    c3 = []

print combos

def cb2(cmb):
    print cmb

combo(combos, [], n, cb2)
