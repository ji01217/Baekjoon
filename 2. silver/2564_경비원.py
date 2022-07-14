# 왼쪽 맨위를 기준으로 사각형을 펼친다고 생각했을 때 상점이 떨어진 거리를 계산해주는 함수
def get_distance(loc, d):
    if loc == 1:  # 북쪽
        return d
    elif loc == 2:  # 남쪽
        return w + h + w - d
    elif loc == 3:  # 서쪽
        return w + h + w + h - d
    else:  # 동쪽
        return w + d


# 입력
w, h = map(int, input().split())  # 사각형의 너비, 높이
n = int(input())  # 상점의 개수

# 풀이
course = []
for _ in range(n + 1):
    loc, d = map(int, input().split())
    course.append(get_distance(loc, d))

ans = 0

for i in range(n):
    in_course = abs(course[-1] - course[i])  # 펼친 면에서 생각했을 때 동근이와 상점의 거리
    out_course = 2 * (w + h) - in_course  # 반대로 돌았을 때 동근이와 상점의 거리
    ans += min(in_course, out_course)  # 두 거리 중 작은 값을 ans에 더한다.

# 출력
print(ans)
