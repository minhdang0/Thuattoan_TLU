def Sum_Large_integer(A,B):
    list_A=list(A)
    list_B=list(B)
    if list_A[0] == 0:
        list_A.pop(list_A[0])
    if list_B[0] == 0:
        list_B.pop(list_B[0])
    result=int("".join(list_A))+int("".join(list_B))
    return result
A=input()
B=input()

print(Sum_Large_integer(A,B))
