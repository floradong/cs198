def children(position):
	return [do_move(position,move) for move in generate_moves(position)]

def solve(position):
	"return value of position through game tree search"
	if primitive(position) != UNKNOWN:
		return primitive(position)
	else:
		values = [solve(child) for child in children(position)]
		if LOSE in values:
			return WIN
		elif TIE in values:
			return TIE
		else:
			return LOSE

for p in range(10,-1,-1):
	print(str(p) + " has value " + solve(p))
