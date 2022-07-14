N = int(input())
lst = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-2, -1, -1):
    while lst[i + 1] <= lst[i]:
        lst[i] -= 1
        cnt += 1
print(cnt)