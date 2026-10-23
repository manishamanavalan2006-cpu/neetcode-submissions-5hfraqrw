class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rowlow=0
        rowhigh=len(matrix)-1
        collow=0
        colhigh=len(matrix[0])-1
        result=[]

        while(rowlow<=rowhigh) and (collow<=colhigh):
            
            #left to right
            for i in range(collow,colhigh+1):
                a=matrix[rowlow][i]
                result.append(a)
            rowlow+=1

            #top to bottom
            for i in range(rowlow,rowhigh+1):
                a=matrix[i][colhigh]
                result.append(a)
            colhigh-=1
            
            if rowlow>rowhigh or collow>colhigh:
                break

            #rightbottom to leftbottom
            for i in range(colhigh,collow-1,-1):
                a=matrix[rowhigh][i]
                result.append(a)
            rowhigh-=1

            #bottom to top

            for i in range(rowhigh,rowlow-1,-1):
                a=matrix[i][collow]
                result.append(a)
            collow+=1
        return result

