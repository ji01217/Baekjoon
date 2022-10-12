while True:
    try:
        a = input()
        b = input()
        alpha1 = {}
        alpha2 = {}
        ans = ''
        for i in a:
            if i in alpha1:
                alpha1[i] += 1
            else:
                alpha1[i] = 1
        for i in b:
            if i in alpha2:
                alpha2[i] += 1
            else:
                alpha2[i] = 1
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
