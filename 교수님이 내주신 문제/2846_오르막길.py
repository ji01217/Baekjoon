N = int(input())
lst = list(map(int, input().split()))
ans = 0
start = -1
for i in range(1, N):
    if lst[i - 1] < lst[i] and start == -1:
        start = i - 1
    elif lst[i - 1] >= lst[i] and start >= 0:
        end = i - 1
        hill = lst[end] - lst[start]
        if ans < hill:
            ans = hill
        start = -1
    elif i == N - 1 and start >= 0:
        end = i
        hill = lst[end] - lst[start]
        if ans < hill:
            ans = hill
print(ans)