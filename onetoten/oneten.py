WIN = "win" #winning
LOSE = "lose" #losing
TIE = "tie" #tied
UNKNOWN = "unknown" #don't know who has won yet

def primitive(position):
	if position == 10:
		return LOSE
	else:
		return UNKNOWN
	#	return LOSE if position == 0 or else UNKNOWN bc game hasn't ended yet

def generate_moves(position):
	#returns a list of possible moves
	# if you're the first to go, you take one to ensure your opponent is in losing pos
	if position == 1:
		return [1]
	else:
		return [1,2]

def do_move(position, move):
	# do the move given the position and move
	return position + move
