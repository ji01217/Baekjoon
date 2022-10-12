from collections import defaultdict

while True:
    try:
        a = input()
        b = input()
        alpha1 = defaultdict(int)
        alpha2 = defaultdict(int)
        ans = ''
        for i in a:
            alpha1[i] += 1
        for i in b:
            alpha2[i] += 1
        s = []
        for char in alpha1:
            if char in alpha2:
                s.append(char)
        s.sort()
        for char in s:
            ans += char * min(alpha1[char], alpha2[char])
        print(ans)
    except:
        break
