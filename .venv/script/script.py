
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


class InputHandler:
    def __init__(self):
        self.user_inpt = None
        self.get_inpt("Enter position of the square and see the colour of the square : ")

    def get_inpt(self, prompt):
        try:
            self.user_inpt = input(prompt)
        except Exception as ex:
            print(ex)

    def input_validation(self):
        while True:
            # divide the use input in to two part as a number and letter
            try:
                number, letter = int(self.user_inpt[0]), self.user_inpt[-1]
            except Exception as ex:
                print("Unexpected format! please enter [number|letter] format like [1a]", ex.__class__)
                self.get_inpt("Enter new square : ")
                continue

            if len(self.user_inpt) != 2:
                print("Unexpected format! please enter [number|letter] format like [1a]")
                self.get_inpt("Enter new square : ")
                continue
            if number not in tuple(range(1, 9)):
                print("Unexpected number format! please enter valid number between 1 to 8")
                self.get_inpt("Enter valid square : ")
                continue
            if letter not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
                print("Unexpected letter! please enter valid letter between a to h")
                self.get_inpt("Enter valid square : ")
                continue

            return number, letter


inpt_handler = InputHandler()
number, letter = inpt_handler.input_validation()

traker = Tracker(number, letter)
print(f"[{letter}{number}] square is  a \"{traker.traker()}\" Square ")
