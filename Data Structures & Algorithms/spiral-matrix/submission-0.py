class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res=[]

        while left < right and top < bottom:

            # get the elements from left to right
            for i in range(left, right):
                res.append(matrix[left][i])

            top+=1
            # get the elements from top to bottom on right side
            for i in range(top, bottom):
                res.append(matrix[i][right-1])

            right-=1

            if not(left < right and top < bottom):
                break
            
            # get the elements from the right to left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            # get the elements from the bottom to top on Left side

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])

            left+=1
        
        return res

        