for t in range(int(input())):
    s=input()
    s=s+'z'
    tmp,ans=0,10**16
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i-1].isdigit():
                ans=min(ans,tmp)
            tmp=0
        else:
            tmp=tmp*10+int(s[i])
    print(ans)