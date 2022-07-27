word = input().lower()

alphabet = [0] * 28

for w in word:
    alphabet[ord(w) - ord("a")] += 1

if alphabet.count(max(alphabet)) > 1:
    print("?")
else:
    print(chr(97+alphabet.index(max(alphabet))).upper())
