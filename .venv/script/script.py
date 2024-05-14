
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

    # create square color tracker function
    def traker(self):
        # if user number and letter is odd or even number then chess board square must be black
        if (self.number % 2 == 1 and self.letter % 2 == 1) or (self.number % 2 == 0 and self.letter % 2 == 0):
            return "Black"
        # if it's not so square must be white
        else:
            return "White"


traker = Tracker(8, "h")

# just testing purpose
print(traker.traker())
