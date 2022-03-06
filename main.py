from game import Game

if __name__ == "__main__":
    game = Game()
    game.board.print_board()

    while True:
        start = input("From: ")
        to = input("To: ")

        # translate is a helper method to turn the user input into
        # a representation depending on how the board is represented
        # start = translate(start)
        # to = translate(to)

        if start == None or to == None:
            continue

        game.move(start, to)


        # check for promotion pawns
        i = 0
        # TODO: I don't like how he suggests to do this
        # let's implement this with methods in game rather than using instantiated class methods and properties
        while i < 8:
            if not game.turn and game.board.board[0][i] != None and \
                    game.board.board[0][i].name == 'P':
                game.promotion((0, i))
                break
            elif game.turn and game.board.board[7][i] != None and \
                    game.board.board[7][i].name == 'P':
                game.promotion((7, i))
                break
            i += 1

        game.board.print_board()
