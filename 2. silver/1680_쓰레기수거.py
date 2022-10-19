T = int(input())
for t in range(T):
    W, N = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    total_dis = 0
    now_trash = 0
    for i in range(N):
        if now_trash + arr[i][1] < W:
            now_trash += arr[i][1]
        elif now_trash + arr[i][1] == W:
            total_dis += arr[i][0] * 2
            now_trash = 0
        else:
            total_dis += arr[i][0] * 2
            now_trash = 0
            now_trash += arr[i][1]
    if now_trash != 0:
        total_dis += arr[N-1][0] * 2

    print(total_dis)
