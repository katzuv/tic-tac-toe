class Board:
    """Class that represents a Tic Tac Toe board."""
    EMPTY = ' '

    def __init__(self):
        """Instantiate a Tic Tac Toe board."""
        self._board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]

    def __str__(self):
        """
        :return: a string describing the current board
        :rtype: str
        """
        return ''.join(' | '.join(row) + '\n' for row in self._board)

    @property
    def board(self):
        """
        Return a read-only property of the board.

        :return: the current board
        :rtype: list
        """
        return self.board

    def move(self, player, row, column):
        """
        Make one move in the game and return whether a win occurred.
        :param player: current player
        :type player: str
        :param row: row the last mark has been inserted into
        :type row: int
        :param column: column the last mark has been inserted into
        :type column: int
        :return: whether a win occurred
        :rtype: bool
        """
        self._insert(player, row, column)
        return self._has_win_occurred(row, column)

    def is_full(self):
        """
        Return whether the board is full.

        :return: whether the board is full
        :rtype: bool
        """
        return all(self.EMPTY not in row for row in self._board)

    def is_cell_empty(self, row, column):
        """
        Return whether a certain cell is empty.

        :param row: row number of the checked cell
        :type row: int
        :param column: column number of the checked cell
        :type column: int
        :return: whether a certain cell is empty
        :rtype: bool
        """
        return self._board[row][column] == self.EMPTY

    def _insert(self, player, row, column):
        """
        Insert a mark of player into the board.
        :param player: current player
        :type player: str
        :param row: row the last mark has been inserted into
        :type row: int
        :param column: column the last mark has been inserted into
        :type column: int
        """
        self._raise_if_cell_full(row, column)
        self._raise_if_cell_not_in_bounds(row, column)
        self._board[row][column] = player

    @classmethod
    def _is_win_in_sequence(cls, sequence):
        return cls.EMPTY not in sequence and len(set(sequence)) == 1

    def _has_win_occurred(self, row_number, column_number):
        """
        Return whether a win has occurred.

        :param row: row the last mark has been inserted into
        :type row: int
        :param column: column the last mark has been inserted into
        :type column: int
        :return: whether a win has occurred
        :rtype: bool
        """
        sequences = list()
        sequences.append(self._board[row_number])  # row
        sequences.append([i[column_number] for i in self._board])  # column
        if row_number == column_number:
            sequences.append([self._board[i][i]
                              for i in range(3)])  # main diagonal
        if row_number == 2 - column_number:
            sequences.append([self._board[i][2 - i]
                              for i in range(3)])  # secondary diagonal

        return any(self._is_win_in_sequence(sequence) for sequence in sequences)

    def _raise_if_cell_full(self, row, column):
        """
        Raise a FullCellError if the inputted cell is already full.
        :param row: row of cell to be checked
        :type row: int
        :param column: column of cell to be checked
        :type column: int
        :raise: FullCellError
        """
        if self._board[row][column] != self.EMPTY:
            raise FullCellError(row, column)

    def _raise_if_cell_not_in_bounds(self, row, column):
        """
        Raise an OutOfBoundsError if the inputted cell is already full.
        :param row: row of cell to be checked
        :type row: int
        :param column: column of cell to be checked
        :type column: int
        :raise: OutOfBoundsError
        """
        if not (0 <= row < 3 and 0 <= column < 3):
            raise OutOfBoundsError(row, column)


class OutOfBoundsError(IndexError):
    """Exception for handling number of rows or columns inputted for cells that are out of board boundaries."""

    def __init__(self, row, column):
        """
        Instantiate a ColumnOutOfBoundsError exception.
        :param row: row inputted for checking if a cell is out of board boundaries
        :type row: int
        :param column: column inputted for checking if a cell is out of board boundaries
        :type column: int
        """
        super().__init__()
        self.row = row
        self.column = column


class FullCellError(Exception):
    def __init__(self, row, column):
        """
        Instantiate a FullColumnError exception.
        :param row: row inputted for checking if it is already full
        :type row: int
        :param column: column inputted for checking if it is already full
        :type column: int
        """
        super().__init__()
        self.row = row
        self.column = column
