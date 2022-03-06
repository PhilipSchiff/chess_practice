import board


class Game:
    """
    Put description of the Game class here
    """

    def __init__(self):
        self.board = board.Board()
        self.turn = None

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
