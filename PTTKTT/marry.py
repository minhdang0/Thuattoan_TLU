men = [['C', 'B', 'E', 'A', 'D'],
       ['A', 'B', 'E', 'C', 'D'],
       ['D', 'C', 'B', 'A', 'E'],
       ['A', 'C', 'D', 'B', 'E'],
       ['A', 'B', 'D', 'E', 'C']]

women = {'A': [2, 4, 1, 0, 3],
         'B': [4, 1, 0, 3, 2],
         'C': [3, 2, 4, 0, 1],
         'D': [0, 1, 2, 3, 4], 
         'E': [1, 2, 3, 0, 4]}

n = len(men)
married = {}
freemen = list(range(n))

while freemen:
    for man in freemen:
        woman = men[man][0]  #gán phụ nữ bằng người đàn ông
        if woman not in married.values():# neu cô vợ chưa có chồng
            married[man] = woman
            freemen.remove(man)
        else:
            for key,value in married.items():
                if value == woman: 
                    current_man=key #tim ra người đàn ông có vợ trùng với man
            tmp0 = women[woman].index(man)
            tmp1 = women[woman].index(current_man)
            if tmp0 < tmp1: #vợ đó thik man hơn chồng hiện tại
                married[current_man]='' #trả tự do cho current_man
                married[man] = woman# cho cô vợ kết hôn với man
                freemen.append(current_man) 
                freemen.remove(man)# xóa man khỏi mảng chưa vợ
            men[man].pop(0) 
            break  
for key,value in married.items():
    print(key+1,' - ', value)
