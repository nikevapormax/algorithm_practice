natural_num = set(range(1, 10001))
not_self = set()

for i in natural_num:
    for j in str(i):
        i += int(j)
    not_self.add(i)

for i in sorted(natural_num - not_self):
    print(i)
