class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(len(board)):
            seen = set()
            for j in board[i]:
                if j!=".":
                    if j in seen:
                        return False
                    else:
                        seen.add(j)
        
        #check columns
        k = 0
        while k<9:
            seen = set()
            for i in range(len(board)):
                if board[i][k]!=".":
                    if board[i][k] in seen:
                        return False
                    else:
                        seen.add(board[i][k])
            k+=1

        #check 3x3 
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] != ".":
                            if board[i + x][j + y] in seen:
                                return False
                            else:
                                seen.add(board[i + x][j + y])
        return True