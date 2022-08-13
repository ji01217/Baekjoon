from collections import deque

# 입력
N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 풀이
dq = deque([i for i in range(1, N+1)])
count = 0
for i in lst:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1

# 출력
print(count)