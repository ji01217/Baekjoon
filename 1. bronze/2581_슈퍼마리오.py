lst = [int(input()) for _ in range(10)]
ans = 0
for i in range(10):
    if ans + lst[i] <= 100:
        ans += lst[i]
    else:
        if abs(ans + lst[i] - 100) > abs(ans - 100):
            break
        else:
            ans += lst[i]
            break
print(ans)