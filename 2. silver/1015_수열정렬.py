# 입력
N = int(input())
A = list(map(int, input().split()))

# 풀이
A_sort = sorted(A)
ans = [0 for _ in range(N)]
for i in range(N):
    idx = A.index(A_sort[i])
    ans[idx] = i
    A[idx] = -1

# 출력
print(*ans)