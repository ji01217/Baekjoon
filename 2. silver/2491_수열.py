# dp 미적용
# 입력
N = int(input())
lst = list(map(int, input().split()))

# 풀이
cnt = 1
ans = 1
for i in range(1, N):
    if lst[i] <= lst[i - 1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt
cnt = 1
for i in range(1, N):
    if lst[i] >= lst[i - 1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

# 출력
print(ans)

# dp 적용
# 입력
N = int(input())
lst = list(map(int, input().split()))

# 풀이
dp1, dp2 = [1] * N, [1] * N
for i in range(1, N):
    if lst[i] <= lst[i - 1]:
        dp1[i] = max(dp1[i], dp1[i - 1] + 1)
    if lst[i] >= lst[i - 1]:
        dp2[i] = max(dp2[i], dp2[i - 1] + 1)

#출력
print(max(max(dp1), max(dp2)))
