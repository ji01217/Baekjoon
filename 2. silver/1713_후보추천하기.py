N = int(input())
r = int(input())
lst = list(map(int, input().split()))

pic = []
cnt = []

for i in range(r):
    if lst[i] in pic:
        for j in range(len(pic)):
            if lst[i] == pic[j]:
                cnt[j] += 1
    else:
        if len(pic) == N:
            for j in range(len(cnt)):
                if cnt[j] == min(cnt):
                    pic.pop(j)
                    cnt.pop(j)
                    break
        pic.append(lst[i])
        cnt.append(1)

pic.sort()
print(*pic)