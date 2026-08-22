class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        r,c=len(matrix), len(matrix[0])
        # transpose=[[0 for _ in range(c)] for _ in range(r)]

        # for i in range(r):
        #     for j in range(c):
        #         transpose[i][j]=matrix[j][i]

        #     transpose[i]=transpose[i][::-1]
        matrix.reverse()
        for i in range(r):
            for j in range(i+1,c):
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        # matrix.reverse()

                

        