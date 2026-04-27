# AI Problem Solving Assignment

Repository name format required by assignment:

AI_ProblemSolving_<RegisterNumber>

This project contains two implemented AI problem-solving systems:

1. Interactive Game AI - Tic-Tac-Toe System
2. Sudoku Solver using CSP

Both problems are implemented using Python Flask with an interactive web interface.

---

## Folder Structure

AI_ProblemSolving_TicTacToe_Sudoku/
│
├── app.py
├── requirements.txt
├── README.md
│
├── problem1_tictactoe/
│   ├── __init__.py
│   └── logic.py
│
├── problem6_sudoku/
│   ├── __init__.py
│   └── logic.py
│
├── templates/
│   ├── index.html
│   ├── tictactoe.html
│   └── sudoku.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── tictactoe.js
        └── sudoku.js

---

## Problem 1: Interactive Game AI - Tic-Tac-Toe System

### Problem Description

A web-based Tic-Tac-Toe game where the user plays against an AI opponent.
User = X, AI = O.

### Algorithms Used

1. Minimax Algorithm
2. Alpha-Beta Pruning

### Sample Output

User Move: X at cell 1  
AI Move: O at cell 5  
Algorithm: Alpha-Beta Pruning  
Nodes Explored: 124  
Execution Time: 0.42 ms  

---

## Problem 6: Sudoku Solver using CSP

### Problem Description

Sudoku is a 9×9 puzzle solved using CSP.

### Algorithm Used

Constraint Satisfaction Problem with Backtracking.

---

## Execution Steps

1. Clone the repository

git clone https://github.com/your-username/AI_ProblemSolving_<RegisterNumber>.git

2. Create virtual environment

python -m venv venv

3. Activate

Windows: venv\Scripts\activate  
Mac/Linux: source venv/bin/activate  

4. Install requirements

pip install -r requirements.txt

5. Run

python app.py

6. Open in browser

http://127.0.0.1:5000
