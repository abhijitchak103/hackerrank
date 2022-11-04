def happy(n: int):
    s = str(n)
    ans = 0
    for i in range(len(s)):
        ans += int(s[i])**2
    
    while ans != n or ans != 1:
        s = str(ans)
        ans = 0
        for i in range(len(s)):
            ans += int(s[i])**2

    if ans == 1:
        print(True)
        return True
    else:
        print(False)
        return False

happy(13)