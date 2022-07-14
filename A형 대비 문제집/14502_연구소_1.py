global ans
now = start
visited = [[0] * M for _ in range(N)]
while q and now > 0:
    i, j = q.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            now -= 1
            if now == 0:
                break
            q.append((ni, nj))
if ans < now:
    ans = now