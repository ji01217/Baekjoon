N = int(input())
lst = [0] + list(map(int, input().split()))

S = int(input())
arr = [list(map(int, input().split())) for _ in range(S)]

for i in range(S):
    if arr[i][0] == 1:  # 남학생
        for j in range(1, N + 1):
            if j % arr[i][1] == 0:
                if lst[j] == 0:
                    lst[j] = 1
                else:
                    lst[j] = 0
    else:  # 여학생
        j = 0
        while arr[i][1] - (j + 1) >= 1 and arr[i][1] + (j + 1) <= N and lst[arr[i][1] - (j + 1)] == lst[arr[i][1] + (j + 1)]:
            j += 1
        for k in range(arr[i][1] - j, arr[i][1] + j + 1):
            if lst[k] == 0:
                lst[k] = 1
            else:
                lst[k] = 0

for i in range(1, N + 1):
    print(lst[i], end=" ")
    if i % 20 == 0:
        print()