class MATRIX:
    def __init__(self, n, m, array):
        self.n = n
        self.m = m
        self.array = array

    def transpose(self):
        result = [[self.array[j][i] for j in range(self.n)] for i in range(self.m)]
        return MATRIX(self.m, self.n, result)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Số cột của ma trận thứ nhất phải bằng số hàng của ma trận thứ hai.")
        result = [[0 for _ in range(other.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i][j] += self.array[i][k] * other.array[k][j]
        return MATRIX(self.n, other.m, result)

    def __str__(self):
        res = ''
        for i in range(self.n):
            for j in range(self.m):
                res += str(self.array[i][j]) + ' '
            res += '\n'
        return res

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        array = []
        for i in range(n):
            row = list(map(int, input().split()))
            array.append(row)
        matran = MATRIX(n, m, array)
        
        result = matran * matran.transpose()
        for row in result.array:
            print(*row)

    
        


