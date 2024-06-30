def base_8(number):
    while len(number)%3!=0:
        number='0'+number
    result=str()
    i=len(number)-1
    while i>=0:
        base_2=number[i-2:i+1]
        coso8=str(int(base_2,2))
        result=coso8+result
        i-=3
    return result
for _ in range (int(input())):
    t=input()
    print(base_8(t))