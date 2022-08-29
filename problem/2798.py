n, m = map(int, input().split())
cards = [card for card in map(int, input().split())]
result = []


for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] <= m:
                result.append(cards[i] + cards[j] + cards[k])
            else:
                continue

print(max(result))
