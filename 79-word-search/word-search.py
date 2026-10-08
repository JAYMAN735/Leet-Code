class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)  #row
        n=len(board[0]) #column
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=m or c<0 or c>=n or board[r][c] != word[i]:
                return False

            temp=board[r][c]
            board[r][c]="#"

            found=(dfs(r+1,c,i+1)or
                    dfs(r-1,c,i+1)or
                    dfs(r,c+1,i+1)or
                    dfs(r,c-1,i+1))

            board[r][c]=temp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False
