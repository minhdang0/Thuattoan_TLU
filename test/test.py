day = ('456$', '789$', '239$' , '729$', '1243$', '811$' , '123$') 
st='Hellob'
print(day[0][1:])
print(st[-1:])

import re


array = ('₹399', '₹1,099')
 
so_list = []  # Tạo một danh sách để lưu trữ các số

for chuoi in array:
    # Loại bỏ các ký tự không phải số và dấu phẩy
    cleaned_chuoi = ''.join(filter(str.isdigit, chuoi))
    
    # Chuyển chuỗi thành số nguyên và thêm vào danh sách
    so = int(cleaned_chuoi)
    so_list.append(so)

# In danh sách các số
print(so_list)
import re

array = ('₹399', '₹1,099')

so_list = []  # Tạo một danh sách để lưu trữ các số

for chuoi in array:
    # Sử dụng biểu thức chính quy để tìm số
    match = re.search(r'\d+', chuoi)
    if match:
        so = int(match.group())
        so_list.append(so)

# In danh sách các số
print(so_list)



