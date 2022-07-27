word = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for cro in croatia:
    if cro in word:
        word = word.replace(cro, "B")

print(len(word))
