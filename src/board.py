class board(object):
    """
    A tic-tac-toe board
    """

    def __init__(self):
        """
        Initializes a board object for tic tac toe
        """
        self.grid = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
                ]

    def getCoord(self, coord):
        """
        Returns the mark at coordinate 'coord', None if no mark
        """
        r,c = coord
        return self.grid[r][c]
    def setCoord(self, coord, mark):
        """
        Sets the board to 'mark' at 'coord'

        Parameters:
        coord - tuple (r,c) where r is the row and c is the column of the 3x3 grid

        mark - a player's mark (either 'X' or 'O')
        """
        r,c = coord
        self.grid[r][c] = mark



    def check_win(self):
        """
        Checks who won the current board, if there is a winner

        Returns a tuple -- (b,p) where b is a boolean (True if winner, False otherwise)
        and p is the mark of the winner (either 'X' or 'O'). If there is no winner, p is None
        """
        rows = self._win_rows()
        if rows[0]:
            return rows
        if self._win_cols()[0]:
            return self._win_cols()
        if self._win_diag()[0]:
            return self._win_diag()
        else:
            return (False, None)

    def _win_rows(self):
        """
        Checks if the rows of the board form a valid win (a diagonal is filled with a single mark)
        
        Returns a tuple of (b, p)
        where b is a boolean (True if winner, false else)
        and p is the mark of the winner (either 'X' or 'O').
        If there is no winner, p is None
        """
        for row in self.grid:
            if row[0] == row[1] and row[1] == row[2]:
                if row[1] is not None:
                    return True, row[0]
        return False, None

    def _win_cols(self):
        """
        Checks if the rows of the board form a valid win (a column is filled with a single mark)
        
        Returns a tuple of (b, p)
        where b is a boolean (True if winner, false else)
        and p is the mark of the winner (either 'X' or 'O').
        If there is no winner, p is None
        """
        
        for col in range(3):
            if (self.grid[1][col] == self.grid[2][col]) and (self.grid[2][col] == self.grid[0][col]):
                if self.grid[1][col] is not None:
                    return True, self.grid[1][col]
        return False, None
                    
    def _win_diag(self):
        """
        Checks if the diagonals of the board form a valid win (a row is filled with a single mark)
        
        Returns a tuple of (b, p)
        where b is a boolean (True if winner, false else)
        and p is the mark of the winner (either 'X' or 'O').
        If there is no winner, p is None
        """
        
        g = self.grid
        if (g[0][0] == g[1][1] and g[1][1] == g[2][2]) or (g[0][2] == g[1][1] and g[1][1] == g[2][0]):
            if g[1][1] is not None:
                return True, g[1][1]
        return False, None
    



