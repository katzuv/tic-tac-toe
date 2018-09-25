from itertools import cycle
from random import randint

from board import Board


class Game:
    """Class that represents a Tic Tc Toe game."""

    def __init__(self, player_x, player_y):
        """Instantiate a Tic Tac Toe game.

        :param x: type of the first player (player x)
        :type x: Player
        :param y: type of the second player (player y)
        :type y: Player
        """
        self.board = Board()
        self.player_x = player_x()
        self.player_y = player_y()

    def play(self):
        """Main method running the game."""
        for player in cycle((self.player_x, self.player_y)):
            row, column = player.turn()
            if self.board.move(player.mark, row, column):
                self.print_win(player)
                return

            if self.board.is_full():
                print(self.board)
                self.print_game_over()
                return

    def print_win(self, winner_mark):
        """
        Print the winner's mark.

        :param player: the winner
        :type player: str
        """
        print(self.board)
        print(f'Player {winner_mark} has won! :)')

    def print_game_over(self):
        """Print that the board is full and the game ended in a tie."""
        print(self.board)
        print('Board is full, tie.')


# def ai():
#     board = Board()

#     # first move
#     while True:
#         try:
#             player = 'X'
#             row, column = cell_input(player)
#             board.move(player, row, column)
#             print(board)
#             break
#         except OutOfBoundsError as error:
#             print(
#                 f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
#         except Exception as error:
#             print(error)

#     if row == 2 and column == 2:
#         board.move('O', 0, 0)

#     if any((row == 0, row == 2 and column == 0, row == 1 and column == 2)):
#         board.move('O', 1, 1)

#     while True:
#         print(board)
#         while True:
#             try:
#                 player = 'X'
#                 row, column = cell_input(player)
#                 if board.move(player, row, column):
#                     print(board)
#                     print_win(player)
#                     return
#                 break
#             except OutOfBoundsError as error:
#                 print(
#                     f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
#             except FullCellError as error:
#                 print(
#                     f'The cell inputted at row {error.row + 1}, column {error.column + 1} is already full.')
#             except Exception as error:
#                 print(error)

#         # The strategy is taken from https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy
#         while True:
#             player = 'O'
#             other = 'X'

#             # 1) Win: If the player has two in a row, they can place a third to get three in a row.
#             # traverse the main diagonal
#             main_diagonal = [board._board[i][i] for i in range(3)]
#             if fill_last_empty(board, main_diagonal, player, other, row):
#                 return

#             # traverse the secondary diagonal
#             secondary_diagonal = [board._board[i][2 - i] for i in range(3)]
#             if fill_last_empty(board, secondary_diagonal, player, other, row):
#                 return

#             for row in board._board:
#                 # traverse the row
#                 if row.count(player) == 2 and row.count(other) == 0:
#                     if board.move(player, row, row.index(board.EMPTY)):
#                         print(board)
#                         print_win(player)
#                         return

#                 # traverse the column
#                 column = [board._board[row] for row in range(3)]
#                 if column.count(player) == 2 and column.count(other) == 0:
#                     if board.move(player, row, column.index(board.EMPTY)):
#                         print(board)
#                         print_win(player)
#                         return

#             # 2) Block: If the opponent has two in a row, the player must play the third themselves to block the
#             # opponent.
#             # traverse the main diagonal
#             main_diagonal = [board._board[i][i] for i in range(3)]
#             if main_diagonal.count(other) == 2 and main_diagonal.count(player) == 0:
#                 if board.move(player, row, main_diagonal.index(board.EMPTY)):
#                     print(board)
#                     print_win(player)
#                     return

#             # traverse the secondary diagonal
#             secondary_diagonal = [board._board[i][2 - i] for i in range(3)]
#             if secondary_diagonal.count(other) == 2 and secondary_diagonal.count(player) == 0:
#                 if board.move(player, row, main_diagonal.index(board.EMPTY)):
#                     print(board)
#                     print_win(player)
#                     return

#             for row in board._board:
#                 # traverse the row
#                 if row.count(other) == 2 and row.count(player) == 0:
#                     if board.move(player, row, row.index(board.EMPTY)):
#                         print(board)
#                         print_win(player)
#                         return

#                 # traverse the column
#                 column = [board._board[row] for row in range(3)]
#                 if column.count(other) == 2 and column.count(player) == 0:
#                     board.move(player, row, column.index(board.EMPTY))
#                     print(board)
#                     print_win(player)
#                     return

#         if board.is_full():
#             print(board)
#             print_game_over()
#             return
#
#
# def fill_last_empty(board, sequence, player, other, row):
#     if sequence.count(player) == 2 and sequence.count(other) == 0:
#         if board.move(player, row, sequence.index(board.EMPTY)):
#             print(board)
#             print_win(player)
#             return True
