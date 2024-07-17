
# Red Blue Nim

## Problem statement

Build an agent to play Red-Blue Nim (standard and misère) against a human player. The game has two piles of marbles (red and blue). Each turn, a player removes one or two marbles from a pile. In the standard version, a player loses if either pile is empty on their turn. In the misère version, they win. The score is based on remaining marbles: 2 points per red, 3 per blue. The program, red_blue_nim.py, is run with red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>. <version> can be standard (default) or misere. <first-player> can be computer (default) or human. <depth> is optional. The computer uses Minimax with Alpha-Beta Pruning to decide moves, with different priorities for each version. The game alternates turns until a pile is empty, then displays the winner and their score.

## File description

red_blue_nim_no_depth.py - Has the implementation for minmax algo with alpha beta pruning, but NOT 
with depth limited implantation. It accepts 3 arguments, namely in order: red, blue, player.

red_blue_nim.py - Has the implementation for minmax algo with alpha beta pruning, 
and ALSO with depth limited implantation. It accepts 4 arguments, namely in order: red, blue, 
player, depth.

## Code structure

- check_win: Returns true if either of pile is empty.
- check_points: Returns the score of the player based on the marble count.
- next_move: Appends all possible moves from a given pile to new_pile.
- minmax_ab: Performs the minmax algorithm with alpha beta pruning for the given pile structure and player identity.
- human_play: Gets human input when it's his/her turn and modifies the pile structure based on the input obtained.
- computer_play: Following to human's turn, it calls for the minmax algo, and selects the best move to make and modifies the pile structure accordingly.
- main: Obtains the input from the terminal and initiates the pile structure and calls in for the appropriate player based on the input obtained.

## Built With

[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
## How to run the code?

- As stated above, red_blue_nim_no_depth.py accepts 3 arguments and red_blue_nim.py accepts 4 arguments(as it works on depth limited search)
- If player is not defined in either of the code, it would set as computer as the first player by default. 


## Support

For support, email thangarajarvind@gmail.com or DM via [@Arvind Thangaraj](https://www.linkedin.com/in/arvind-thangaraj/)

