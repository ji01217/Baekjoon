# BFS 조합 문제
from collections import deque


def wall(cnt):
    if cnt == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0



def BFS():
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


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = start = 0
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            start += 1
        if arr[i][j] == 2:
            q.append((i, j))
start -= 3  # 새로 설치한 벽 제외
wall(0)
print(ans)
