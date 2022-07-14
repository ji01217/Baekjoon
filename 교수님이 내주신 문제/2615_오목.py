def omok():
    di = [0, 1, 1, -1]
    dj = [1, 0, 1, 1]
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                stone = arr[i][j]

                for k in range(4):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]

                    while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == stone:
                        cnt += 1

                        if cnt == 5:
                            # 앞이나 뒤에 같은 색 돌이 있는지 확인
                            if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19 and arr[i - di[k]][j - dj[k]] == stone:
                                break
                            if 0 <= ni + di[k] < 19 and 0 <= nj + dj[k] < 19 and arr[ni + di[k]][nj + dj[k]] == stone:
                                break
                            return [stone, i + 1, j + 1]

                        ni += di[k]
                        nj += dj[k]
    return 0


arr = [list(map(int, input().split())) for _ in range(19)]

ans = omok()

if ans == 0:
    print(0)
else:
    print(ans[0])
    print(ans[1], ans[2])