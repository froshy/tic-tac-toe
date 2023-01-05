import board
import player


def assertEquals(arg, exp):
    """
    A helper testing function

    Parameters:
    arg - the argument wanting to be tested

    exp - the expected value 
    """

    assert arg == exp, f"Expected {exp} but instead got {arg}"
col1_win = [
            ["X", None, None],
            ["X", None, None],
            ["X", None, None],
        ]

col2_win = [
            [None, "X", None],
            [None, "X", None],
            [None, "X", None],
        ]

col3_win = [
            [None, None, "X"],
            [None, None, "X"],
            [None, None, "X"],
        ]

row1_win = [
            ["X", "X", "X"],
            [None, None, None],
            [None, None, None],
        ]

row2_win = [
            [None, None, None],
            ["X", "X", "X"],
            [None, None, None],
        ]

row3_win = [
            [None, None, None],
            [None, None, None],
            ["X", "X", "X"],
        ]

diag1_win = [
            ["X", None, None],
            [None, "X", None],
            [None, None, "X"],
        ]

diag2_win = [
            [None, None, "X"],
            [None, "X", None],
            ["X", None, None],
        ]


class test(object):
    """
    The testing suite for the tic-tac-toe game
    """
    
    def testBoard(self):
        """
        Testing suite for module board
        """
        b = board.board()
        # testing get coord on empty board
        assertEquals(b.getCoord((0,0)), None)
        assertEquals(b.getCoord((1,1)), None)
        # testing setting coord and getting coord 
        b.setCoord((0,0), 'X')
        assertEquals(b.getCoord((0,0)), 'X')
        b.setCoord((0,1), 'O')
        assertEquals(b.getCoord((0,1)), 'O')

        # testing positive wins
        b = board.board()
        b2 = board.board()
        b2.grid = col1_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = col2_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = col3_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = row1_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = row2_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = row3_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = diag1_win
        assertEquals(b2.check_win(), (True, 'X'))
        b2.grid = diag2_win
        assertEquals(b2.check_win(), (True, 'X'))
        # testing none-winning boards
        b2.grid = b.grid
        assertEquals(b2.check_win(), (False, None))
        b2.setCoord((0,1), 'X')
        b2.setCoord((0,2), 'X')
        b2.setCoord((1,0), 'X')
        b2.setCoord((2,1), 'X')
        b2.setCoord((2,2), 'X')
        assertEquals(b2.check_win(), (False, None))
        temp = b2.grid
        b2.setCoord((1,1), 'X')
        assertEquals(b2.check_win(), (True, 'X'))
        # testing if X-O-X diagonal -> false
        b2.setCoord((1,1), 'O')
        assertEquals(b2.check_win(), (False, None))
        

    def testall(self):
        """
        Calls all test functions here
        """
        self.testBoard()
        print('Passed all tests')
        

t = test()
t.testall()
