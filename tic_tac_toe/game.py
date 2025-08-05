from .board import Board
from .players import AIPlayer, HumanPlayer, PlayerAlternator, Player
import os


def clear_and_render(game_board):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    game_board.render()
    
    
def play_game(human_players: int):
    message = ''
    game_board = Board()
    if human_players == 1:
        play1 = HumanPlayer(game_board, marker='O', name='Player 1')
        play2 = AIPlayer(game_board, marker='X', name='AI')
    elif human_players == 2:
        play1 = HumanPlayer(game_board, marker='O', name='Player 1')
        play2 = HumanPlayer(game_board, marker='X', name='Player 1')
    else:
        play1 = AIPlayer(game_board, marker='O', name='AI_001')
        play2 = AIPlayer(game_board, marker='X', name='AI_002')
    
    players = PlayerAlternator([play1, play2])
    
    while not game_board.winner and not game_board.game_over:
        if human_players > 0:
            clear_and_render(game_board)
        
        current_player = players.current_player
        
        current_player.make_move()
        
        if game_board.winner:
            clear_and_render(game_board)
            message = f'{current_player.name} won the game!'
        else:
            if game_board.game_over:
                clear_and_render(game_board)
                message = 'Game was a Tie'
        
        players.switch_player()
    
    return message
    
    
    