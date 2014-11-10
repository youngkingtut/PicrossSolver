__author__ = "Tristan Storz tristanstorz@gmail.com"
__email__ = "tristanstorz@gmail.com"
__status__ = "Development"
__version__ = "0.1.1"


class PicrossPuzzle(object):
    """
        Picross Puzzle contains all methods for creating and
        Finding hints for a given puzzle. More puzzle formats
        will be added at a later time. For now only a simple
        2d square array is considered.
    """
    def __init__(self, puzzle):
        """
            Create class by inputting a 2 dimensional square list.
            verify_puzzle is called to check for correct input.
        """
        self.puzzle = puzzle
        self.size = len(self.puzzle)

        try:
            self.verify_puzzle(self.puzzle)
        except NameError, error:
            self.puzzle = [[1, 1], [1, 1]]
            print error

        self.set_puzzle_hints(self.puzzle)

    def verify_puzzle(self, puzzle):
        """
            Simple verfication. Throws a defined NameError if the
            input list does not have equal columns and rows
        """
        for row in self.puzzle:
            if len(row) != self.size:
                raise NameError("Invalid puzzle, setting to simple case")

    def set_puzzle_hints(self, puzzle):
        """
            FInd hints for given puzzle. Hints are stored in
            self.vertical_hints and self.horizontal_hints
        """
        transposed_puzzle = [[self.puzzle[y][x] for y in range(len(self.puzzle))] for x in range(len(self.puzzle[0]))]
        self.horizontal_hints = self.get_horizontal_hints(self.puzzle)
        self.vertical_hints = self.get_horizontal_hints(transposed_puzzle)

    def get_horizontal_hints(self, puzzle):
        """
            Returns list of vertical hints
        """
        horizontal_hints = []

        for row_index, row in enumerate(puzzle):
            temp_counter = 0
            horizontal_hints.append([])

            for column_index, column_val in enumerate(row):
                if column_val > 0:
                    temp_counter += 1

                if column_val == 0 and temp_counter > 0:
                    horizontal_hints[row_index].append(temp_counter)
                    temp_counter = 0

                if column_index == self.size - 1:
                    if column_val > 0:
                        horizontal_hints[row_index].append(temp_counter)
                        temp_counter = 0
        return horizontal_hints
