# AI-MinesSweeper 
Initializes the game:
	•	Creates a blank board of specified size.
	•	Sets up data structures for revealed cells and mine positions.
	•	Randomly generates the mines via generate_board.
generate_board(self)

Randomly places the specified number of mines on the board, ensuring no duplicates.
count_adjacent_mines(self, x, y)

Counts the number of mines adjacent to cell (x, y) by checking all 8 surrounding cells.
reveal(self, x, y)

Reveals the cell at (x, y):
	•	If it’s a mine, prints a game-over message and returns False.
	•	Otherwise, updates the board with the count of adjacent mines and returns True.

 Prints the current state of the board:
	•	Revealed cells show their adjacent mine count.
	•	Unrevealed cells show as " . ".
Main loop that drives the game:
	•	Repeatedly prints the board, selects the next move using the AI, and reveals the selected cell.
	•	Ends if a mine is hit or there are no more safe moves.
