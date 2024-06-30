def nicenumber(num):
    array=[]
    while num>0:
       j=num%10
       array.append(j)
       num=num//10
    for i in range (0,len(array)):
        if array[i]!=array[i+2]:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    N=int(input())
    print(nicenumber(N))