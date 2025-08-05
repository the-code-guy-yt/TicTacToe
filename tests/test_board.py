import unittest
from tic_tac_toe.board import Board

class TestBoardMove(unittest.TestCase):
    
    def test_valid_move(self):
        board = Board()
        result = board.move(1,'X')
        self.assertTrue(result)
        self.assertEqual(board.board[0], 'X')
        
    def test_no_overwrite_cell(self):
        board = Board()
        result = board.move(1, 'X')
        self.assertTrue(result)
        result = board.move(1, 'O')
        self.assertFalse(result)
        
        