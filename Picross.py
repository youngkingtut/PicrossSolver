def column(array, i):
    return [row[i] for row in array]


class PicrossPuzzle:
    """
        Picross Puzzle contains all methods for creating and
        Translating a puzzle from hints to solution. Intialized
        with a equal size 2d array (initially).
    """
    def __init__(self, puzzle):
        try:
            self.verify_puzzle(puzzle)
        except NameError, error:
            puzzle = [1]
            print error

        self.solution  = puzzle
        self.size = len(puzzle)
        self.calculate_hints(puzzle)

    def verify_puzzle( self, puzzle ):
        for row in puzzle:
            if len(row) != len( puzzle ):
                raise NameError("Invalid puzzle, setting puzzle to simple case")

    def calculate_hints( self, puzzle ):
        vertical_hints = []
        horizontal_hints = []
        temp_counter = 0

        for row_index, row in enumerate( puzzle ):
            temp_counter = 0
            horizontal_hints.append([])

            for column_index, column_val in enumerate( row ):
                if column_val > 0:
                    temp_counter += 1 ;

                if column_val == 0 and temp_counter > 0:
                    horizontal_hints[row_index].append(temp_counter)
                    temp_counter = 0

                if column_index == self.size - 1:
                    if column_val > 0:
                        horizontal_hints[row_index].append(temp_counter)
                        temp_counter = 0

            if len(horizontal_hints[row_index]) == 0:
                horizontal_hints[row_index].append(0)

        for column_index in range(len(puzzle)):
            temp_counter = 0
            vertical_hints.append([])
            
            for row_index, row_val in enumerate([row[column_index] for row in puzzle]):

                if row_val > 0:
                    temp_counter += 1 ;

                if row_val == 0 and temp_counter > 0:
                    vertical_hints[column_index].append(temp_counter)
                    temp_counter = 0

                if row_index == self.size - 1:
                    if row_val > 0:
                        vertical_hints[column_index].append(temp_counter)
                        temp_counter = 0

        self.vertical_hints = vertical_hints
        self.horizontal_hints = horizontal_hints






some = PicrossPuzzle([[1,0,1],
                      [0,1,0],
                      [1,1,1]])
print some.solution
print some.horizontal_hints
print some.vertical_hints

