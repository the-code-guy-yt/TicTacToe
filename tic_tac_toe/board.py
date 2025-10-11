class Board:

    ROWS = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    COLS = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    DIAGS = [(0, 4, 8), (2, 4, 6)]
    
    CHECKS = ROWS + COLS + DIAGS

    def reset(self) -> None:
        """
        Resets the board to an empty state
        :return: Nothing
        """
        self.board = [' '] * 9
        self.available_moves = list(range(1,10))
        self.move_log.clear()
    
    def __init__(self) -> None:
        self.player_markers_allowed = ['O', 'X']
        self.available_moves = []
        self.board = []
        self.move_log = []
        self.reset()
        
    def move(self, position: int, player_marker: str) -> bool:
        """
        Processes a player move
        :param position: The position of the move on the board
        :param player_marker: The marker of the player
        :return: Whether the move was successful
        """
        placed = False
        if position in self.available_moves:
            self.available_moves.remove(position)
            position -= 1
            self.board[position] = player_marker
            placed = True
            self.move_log.append(position)
        
        return placed

    def undo(self):
        cell_pos = self.move_log.pop()
        self.available_moves.append(cell_pos+1)
        self.board[cell_pos] = ' '
    
    @property
    def playable_cells(self) -> list:
        return self.available_moves[:]

    @property
    def turns_left(self):
        return len(self.available_moves)
    
    @property
    def game_over(self):
        return not self.available_moves
    
    @property
    def winner(self) -> str:
        
        _winner = None
        for check in self.CHECKS:
            pos1, pos2, pos3 = check
            if self.board[pos1] == self.board[pos2] == self.board[pos3] != ' ':
                _winner = self.board[pos1]
                break
            
        return _winner
    
    def render(self):
        
        splitter = '--- --- ---\n'
        spacer = '   |   |   \n'
        board_str = spacer
        board_str += f' {self.board[6]} | {self.board[7]} | {self.board[8]}\n'
        board_str += spacer
        board_str += splitter
        board_str += spacer
        board_str += f' {self.board[3]} | {self.board[4]} | {self.board[5]}\n'
        board_str += spacer
        board_str += splitter
        board_str += spacer
        board_str += f' {self.board[0]} | {self.board[1]} | {self.board[2]}\n'
        board_str += spacer
        
        print(board_str)
        
    