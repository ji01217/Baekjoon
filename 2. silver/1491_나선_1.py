def solve_1941(n, m):
    arr = [[0] * n for _ in range(m)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    ci, cj = 0, 0
    cnt = 1
    dis = 0

    while True:
        if cnt == n * m:
            print(ci, cj)
            break

        arr[ci][cj] = 1
        ni, nj = ci + dx[dis], cj + dy[dis]

        if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 0:
            ci, cj = ni, nj
            cnt += 1

        else:
            dis  = (dis + 1) % 4


n, m = map(int, input().split())
solve_1941(n, m)