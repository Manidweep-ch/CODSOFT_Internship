import random

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
        True if any player has won, False otherwise.
    """
    for combo in winning_combinations:
        # Check if all three positions in a winning combination have the same symbol
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False


def is_board_full():
    """Check if the board is completely filled with no empty spaces.
    
    Returns:
        True if board is full, False if there are empty spaces.
    """
    return " " not in board


def getAvailable_moves():
    """Get a list of all empty positions on the board.
    
    Returns:
        A list of indices (0-8) that are currently empty.
    """
    available_positions = []
    for i in range(9):
        if board[i] == " ":
            available_positions.append(i)
    return available_positions


def Ai_turn():
    """Make the AI's move by randomly selecting an available position."""
    available = getAvailable_moves()
    choice = random.choice(available)
    board[choice] = "O"

def verify_status(current_player):
    """Check if the game has ended (win or draw).
    
    Args:
        current_player: The symbol of the player who just moved ("X" or "O").
    
    Returns:
        True if the game has ended, False otherwise.
    """
    if checkWinning():
        printboard()
        print(f"{current_player} has won the game")
        return True
    elif is_board_full():
        printboard()
        print("Its a draw")
        return True
    return False

def play_game():
    """Main game loop for Human vs Random AI Tic-Tac-Toe."""
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
        
        # Check if the player has won
        if verify_status("X"):
            break
        
        # AI makes its move
        Ai_turn()
        
        # Check if the AI has won
        if verify_status("O"):
            break


# Run the game when the script is executed
play_game()