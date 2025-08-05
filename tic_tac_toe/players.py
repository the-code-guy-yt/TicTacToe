import abc
from .board import Board
from random import randint
from common.input_validation import get_numeric


class BasePlayer(abc.ABC):
    
    @abc.abstractmethod
    def make_move(self):
        pass
    
    
class Player(BasePlayer):
    
    def __init__(self, board: Board, marker, name):
        self.marker = marker
        self.board = board
        self.name = name
        
    def make_move(self):
        raise NotImplementedError
        

class AIPlayer(Player):
    
    def __init__(self, board: Board, marker: str, name: str) -> None:
        super().__init__(board, marker, name)
        temp = self.board.player_markers_allowed[:]
        temp.remove(marker)
        self.opponent_marker = temp[0]
        
    def evaluate_board_state(self) -> int:
        if self.board.winner is not None:
            if self.board.winner == self.marker:
                score = 1
            else:
                score = -1
        else:
            score = 0
        
        return score
    
    def mini_max(self, is_max: bool):
        
        if self.board.game_over or self.board.winner:
            move = -1
            best = self.evaluate_board_state()
        else:
            best = -2 if is_max else 2
            actual_payer_marker = self.marker if is_max else self.opponent_marker
            
            for possible_move in self.board.playable_cells:
                self.board.move(possible_move, actual_payer_marker)
                score, _ = self.mini_max(not is_max)
                self.board.undo()
                
                if (is_max and score > best) or (not is_max and score < best):
                    best = score
                    move = possible_move
            
        return best, move
        
    def make_move(self):
        
        if self.board.turns_left == 9:
            cell = randint(1, 9)
        else:
            _, cell = self.mini_max(is_max=True)
        
        placed = self.board.move(cell, self.marker)


class HumanPlayer(Player):
    
    def __init__(self, board: Board, marker: str, name: str) -> None:
        super().__init__(board, marker, name)
    
    def make_move(self):
        
        placed = False
        while not placed:
            placed = self.board.move(
                get_numeric(prompt_text='Select Game Cell (0-9)', range_start=1, range_end=9),
                self.marker
            )


class PlayerAlternator:
    
    def __init__(self, players: list):
        self.players = players
        self.__current_player = 0
    
    @property
    def current_player(self):
        return self.players[self.__current_player]
    
    def switch_player(self):
        if self.__current_player == len(self.players)-1:
            self.__current_player = 0
        else:
            self.__current_player += 1
