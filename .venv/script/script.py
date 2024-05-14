
class Tracker:
    def __init__(self, number, letter):
        # initialize chess board has specific number and character position list
        self.initial_numbers = tuple(range(1, 9))
        self.initial_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        # get user chosen number and letter from board
        self.number = number
        self.letter = letter


traker = Tracker(2, "c")
