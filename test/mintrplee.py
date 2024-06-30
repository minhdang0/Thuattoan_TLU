import sys
def mintriple(n,array):
    ans = sys.maxsize;
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans = min(ans, array[i] + array[j] + array[k]);
    return ans;
for t in range (int(input())):
    N = int(input())
    A=list(map(int,input().split()))
    result=mintriple(N,A)
    print(result)