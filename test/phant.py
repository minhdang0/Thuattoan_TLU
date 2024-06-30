import time

start_time = time.time()

import math

def uoc(n):

    aray=[]
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
             aray.append(i)
    return aray

for t in range (int(input())):
    X=int(input())
    min=0
    for i in range(2,X):
        if len(uoc(X))<=len(uoc(i)):
            X+=1
        else:
            min=X
    print(min)

 
end_time = time.time()
elapsed_time = end_time - start_time

print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

 