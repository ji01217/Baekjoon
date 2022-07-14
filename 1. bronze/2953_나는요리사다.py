arr = [list(map(int, input().split())) for _ in range(5)]
ans = [0, 0]
for i in range(5):
    ssum = 0
    for j in range(4):
        ssum += arr[i][j]
    if ans[1] < ssum:
        ans = [i + 1, ssum]
print(*ans)