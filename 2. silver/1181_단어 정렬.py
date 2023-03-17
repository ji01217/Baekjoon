N = int(input())
s = set()
for _ in range(N):
    s.add(input())
lst = list(s)
lst.sort(key =  lambda x: (len(x), x))
for word in lst:
    print(word)