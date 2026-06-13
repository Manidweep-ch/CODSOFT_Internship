# Initialize the game board with 9 empty spaces (representing a 3x3 grid)
board = [" "] * 9


def printboard():
    """Display the current state of the Tic-Tac-Toe board."""
    print("|---|---|---|")
    for i in range(3):
        print(end="| ")
        for j in range(3):
            print(board[i*3+j], end=" | ")
        print("\n|---|---|---|")

# All possible winning combinations (rows, columns, and diagonals)
winning_combinations = [
    [0, 1, 2],      # Top row
    [3, 4, 5],      # Middle row
    [6, 7, 8],      # Bottom row
    [0, 3, 6],      # Left column
    [1, 4, 7],      # Middle column
    [2, 5, 8],      # Right column
    [0, 4, 8],      # Diagonal (top-left to bottom-right)
    [2, 4, 6]       # Diagonal (top-right to bottom-left)
]


def checkWinning():
    """Check if the current board state has a winning combination.
    
    Returns:
        The symbol ("X" or "O") if that player has won, None otherwise.
    """
    for combo in winning_combinations:
        # Check if all three positions in a winning combination have the same symbol
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None


def is_board_full():
    """Check if the board is completely filled with no empty spaces.
    
    Returns:
        True if board is full, False if there are empty spaces.
    """
    return " " not in board

# Score values for the minimax algorithm
# O (AI) winning is best: +1, X (human) winning is worst: -1, Draw/Tie: 0
Scores = {"O": 1, "tie": 0, "X": -1}


def minimax(ai_turn, depth):
    """Recursively evaluate all possible game states to find the best score.
    
    This is the core of the AI. It explores the entire game tree and scores
    each outcome assuming both players play optimally.
    
    Args:
        ai_turn: Boolean indicating if it's the AI's turn (True) or human's (False)
        depth: Current depth in the game tree (used for optimization)
    
    Returns:
        A list [score, depth] where score represents the outcome and depth is used
        to prefer faster wins/losses
    """
    # Check if the game has already been won or drawn
    winner = checkWinning()
    if winner is not None:
        return [Scores[winner], depth]
    if is_board_full():
        return [Scores["tie"], depth]
    
    # Minimizing player's turn (human playing as X)
    # Try to minimize the score (get the worst outcome for AI)
    if ai_turn == False:
        best_score = [float('inf'), depth]
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, depth + 1)
                # Keep track of the minimum score
                if score[0] < best_score[0]:
                    best_score = score
                # If scores are equal, prefer shallower depth (faster game)
                elif score[0] == best_score[0]:
                    if score[1] < best_score[1]:
                        best_score = score
                board[i] = " "
        return best_score
    
    # Maximizing player's turn (AI playing as O)
    # Try to maximize the score (get the best outcome for AI)
    best_score = [float('-inf'), depth]
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, depth + 1)
            # Keep track of the maximum score
            if score[0] > best_score[0]:
                best_score = score
            # If scores are equal, prefer shallower depth (faster game)
            elif score[0] == best_score[0]:
                if score[1] < best_score[1]:
                    best_score = score
            board[i] = " "
    return best_score


def best_move():
    """Find the best move for the AI using the minimax algorithm.
    
    Evaluates each possible move and returns the position that leads to
    the best outcome for the AI.
    
    Returns:
        The index (0-8) of the best move to make.
    """
    best_Score = [float('-inf'), 0]
    best_Move = None
    
    # Try each empty position and evaluate the resulting board state
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, 0)
            # Keep track of the best move found so far
            if score[0] > best_Score[0]:
                best_Score = score
                best_Move = i
            # If scores are equal, prefer move that leads to faster win/loss
            elif score[0] == best_Score[0]:
                if score[1] < best_Score[1]:
                    best_Score = score
                    best_Move = i
            board[i] = " "
    
    return best_Move



def Ai_turn():
    """Make the AI's move by finding and playing the best move using minimax."""
    move = best_move()
    board[move] = "O"


def verify_status():
    """Check if the game has ended (win or draw).
    
    Returns:
        True if the game has ended, False otherwise.
    """
    winner = checkWinning()
    if winner:
        printboard()
        print(f"{winner} has won the game")
        return True
    elif is_board_full():
        printboard()
        print("Its a draw")
        return True
    
    return False

def play_game():
    """Main game loop for Human vs Minimax AI Tic-Tac-Toe."""
    # Display welcome message and board position guide
    print("Welcome to Tic-Tac-Toe game")
    print("Position of the board are:")
    print()
    print("|---|---|---|")
    for i in range(3):
        print(end="| ")
        for j in range(1, 4):
            print(3*i+j, end=" | ")
        print("\n|---|---|---|")
    print("Start the Game")
    
    # Main game loop - continues until someone wins or it's a draw
    while True:
        # Display current board state
        printboard()
        
        # Get player input for their move
        move = input(f"Player X Enter position (1-9): ")
        
        # Validate that input is a number
        if not move.isdigit():
            print("Enter a number.")
            continue

        # Convert to integer
        move = int(move)

        # Validate that move is within range 1-9
        if move < 1 or move > 9:
            print("Position must be between 1 and 9.")
            continue

        # Check if the chosen position is already occupied
        if board[move - 1] != " ":
            print("Position already occupied.")
            continue
        
        # Place the player's symbol on the board (convert from 1-9 to 0-8 index)
        board[move - 1] = "X"
        
        # Check if the game has ended
        if verify_status():
            break
        
        # AI makes its move using minimax algorithm
        Ai_turn()
        
        # Check if the game has ended
        if verify_status():
            break


# Run the game when the script is executed
play_game()