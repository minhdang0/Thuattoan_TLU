if __name__ == '__main__':
    n = int(input())
    a = [list(input()) for _ in range(n)]
    
    row_counts = [0] * n  
    col_counts = [0] * n   

    for i in range(n):
        for j in range(n):
            if a[i][j] == 'C':
                row_counts[i] += 1
                col_counts[j] += 1
    
    cnt = 0  
    
    for count in row_counts:
        cnt += count * (count - 1) // 2
    
    for count in col_counts:
        cnt += count * (count - 1) // 2
    
    print(cnt)
