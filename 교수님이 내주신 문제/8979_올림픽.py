# nations, nation = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(nations)]
#
# ans = sorted(arr, key=lambda x: (x[1], x[2], x[3]), reverse=True)
# flag = False
#
# for i in range(nations):
#     if ans[i][0] == nation:
#         a = 1
#         if i - a == -1:
#             ranking = 1
#             flag = True
#             break
#         else:
#             while ans[i-a][1] == ans[i][1] and ans[i-a][2] == ans[i][2] and ans[i-a][3] == ans[i][3]:
#                 a += 1
#             ranking = i - a + 2
#             flag = True
#             break
#     if flag:
#         break
#
# print(ranking)

N, K = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    arr[nation] = [gold, silver, bronze]
rank = 1
for i in range(1, N+1):
    if arr[i][0] > arr[K][0]:
        rank += 1
    elif arr[i][0] == arr[K][0] and arr[i][1] > arr[K][1]:
        rank += 1
    elif arr[i][0] == arr[K][0] and arr[i][1] == arr[K][1] and arr[i][2] > arr[K][2]:
        rank += 1
print(rank)
