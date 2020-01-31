from tictactoe import *
import os

class Play(object):
    
    VERSION_STRING = "v1.0"

    @staticmethod
    def init():
        # Optionally clear the screen.
        Play.clear()

        # Show the welcome banner.
        Play.showBanner()

        # Initialize the game backend.
        game = TicTacToe()

        # Let the X character to turn first.
        lastMove = TicTacToe.CHARACTER_X_SYMBOL

        # Game loop
        while True:
            # Clear the screen on every (hopefully, frame).
            Play.clear()

            # Render (or shows) the board.
            Play.renderBoard(game)

            # Getting the winner.
            # This method is used to prevent bad experience if we had to
            # call `playerMoves` in the beginning.
            winner = game.getWinner()

            # Check for the winner existance.
            if len(winner) > 0:
                print("Game has been ended!")
                print("The winner is Player {}".format(winner))
                break
            # A condition where nobody (everybody) won the game. In the other hand, tie is occured.
            elif len(game.getPlayerMovesRecord(TicTacToe.CHARACTER_X_SYMBOL)) + len(game.getPlayerMovesRecord(TicTacToe.CHARACTER_O_SYMBOL)) == 9:
                print("Game tied!")
                break

            # Check and validate all player's move.
            Play.playerMoves(game, lastMove)

            # Swap the turn.
            lastMove = TicTacToe.CHARACTER_O_SYMBOL if lastMove == TicTacToe.CHARACTER_X_SYMBOL else TicTacToe.CHARACTER_X_SYMBOL

    @staticmethod
    def playerMoves(game: TicTacToe, character: str):
        while True:
            # Prompt the player to select the cell.
            selectedCell = (Play.readMoves(character)) - 1

            # Check if the selected cell is taken by themselves or their opponent.
            if game.isCellTaken(selectedCell):
                print("The cell that you selected is taken!")
                print("Please insert another cell.")
                continue

            # In this state, the cell is empty and ready to be inserted with a new value.

            # Inserting the cell with value: character (X or O).
            game.insertCellValue(selectedCell, character)

            # Save the player's record into its list.
            game.saveMovesRecord(selectedCell, character)

            # Get the player's move record.
            playerMoves = game.getPlayerMovesRecord(character)

            # Whenever the record has reach 3 or more element
            # it is a valid moves to win the game.
            # This method is kinda hack, because the function `checkMoves` is so expensive.
            if len(playerMoves) >= 3:
                # If player's move matches with the Data Set
                # it should stop the game by flagging the winner.
                if game.checkMoves(playerMoves):
                    game.setWinner(character)
            break

    @staticmethod
    def readMoves(character: str) -> int:
        while True:
            buffer = input("Player {} turns, please input cell number [1..9]: ".format(character))
            if buffer.isnumeric() and len(buffer) == 1:
                return int(buffer)

    @staticmethod
    def renderBoard(game: TicTacToe) -> None:
        for i in range(1, 4):
            c1, c2, c3 = list(map(lambda lst: "_" if lst[0] == None else lst[0], game.getBoardRow(i)))
            print("\t{}\t|\t{}\t|\t{}\t".format(c1, c2, c3))
    
    @staticmethod
    def showBanner() -> None:
        if os.name.startswith("posix"):
            sttyBuffer = os.popen("stty size", "r").read().split()
            h, w = int(sttyBuffer[0]), int(sttyBuffer[1])

            print()
            print("TicTacToe {}".format(Play.VERSION_STRING).center(w // 2))
            print("Written in Python and made by @KennFatt :)".center(w // 2))
            print()

        else:
            print("\n\t\t\tTicTacToe {}\n\t\tWritten in Python and made by @KennFatt :)\n".format(
                Play.VERSION_STRING))
        input("Please tap [enter] to continue...")
    
    @staticmethod
    def clear() -> None:
        if os.name.startswith("posix"):
            os.system("clear")
        else:
            os.system("cls")

if __name__ == "__main__":
    Play.init()
