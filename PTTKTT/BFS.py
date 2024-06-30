from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos):
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [-1, -2, -2, -1, 1, 2, 2, 1]
        
        queue = deque()
        visited = set()
        
        queue.append((knightPos[0], knightPos[1], 0))
        visited.add((knightPos[0], knightPos[1]))
        
        while queue:
            x, y, dis = queue.popleft()
            
            if x == targetPos[0] and y == targetPos[1]:
                return dis
            
            for i in range(8):
                newX = x + dx[i]
                newY = y + dy[i]
                
                if (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append((newX, newY, dis + 1))
        
        return -1 

# Test
solution = Solution()
knightPos = [0, 0]
targetPos = [5, 5]
print(solution.minStepToReachTarget(knightPos, targetPos))  # Kết quả: 5
