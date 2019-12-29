s = []
for c in raw_input():
    s.append(int(c))

ec = 0
for i in s:
    if i % 2 == 0:
        ec += 1

for i in s:
    print ec,
    if i % 2 == 0:
        ec -= 1

