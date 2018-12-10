WIN = "win" #You win
LOSE = "lose" #You lose
TIE = "tie" #You tied
UNKNOWN = "unknown" #The hasn't ended yet and you don't know who is going to win

def primitive(position):
	# "lose" if end of game, otherwise UNKNOWN
	if position == 10:
		return LOSE
	else:
		return UNKNOWN
	#	return LOSE if position == 0 else UNKNOWN

def generate_moves(position):
	# "return a tuple of possible moves"
	#If your position is one, you only take one to ensure your opponent is already in
	#the losing position. 
	if position == 1:
		return (1,)
	else:
		return (1,2)

def do_move(position, move):
	# "given position and move, do move on position"
	return position + move
