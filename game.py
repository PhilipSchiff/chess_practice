import board


class Game:
    """
    Put description of the Game class here
    """

    def __init__(self):
        self.board = board.Board()
        self.turn = None

    def algebraic_to_board_indices(self, algebraic_square):
        assert type(algebraic_square) == str
        assert len(algebraic_square) == 2
        file = algebraic_square[0]
        file_dict = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
        assert file in file_dict.keys()
        row = int(algebraic_square[1])
        assert 1 <= row <= 8
        i = row - 1 # 1, 2, 3... 8 ---> 0, 1, 2... 7
        j = file_dict.get(file)
        return i, j

    def promotion(self, square):
        """
        square: a tuple (rank, file) describing a square
        """
        # add any parameters necessary and replace the body with
        # functionality on promoting a Pawn that has reached the
        # end of the board
        pass

    def move(self, start, to):
        """
        start: starting square
        to: square to move to
        """
        print(f"Moving from {start} to {to}")
        start_square_indices = self.algebraic_to_board_indices(start)
        to_square_indices = self.algebraic_to_board_indices(to)