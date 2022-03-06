# I added some helper functions here when I saw the same code logic repeated

class Piece:
    """
    Put description of the Piece class here
    """

    def __init__(self):
        # add any additional parameters
        # standard initiation of a piece
        pass

    def is_valid_move(self):
        return False

    def is_white(self):
        pass

    def __str__(self):
        # replace the body and return a string with how you want your piece
        # to be printed as when `print([A Piece Object])` is called
        return ''


# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation
class Rook(Piece):
    def __init__(self, color):
        super().__init__()

    def is_valid_move(self, board=None, start=None, to=None):
        pass


class Knight(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class Bishop(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        super().__init__()


class Queen(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class King(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass

    # I added an extra method for the King class
    def can_castle(self):
        pass


# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__()

    def is_valid_move(self):
        return False


class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass