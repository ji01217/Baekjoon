W, H = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cuts = [[0], [0]]
for n in range(N):
    cuts[arr[n][0]].append(arr[n][1])

cuts[0].sort()
cuts[1].sort()
cuts[0].append(H)
cuts[1].append(W)

max_W = 0
max_H = 0

for i in range(1, len(cuts[0])):
    h = cuts[0][i] - cuts[0][i-1]
    if max_H < h:
        max_H = h
for i in range(1, len(cuts[1])):
    w = cuts[1][i] - cuts[1][i-1]
    if max_W < w:
        max_W = w

print(max_H * max_W)