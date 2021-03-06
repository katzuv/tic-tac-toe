from pytest import mark

from board.board import Board
from players import RandomComputer


@mark.parametrize('mark', ('X', 'O'))
def test_row(mark):
    board = Board()
    board._rows = [[' ', ' ', ' '],
                   [' ', mark, mark],
                   [' ', mark, ' ']]

    for _ in range(100):
        player = RandomComputer(mark)
        row, column = player.turn(board)
        assert board.is_cell_empty(row, column)
