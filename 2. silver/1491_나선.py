# 입력
N, M = map(int, input().split())

# 풀이
arr = [[0] * N for _ in range(M)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
ci, cj = 0, 0
dis = 0
cnt = 1

while True:
    if cnt == N * M:
        break

    arr[ci][cj] = 1
    ni, nj = ci+di[dis], cj+dj[dis]

    if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
        ci, cj = ni, nj
        cnt += 1

    else:
        dis = (dis+1) % 4

# 출력
print(nj, ni)