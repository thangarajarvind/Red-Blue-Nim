Programming language used: Python (3.10.2)

CODE STRUCTURE:

DEPTH LIMITED SEARCH is implemented in a separate code file.

There are 2 files, red_blue_nim_no_depth.py (and) red_blue_nim.py

red_blue_nim_no_depth.py - Has the implementation for minmax algo with alpha beta pruning, but NOT 
with depth limited implantation. It accepts 3 arguments, namely in order: red, blue, player.

red_blue_nim.py - Has the implementation for minmax algo with alpha beta pruning, 
and ALSO with depth limited implantation. It accepts 4 arguments, namely in order: red, blue, 
player, depth.

Description about the logic used for depth limited minmax is explained in the other document .

The code structure has multiple function blocks, who's their description is given below:

check_win: Returns true if either of pile is empty.
check_points: Returns the score of the player based on the marble count.
next_move: Appends all possible moves from a given pile to new_pile.
minmax_ab: Performs the minmax algorithm with alpha beta pruning for the given pile 
structure and player identity.
human_play: Gets human input when it's his/her turn and modifies the pile structure based on 
the input obtained.
computer_play: Following to human's turn, it calls for the minmax algo, and selects the best 
move to make and modifies the pile structure accordingly.
main: Obtains the input from the terminal and initiates the pile structure and calls in for the 
appropriate player based on the input obtained.

HOW TO RUN THE CODE:

As stated above, red_blue_nim_no_depth.py accepts 3 arguments and red_blue_nim.py accepts 4 arguments(as it works on depth limited search)
If player is not defined in either of the code, it would set as computer as the first player by default. 
