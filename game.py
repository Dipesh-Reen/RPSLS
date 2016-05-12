import random

# GLOBAL VARIABLES
#  Store a predefined order that is important as every 'x' defeats only 'x+1' and 'x+2'
option_sequence = 'Rock', 'Scissor', 'Lizzard', 'Paper', 'Spock'
# Keep track of game scores for multiple game matches
game_series = {"user" : 0, "computer" : 0}

class Game(object):
	""" Instance of a single RPSLS Game """

	def __init__(self, game_no):
		self.game_no = game_no + 1
		print ("\nGame", self.game_no)

	def __handle_specific_inputs(self):
		""" Handle exit condition and faulty input"""
		# Exit condition
		if self.user_option == '0':
			raise SystemExit
		# Fau;ty input
		try:
			# .title() standardizes the user input format
			# .index() finds the index of user input in the option sequence tuple
			self.user_option_index = option_sequence.index(self.user_option.title())
			return False
		except:
			print ("Wrong input. Try again")
			return True
			
	def get_choices(self):
		""" Get users choice and randomly generated computer choice """
		self.user_option = input("Enter your choice : ")
		chk_input_for_error = self.__handle_specific_inputs()
		if chk_input_for_error:
			self.get_choices()
		self.comp_option_index = random.randint(0,4)
		print ("The computer chose", option_sequence[self.comp_option_index])

	def get_match_result(self):
		""" Compare the user's and computer's choices to decide the match winner """
		global game_series
		# Get the relative positions of the choices in the predefined order
		self.match_result = (self.user_option_index - self.comp_option_index) % 5
		if self.match_result == 0:
			print ("It's a tie!!")
		elif self.match_result > 2:
			print ("You won!!")
			game_series['user'] += 1
		else:
			print ("Computer won!!")
			game_series['computer'] += 1

	def get_series_progress(self):
		print ("You : {0}  ::  Computer : {1}".format(game_series['user'], game_series['computer']))
		

def rules():
	# Rules straight out of 'Big Bang Theory'
	return """The rules for Rock Paper Scissor Lizzard Spock are as follows : 

	Scissor cuts Paper
	Paper covers Rock
	Rock crushes Lizzard
	Lizzard poisons Spock
	Spock smashes Scissor
	Scissor decapitates Lizzard
	Lizzard eats Paper
	Paper disproves Spock
	Spock vapourizes Rock
	and as it always has...
	Rock crushes Scissors

		- Dr. Sheldon Cooper
	"""

def main():
	print (rules())
	try:
		no_of_games = int(input("How many games do you want to play? : "))
		if no_of_games != 0:
			print ("Enter 0 to quit")
		for i in range(no_of_games):
			game = Game(i)
			game.get_choices()
			game.get_match_result()
			game.get_series_progress()
	except ValueError:
		print ("That wasn't a valid number. Try again...")
		
if __name__ == '__main__':
	main()