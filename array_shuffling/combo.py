a = raw_input().split()

l = len(a)
def combo(a, cmb, l):
    if l == 0:
        print cmb
        return

    for e in a:
        if not e in cmb:
            cmb.append(e)
            combo(a, cmb, l - 1)
            cmb.pop(-1)

combo(a, [], l)
