# Tic-Tac-Toe with AI

## What is Tic-Tac-Toe?

Tic-Tac-Toe is a simple game where two players take turns marking a 3×3 grid. The first person to get three marks in a row (up, down, left, right, or diagonal) wins!

## What Did I Build?

I created three versions of this game with increasing AI difficulty:

1. **Two Players** - You vs Your Friend
2. **vs Random AI** - You vs Computer (Computer plays randomly)
3. **vs Smart AI** - You vs Computer (Computer plays perfectly)

---

## The Three Versions

### Version 1: Player vs Player
**File:** `Tic-Tac-Toe-2player.py`

Two human players play against each other. Good for learning how the game works!

**What it does:**
- Creates a 3×3 board
- Players take turns as X and O
- Checks if someone won
- Detects when the board is full (draw)
- Makes sure players enter valid moves

### Version 2: Player vs Random AI
**File:** `Tic-Tac-Tao-Random_Ai.py`

The computer plays randomly. You can usually beat it!

**What's new:**
- The computer picks a random empty spot
- You play as X, computer plays as O
- Good for testing the game and understanding how computers make moves

### Version 3: Player vs Smart AI (Unbeatable!)
**File:** `Tic-Tac-Toe-Minimax.py`

The computer plays perfectly using a smart algorithm. You can't beat it, but you might tie!

**What makes it smart:**
- The AI thinks about ALL possible future moves
- It picks the move that's best for itself
- It never makes a mistake
- This version teaches us real AI concepts

---

## How Does the Smart AI Work? (Minimax Algorithm)

### The Simple Explanation

Imagine you're playing the game and you think:
- "If I put X here, what will happen?"
- "Then the AI will put O there..."
- "Then I could put X there..."
- And so on...

The smart AI does exactly this! It checks EVERY possible path the game could take, then picks the path that's best for it.

### The Three Key Ideas

**1. Scoring**
- If AI wins → Score = +1 (good for AI)
- If you win → Score = -1 (bad for AI)
- If it's a draw → Score = 0 (neutral)

**2. The AI's Goal**
- The AI always tries to get a +1 score
- You always try to get a -1 score
- It assumes you play as smart as it does

**3. Working Backwards**
- The AI starts from the current board state
- For each empty spot, it imagines moving there
- It then imagines what you would do (you play to win)
- It then imagines what it would do next (it plays to win)
- This keeps going until the game ends
- Then it picks the move that gives it the best result

---
---

## Features

✅ Play two players against each other

✅ Play against a computer that picks random moves

✅ Play against a computer that plays perfectly

✅ The game checks for winners and draws

✅ The game prevents invalid moves

✅ Easy-to-read board display

---

## How to Run (Simple Steps)

### What You Need
- Python 3 installed on your computer

### Step 1: Open a Terminal/Command Prompt

On Windows: Press `Win + R`, type `cmd`, and hit Enter

### Step 2: Go to the Game Folder

```
cd Desktop\CodSoft\Task-2\ Tic-Tac-Toe
```

### Step 3: Pick a Version and Run It

**To play with a friend:**
```
python Tic-Tac-Toe-2player.py
```

**To play against random AI:**
```
python Tic-Tac-Toe-Random_Ai.py
```

**To play against smart AI:**
```
python Tic-Tac-Toe-Minimax.py
```

### Step 4: Play!

1. The game shows you the board positions (1-9)
2. Enter a number between 1-9 to place your mark
3. The computer plays automatically
4. Keep playing until someone wins or it's a draw

---

## The Board

The board has 9 positions numbered like this:

```
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```

When you play, just enter the number where you want to go!

---

## Folder Structure

```
Tic-Tac-Toe/
│
├── Tic-Tac-Toe-2player.py        (Two player game)
│
├── Tic-Tac-Toe-Random_Ai.py      (vs Random AI)
│
├── Tic-Tac-Toe-Minimax.py        (vs Smart AI)
│
└── README.md                      (This file)
```

---

## What I Learned

📚 **Python Basics** - How to write functions, loops, and lists

🎮 **Game Logic** - How to build a working game with rules and win conditions

🔄 **Recursion** - How functions can call themselves (used in the smart AI)

🤖 **AI** - How computers can make smart decisions

⚙️ **Minimax Algorithm** - A real algorithm used in game AI

💡 **Problem Solving** - Breaking big problems into smaller pieces

---

## Want to Try Something Harder?

Here are some ideas if you want to improve this project:

- **Difficulty Levels** - Make the AI easier or harder to beat
- **GUI** - Add a graphical interface with buttons instead of text
- **Score Tracking** - Keep track of wins and losses
- **Faster AI** - Optimize the minimax algorithm to make it run quicker
- **Undo Moves** - Let players take back their last move

---

## Reflection

This project was really interesting! I started with a basic game and added AI to it step by step. The coolest part was seeing the computer go from picking random moves to playing perfectly. 

The Minimax algorithm showed me that even complex AI isn't magic—it's just checking all possible options and picking the best one. Understanding this algorithm taught me a lot about how computers can play games and make decisions.

---

**Made during the CodSoft AI Internship** 🎓
