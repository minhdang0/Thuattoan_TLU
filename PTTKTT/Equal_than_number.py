def sumIndex(arr):
    newArray = [0] * len(arr)
    newArray[0] = arr[0]
    for i in range(1, len(arr)):
       newArray[i] = arr[i] + newArray[i-1]
    return newArray

b = [1,1,1]
number =int(input("Nhập số : "))
Results= []
while b:
    newArr=sumIndex(b)
    for i in range(len(newArr)):
        if newArr[i]>number:
            Results.append(newArr[i])
    newArr.clear()
    b.pop(0)
final_Result = set(Results)
print(len(final_Result))
    