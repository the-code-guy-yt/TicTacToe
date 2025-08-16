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
        self.board = [None] * 9
        self.move_log.clear()
        self._move = 0
    
    def __init__(self) -> None:
        self.player_markers_allowed = ['O', 'X']
        self.board = []
        self.move_log = []
        self.reset()
        self._move = 0
        
    def move(self, position: int, player_marker: str) -> bool:
        """
        Processes a player move
        :param position: The position of the move on the board
        :param player_marker: The marker of the player
        :return: Whether the move was successful
        """
        placed = False
        position -= 1
        if self.board[position] is None:
            self.board[position] = player_marker
            placed = True
            self.move_log.append(position)
            self._move += 1
        
        return placed

    def undo(self):
        cell_pos = self.move_log.pop()
        self.board[cell_pos] = None
        self._move -= 1
    
    @property
    def playable_cells(self) -> list:
        return [cell_id + 1 for cell_id, cell in enumerate(self.board) if cell is None]

    @property
    def turns_left(self):
        return 9 - self._move
    
    @property
    def game_over(self):
        return self.turns_left == 0
    
    @property
    def winner(self) -> str:
        
        _winner = None
        for check in self.CHECKS:
            pos1, pos2, pos3 = check
            if self.board[pos1] == self.board[pos2] == self.board[pos3] is not None:
                _winner = self.board[pos1]
                break
            
        return _winner
    
    def render_cell(self, position):
        ret = ' '
        temp = self.board[position - 1]
        if temp is not None:
            ret = temp
        
        return ret
    
    def render(self):
        
        splitter = '--- --- ---\n'
        spacer = '   |   |   \n'
        board_str = spacer
        board_str += f' {self.render_cell(7)} | {self.render_cell(8)} | {self.render_cell(9)}\n'
        board_str += spacer
        board_str += splitter
        board_str += spacer
        board_str += f' {self.render_cell(4)} | {self.render_cell(5)} | {self.render_cell(6)}\n'
        board_str += spacer
        board_str += splitter
        board_str += spacer
        board_str += f' {self.render_cell(1)} | {self.render_cell(2)} | {self.render_cell(3)}\n'
        board_str += spacer
        
        print(board_str)
        
    