def songuyento(n):
    prime = list()
    for i in range (2, int((n**0.5)+1)):
        if prime[i]:
            for j in range (i*i, n+1 , i):
                prime[i]=False
    return [i for i in range (2,n+1)if prime[i]]

print(songuyento(120))

        
        