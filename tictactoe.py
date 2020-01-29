import random

class TicTacToe(object):

    CHARACTER_X_SYMBOL = "X"
    CHARACTER_O_SYMBOL = "O"

    # All the probability of winner's move.
    DATA_SET = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self, debugMode = False):
        print("Initialize the game...")
        self.__isDebugMode = debugMode

        # Initialize the board with empty value.
        # Board size: 3x3
        self.board = [[None] for i in range(0, 9)]

        # Records the moves of player x.
        self.__xMoves = []
        # Records the moves of player o.
        self.__oMoves = []

        # Random fill:
        if self.isDebugMode:
            for i in self.board:
                val = random.randint(0, 1)
                if val == 0:
                    i[0] = TicTacToe.CHARACTER_X_SYMBOL
                else:
                    i[0] = TicTacToe.CHARACTER_O_SYMBOL
        print("Game is now initialized!")

    def getBoardCross(self, cr: int) -> list:
        """Get board's cross value in a list. It only has two valid value for `cr` wich is `1` and `2`.
        Otherwise will raise a RuntimeError.

        1 is the cross side from `Top-left` to `Bottom-right`,

        2 is the cross side from `Bottom-left` to `Top-right`.
        
        Arguments:
            cr {int} -- The cross side.

        Raises:
            RuntimeError
        
        Returns:
            list -- The value of cross side.
        """
        if (cr != 1) or (cr != 2):
            raise RuntimeError("Invalid cross side was given: %d" % cr)

        if cr == 1:  # Top-Left -> Bottom-right
            return [self.board[n] for n in range(0, 9, 4)]
        else: # Top-right -> Bottom-left
            return [self.board[n] for n in range(2, 8, 2)]

    def getBoardColumn(self, col: int) -> list:
        """Get board's column value in a list.
        
        Arguments:
            col {int} -- Column index (1, 2, 3).

        Raises:
            RuntimeError
        
        Returns:
            list -- The value of column.
        """
        if (col < 1) or (col > 3):
            raise RuntimeError("Invalid column index was given: %d" % d)

        if col == 1:
            return [self.board[n] for n in range(0, 9, 3)]
        elif col == 2:
            return [self.board[n] for n in range(1, 9, 3)]
        else:
            return [self.board[n] for n in range(2, 9, 3)]

    def getBoardRow(self, row: int) -> list:
        """Get board's row value in a list.
        
        Arguments:
            row {int} -- Row index (1, 2, 3).
        
        Raises:
            RuntimeError
        
        Returns:
            list -- The value of row.
        """
        if (row < 1) or (row > 3):
            raise RuntimeError("Invalid row index was given: %d" % row)

        if row == 1:
            return [self.board[n] for n in range(0, 3)]
        elif row == 2:
            return [self.board[n] for n in range(3, 6)]
        else:
            return [self.board[n] for n in range(6, 9)]

    def insertCellValue(self, index: int, character: str) -> None:
        """Insert new value into specific cell.
        
        Arguments:
            index {int} -- Cell's index.
            character {str} -- Fill value.
        
        Raises:
            RuntimeError
        """
        if (index < 0) or (index > 8):
            raise RuntimeError("Given index exceed the limits: %d" % index)

        if (character != TicTacToe.CHARACTER_X_SYMBOL) and (character != TicTacToe.CHARACTER_O_SYMBOL):
            raise RuntimeError("Given value is not a valid character: %c" % character)

        if self.board[index][0] != None:
            raise RuntimeError("The index is already filled with value: %c" % self.board[index][0])

        self.board.insert(index, character)
    
    def saveMovesRecord(self, character: str, index: int) -> None:
        """Save each moves record into a list. The record would be used to get the winner.
        
        Arguments:
            character {str} -- Character type.
            index {int} -- Destination cell's index.
        
        Raises:
            RuntimeError
        """
        if (character != TicTacToe.CHARACTER_X_SYMBOL) and (character != TicTacToe.CHARACTER_O_SYMBOL):
            raise RuntimeError("Given value is not a valid character: %c" % character)

        if character == TicTacToe.CHARACTER_X_SYMBOL:
            self.__xMoves.append(index)
        else:
            self.__oMoves.append(index)

    def checkMoves(self, records: list, dataSet: list) -> bool:
        """Check player moves from the given `records`.
        
        Arguments:
            records {list} -- Player's move records.
            dataSet {list} -- All the probability of winner moves.
        
        Returns:
            bool -- True if there is matches move from the data set (Found the winner).
        """
        def isContain(item) -> bool:
            for x in records:
                if x == item:
                    return True
            return False

        for item in dataSet:
            if not isContain(item):
                return False
        return True

    @property
    def isDebugMode(self) -> bool:
        return self.__isDebugMode