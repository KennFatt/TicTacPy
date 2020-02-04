from tictactoe import TicTacToe
import os

class Play(object):
    
    VERSION_STRING = "v1.0"

    @staticmethod
    def init():
        # Optionally clear the screen.
        Play.clear()

        # Show the welcome banner.
        Play.show_banner()

        # Initialize the game backend.
        game = TicTacToe()

        # Let the X character to turn first.
        last_move = TicTacToe.CHARACTER_X_SYMBOL

        # Game loop
        while True:
            # Clear the screen on every (hopefully, frame).
            Play.clear()

            # Render (or shows) the board.
            Play.render_board(game)

            # Getting the winner.
            # This method is used to prevent bad experience if we had to
            # call `player_moves` in the beginning.
            winner = game.get_winner()

            # Check for the winner existance.
            if len(winner) > 0:
                print("Game has been ended!")
                print("The winner is Player {}".format(winner))
                break
            # A condition where nobody (everybody) won the game. In the other hand, tie is occured.
            elif len(game.get_player_moves_record(TicTacToe.CHARACTER_X_SYMBOL)) + len(game.get_player_moves_record(TicTacToe.CHARACTER_O_SYMBOL)) == 9:
                print("Game tied!")
                break

            # Check and validate all player's move.
            Play.player_moves(game, last_move)

            # Swap the turn.
            last_move = TicTacToe.CHARACTER_O_SYMBOL if last_move == TicTacToe.CHARACTER_X_SYMBOL else TicTacToe.CHARACTER_X_SYMBOL

    @staticmethod
    def player_moves(game: TicTacToe, character: str):
        while True:
            # Prompt the player to select the cell.
            selected_cell = (Play.read_moves(character)) - 1

            # Check if the selected cell is taken by themselves or their opponent.
            if game.is_cell_taken(selected_cell):
                print("The cell that you selected is taken!")
                print("Please insert another cell.")
                continue

            # In this state, the cell is empty and ready to be inserted with a new value.

            # Inserting the cell with value: character (X or O).
            game.insert_cell_value(selected_cell, character)

            # Save the player's record into its list.
            game.save_moves_record(selected_cell, character)

            # Get the player's move record.
            player_moves = game.get_player_moves_record(character)

            # Whenever the record has reach 3 or more element
            # it is a valid moves to win the game.
            # This method is kinda hack, because the function `checkMoves` is so expensive.
            if len(player_moves) >= 3:
                # If player's move matches with the Data Set
                # it should stop the game by flagging the winner.
                if game.check_moves(player_moves):
                    game.set_winner(character)
            break

    @staticmethod
    def read_moves(character: str) -> int:
        while True:
            buffer = input("Player {} turns, please input cell number [1..9]: ".format(character))
            if buffer.isnumeric() and len(buffer) == 1:
                return int(buffer)

    @staticmethod
    def render_board(game: TicTacToe) -> None:
        for i in range(1, 4):
            c1, c2, c3 = list(map(lambda lst: "_" if lst[0] == None else lst[0], game.get_board_row(i)))
            print("\t{}\t|\t{}\t|\t{}\t".format(c1, c2, c3))
    
    @staticmethod
    def show_banner() -> None:
        if os.name.startswith("posix"):
            stty_buff = os.popen("stty size", "r").read().split()
            h, w = int(stty_buff[0]), int(stty_buff[1])

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
