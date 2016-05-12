import random

class Game(object):
	"""docstring for Game"""

	def __init__(self, game_no):
		self.game_no = game_no
		print ("Game", self.game_no)

	def __option_sequence(self):
		""" Return a tuple of possible options """
		#  The order is important as every 'x' defeats only 'x+1' and 'x+2'
		return 'Rock', 'Scissor', 'Lizzard', 'Paper', 'Spock'

	def get_choices(self):
		""" get users choice and randomly generated computr choice """
		self.user_option = input("Enter your choice : ")
		if self.user_option == 0:
			# exit()
		self.comp_option = random.randint(0,4)

	def compare_choices(self):
		pass

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
	no_of_games = int(input("How many games do you want to play? : "))
	if no_of_games != 0:
		print ("Enter 0 to quit")
	for i in range(no_of_games):
		game = Game(i)
		game.get_choices()
		game.compare_choices()

	

if __name__ == '__main__':
	main()