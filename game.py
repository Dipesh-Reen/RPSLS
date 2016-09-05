import random
import argparse


class Game(object):
    """ Instance of a single RPSLS Game """
    #  Store a predefined order that is important as every 'x' defeats only 'x+1' and 'x+2'
    option_sequence = 'Rock', 'Scissors', 'Lizard', 'Paper', 'Spock'
    # Keep track of game scores for multiple game matches
    game_series = {"user" : 0, "computer" : 0}
    def __init__(self, game_no):
        self.game_no = game_no
        print ("\nGame", self.game_no)

    def __handle_specific_inputs(self):
        """ Handle exit condition and faulty input"""
        # Exit condition
        if self.user_option == '0':
            raise SystemExit
        # Faulty input
        try:
            # .title() standardizes the user input format
            # .index() finds the index of user input in the option sequence tuple
            self.user_option_index = self.option_sequence.index(self.user_option.title())
            return True
        except ValueError:
            print ("Invalid input. Try again")
            return False

    def get_choices(self):
        """ Get users choice and randomly generated computer choice """
        valid_input = False
        while not valid_input:
            self.user_option = input("Enter your choice(0 to quit): ")
            valid_input = self.__handle_specific_inputs()
        self.comp_option_index = random.randint(0,4)
        print ("The computer chose", self.option_sequence[self.comp_option_index])

    def get_match_result(self):
        """ Compare the user's and computer's choices to decide the match winner """
        # Get the relative positions of the choices in the predefined order
        self.match_result = (self.user_option_index - self.comp_option_index) % 5
        if self.match_result == 0:
            print ("It's a tie!!")
        elif self.match_result > 2:
            print ("You won!!")
            self.game_series['user'] += 1
        else:
            print ("Computer won!!")
            self.game_series['computer'] += 1

    @classmethod
    def get_series_progress(cls):
        print ("You : {0}  ::  Computer : {1}".format(cls.game_series['user'], cls.game_series['computer']))


def rules():
    # Rules straight out of 'Big Bang Theory'
    return """The rules for Rock Paper Scissor Lizard Spock are as follows :

    Scissor cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissor
    Scissor decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vapourizes Rock
    and as it always has...
    Rock crushes Scissors

        - Dr. Sheldon Cooper
    """

def begin_text_mode():
    """ Textual Interaction for the user """
    print (rules())
    try:
        i = 0
        while True:
            i += 1
            game = Game(i)
            game.get_choices()
            game.get_match_result()
            game.get_series_progress()
    except Exception as err:
        print ("Unknown Error [%s]" % err)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--voice", help="Use voice as the mode of interaction", action="store_true")
    if parser.parse_args().voice:
        print ("Voice controls under development")     # needs implementation
    else:
        begin_text_mode()

if __name__ == '__main__':
    main()
