"""GAME: FLOOD IT

The objective of the game is to fill a board completely with 
one number in the given amount of moves. Only the squares of 
the same number adjacent to the top left corner (as we note, 
coordinate (1,1) ) will change into the desired number
the player wants. """

from board import *
import math

Size = input("Welcome to Flood It! Choose your size from 3 to 14. ")
Counter = 0
Game_Over = False
You_Win = False
Moves = math.ceil((1.5 * Size) + (Size - 3) / 2)
corList = []
board = []

def create_board_of_length(n):
	"""
	Creates a board that is whatever the user input as their chosen size. 
	"""
	global Size, board
	numbers = range(1, 7)
	for _ in range(n):
		row = []
		for _ in range(n):
			row.append(random.choice(numbers))
		board.append(row)
	return board

Board = create_board_of_length(Size)

def update_display():
	global board
	"""
	Prints square board that is Size * Size.

	Board size 6 might look like: 

	[6, 1, 2, 1, 2, 2]
	[1, 5, 5, 3, 5, 6]
	[2, 3, 6, 6, 3, 4]
	[3, 6, 3, 5, 3, 4]
	[1, 6, 6, 3, 6, 5]
	[4, 1, 1, 3, 3, 1]
	"""

 	for row in board:
 		print(row)

def item_of_coordinates(row, column):
	"""
	Returns the item that is at the given 
	coordinate. 

	If the number at (1, 1) is 6, it would 
	return 6.
	"""
 	board_row = board[row-1]
 	board_column = board_row[column-1]
 	return board_column

def coordinates(row, column):
	"""
	Creates a list form of the coordinates. 

	coordinates(1, 1) could be [1, 1]
	"""
	return [row, column]

# def item_a_b_board(row, column, board):

# 	x = board[column]
# 	return x[row]

def change(row, column):
	"""
	Changes all the cells of the same number that are adjacent to (1,1)
	to the same number as the cell that you've selected.

	If (1, 2) has a 6, change(1, 4) would change all the cells with the same
	number that are adjacent to (1, 1) to a 3. 

	Current board:

	[6, 6, 6, 1, 2, 2]
	[6, 6, 6, 3, 5, 6]
	[6, 3, 6, 6, 3, 4]
	[3, 6, 3, 5, 3, 4]
	[1, 6, 6, 3, 6, 5]
	[4, 1, 1, 3, 3, 1]

	change(3, 2) would result in: 

	[3, 3, 3, 1, 2, 2]
	[3, 3, 3, 3, 5, 6]
	[3, 3, 3, 3, 3, 4]
	[3, 6, 3, 5, 3, 4]
	[1, 6, 6, 3, 6, 5]
	[4, 1, 1, 3, 3, 1]

	"""
	global Counter
	global corList
	Counter += 1
	if row > 1 or column > 1: 
		print("Invalid move. Try again.")
	for item in range(len(corList)):
		a = corList[item]
		x = a[0]
		y = a[1]
		item = item_of_coordinates(x, y) 
		item = item_of_coordinates(row, column)
		Board[x - 1][y - 1] = item
	update_display()
	corList = []
	check_color(1, 1, item_of_coordinates(1, 1))
	print ("You have ") + str(Moves - Counter) +(" moves left.")
	finish_move()

def check_color(x, y, number):
	"""
	Creates a list of lists that finds the coordinates adjacent to (1, 1)
	that have the same number as (1, 1).

	Current Board: 

	[3, 3, 3, 1, 2, 2]
	[3, 3, 3, 3, 5, 6]
	[3, 3, 3, 3, 3, 4]
	[3, 6, 3, 5, 3, 4]
	[1, 6, 6, 3, 6, 5]
	[4, 1, 1, 3, 3, 1]

	check_color(1, 1, 3) would result in a list of lists of all the
	coordinates adjacent to (1, 1) that are 3. 

	[[1, 1], [2, 1], [3, 1], [4, 1], [3, 2], [3, 3], [4, 3], 
	[3, 4], [3, 5], [4, 5], [2, 4], [2, 3], [1, 3], [1, 2], [2, 2]]
	"""
 
	global corList
	if item_of_coordinates(x, y) == number:
		if coordinates(x, y) not in corList:
			corList.append(coordinates(x, y))
		if coordinates(x + 1, y) not in corList:
			if x < Size:
				check_color(x + 1, y, number)
		if coordinates(x, y + 1) not in corList:
			if y < Size:
				check_color(x, y + 1, number)
		if coordinates(x - 1, y) not in corList:
			if (x-1 != 0):
				if (x <= Size):
					check_color(x - 1, y, number)
		if coordinates(x, y - 1) not in corList:
			if (y-1 != 0):
				if (y <= Size):
					check_color(x, y - 1, number)
	return corList

def finish_move():
	"""
	Determines if the game is over or not.
	"""
	global Game_Over
	global You_Win
	if ((Moves - Counter) <= 0) and ((len(check_color(1, 1, item_of_coordinates(1, 1)))) != Size*Size):
		Game_Over == True
		print("Sorry. Game over. You lose.")
	if ((Moves - Counter) >= 0) and ((len(check_color(1, 1, item_of_coordinates(1, 1)))) == Size*Size):
		Game_Over == False
		You_Win == True
		print("YAY! YOU WIN!")









