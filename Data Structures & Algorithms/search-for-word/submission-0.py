class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        
        def value(r,c,ides):
            if ides==len(word):
                return True
            
            if r>=rows or r<0 or c<0 or c>=cols or board[r][c]!=word[ides] or board[r][c] =="#":
                return False

            temp=board[r][c]
            board[r][c]="#"

            found=(value(r+1,c,ides+1) or value(r-1,c,ides+1) or value(r,c-1,ides+1)or value(r,c+1,ides+1))
            board[r][c]=temp
            return found
        for r in range(rows):
            for c in range(cols):
                if value(r,c,0):
                    return True
        return False

