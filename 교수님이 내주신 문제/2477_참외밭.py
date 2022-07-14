K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

width = []
height = []
total = []

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        width.append(arr[i][1])
        total.append(arr[i][1])
    else:
        height.append(arr[i][1])
        total.append(arr[i][1])

big = max(height) * max(width)
maxhidx = total.index(max(height))
maxwidx = total.index(max(width))

smallh = abs(total[maxhidx - 1] - total[0 if maxhidx == 5 else maxhidx + 1])
smallw = abs(total[maxwidx - 1] - total[0 if maxwidx == 5 else maxwidx + 1])

area = big - smallh * smallw

print(area * K)
