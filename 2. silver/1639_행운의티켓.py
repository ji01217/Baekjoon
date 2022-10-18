S = list(map(int, input()))

if len(S) % 2 == 0:
    nn = len(S)
else:
    nn = len(S) - 1

ans = 0

while nn > 0 and ans == 0:
    for i in range(len(S)-nn+1):
        mid = nn//2
        if sum(S[i:i+mid]) == sum(S[i+mid:(i+nn)]):
            ans = nn
            break
    nn -= 2

print(ans)