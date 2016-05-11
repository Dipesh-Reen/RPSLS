def generate_option_sequence():
	# THe order is important as every 'x' defeats only 'x+1' and 'x+2'
	return 'Rock', 'Scissor', 'Lizzard', 'Paper', 'Spock'

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
	

if __name__ == '__main__':
	main()