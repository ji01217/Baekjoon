def bingo(i, j):
    global line, ans
    for k in range(5):
        if mc[i][j] in arr[k]:
            for l in range(5):
                if mc[i][j] == arr[k][l]:
                    arr[k][l] = 0
                    if k == l:
                        if arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == 0 and arr[3][3] == 0 and arr[4][4] == 0:
                            line += 1
                    if k + l == 4:
                        if arr[4][0] == 0 and arr[3][1] == 0 and arr[2][2] == 0 and arr[1][3] == 0 and arr[0][4] == 0:
                            line += 1
                    if arr[k] == [0, 0, 0, 0, 0]:
                        line += 1
                    if arr[0][l] == 0 and arr[1][l] == 0 and arr[2][l] == 0 and arr[3][l] == 0 and arr[4][l] == 0:
                        line += 1
                    if line >= 3:
                        ans = i * 5 + j + 1
                        return


arr = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]

line = 0
ans = 0
flag = False

for i in range(5):
    if line >= 3:
        break
    for j in range(5):
        if line >= 3:
            break
        bingo(i, j)

print(ans)