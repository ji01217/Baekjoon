# 입력
x, y = map(int, input().split())

# 풀이
num = 1
for i in range(7):
    num += i*6
    if i == x+y:
        break

# 출력
if y == 0:
    print(num)
elif y == 1:
    print(num - ((x+y)*6 - 1))
else:
    print(num - ((x+y)*6 - 1) + y - 1)