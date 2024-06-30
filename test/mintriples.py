import sys
def mintriple(N,A):
    min1, min2, min3=sys.maxsize()
    for i in range (N):
        if A[i]<min1:
            min3=min2
            min2=min1
            min1=A[i]
        elif A[i]<min2:
            min2=A[i]
            min3=min2
        elif A[i]<min3:
            min3=A[i]
    return min1+min2+min3

T= int( input())
for _ in range(T):
    N = int(input())
    A=list(map(int,input().split()))
    result=mintriple(N,A)
    print(result)