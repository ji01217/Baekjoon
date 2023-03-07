N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()
for i in range(N):
    print(lst[i][0], lst[i][1])