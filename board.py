class Board:
    """
    Put description of the Board class here
    """

    STARTING_POSITION = [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"]
    ]

    def __init__(self):
        self.board = Board.STARTING_POSITION


    def print_board(self):
        # replace body with how you want your board printed
        print("Printing the Board")
        board_string = ""
        for row in self.board:
            for square in row:
                board_string += "|"
                if square:
                    board_string += square
                else:
                    board_string += " "
            board_string += "|\n"

        print(board_string)
