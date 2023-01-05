class player(object):
    """
    Represents a player in a game of tic-tac-toe
    Includes the player's mark ('X' or 'O') and their current score
    """

    def __init__(self, mark):
        """
        Initializes a player object
        """
        
        # mark must be a single character letter string

        assert (mark == 'X') or (mark == 'O')
        self.mark = mark
        self.score = 0
    
    
