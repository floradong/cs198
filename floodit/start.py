from floodit import *

def start():
	"""
	This initial script implements one of the features -- 
	it asks the player what board size they would want to play. 
	The larger the board, the more difficult the game. 
	After generating the board and updating display, 
	the "check color 1, 1, item of coordinates (1,1)" 
	block reports the squares that are adjecent to (1,1) that have the same "item" 
	-- in this case, number -- as (1,1). 
	"""
	global corList
	check_color(1, 1, item_of_coordinates(1, 1))
	update_display()
