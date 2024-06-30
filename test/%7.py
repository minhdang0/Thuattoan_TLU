
# N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.

# Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.
def reverse(num):
    for i in range (1000):
        if num%7==0:
            return num
        num+= int(str(num)[::-1])    
    return -1
for i in range(int(input())):
    N=int(input())
    print(reverse(N))