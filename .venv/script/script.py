
class Tracker:
    def __init__(self, number, letter):
        # initialize chess board has specific number and character position list
        self.initial_numbers = tuple(range(1, 9))
        self.initial_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        # get user chosen number and letter from board
        self.number = number
        # store letter as a numerical value
        #   take the letter position using indexing of inside the tuple
        self.letter = self.initial_letter.index(letter) + 1  # letter index increase by one to match initial numbers


traker = Tracker(2, "c")

# just testing purpose
print(traker.letter)
