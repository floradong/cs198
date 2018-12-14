Flood-It

The Manual

The complete version with GUI graphics is (here). I personally coded the python version after learning python while a friend using numbers instead of colors. Additionally, I coded it in a visual programming language called Snap! (based off of Scratch) as part of a project in an introductory computer science course my first semester at UC Berkeley.  The .xml file is located in the folder. You may open snap.berkeley.edu and drag the .xml file run in. A separate README is provided for that. 

Objective: The objective of the game is to fill a board completely with one number in the given amount of moves. Only the squares of the same color adjacent to the top left corner (as we note, coordinate (1,1) ) will change numbers into the desired number the player wants. 

How: To change the squares’ colors, the player must input the coordinates of the square that is the desired number they would want to change the board to using change(x, y), with x being the row and y being the column.  Once entered, all the squares of the same number adjacent to the top left square (1,1) will turn into the desired number. 

To start the game, the player run start.py, in which a welcome message and a question will appear, asking about the board size. Players may choose their difficulty based on the size of the board they want to play with. From a scale of 2 to 14, players may input their desired board size to get their desired difficulty. For example, if a player wants a slightly hard board and inputs 10, a 10x10 board will appear. 

If the player successfully changes all the squares in the entire board to the same number within the given amount of steps, the screen will display that the player have won. However, if the player ran out of moves and have already used up all their moves before the entire board is changed to the same color, the screen will display that the player has lost and that the game is over. 




