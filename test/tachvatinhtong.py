A=input()
while True:
    n=len(A)
    if n==1:
        break
    mid=n//2
    tmp=int(A[:mid]) +int(A[mid:])
    A=str(tmp)
    print(A)
    
   
