# Sudoku Game

Welcome to the **Sudoku Game** project! This web-based game generates endless Sudoku puzzles for players to solve, complete with helpful features like input validation and solution highlights.

## Features

- **Infinite Sudoku Puzzles**: Generates a new, unique Sudoku puzzle every time you click the "Generate Sudoku" button.
- **Input Validation**: Only allows numbers between 1 and 9 in the Sudoku grid, preventing invalid numbers.
- **Mistake Notification**: Alerts the user if there are mistakes in their solution after clicking the "Check Sudoku" button.
- **Solution Button**: The "Show Solution" button only appears if the user has mistakes in their solution, offering them the correct solution.
- **Responsive Design**: Sudoku grid and buttons are centered for a clean and tidy UI.
- **Dark Mode**: Toggle between light and dark themes for a better gaming experience.

## Screenshots

![{9B505917-8E4C-4954-925A-42C7123A9927}](https://github.com/user-attachments/assets/b619b122-9fd7-4b56-9e98-368b1f324fa4)


## Getting Started

Follow these instructions to install a copy of the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (preferably Python 3)
- [Django](https://www.djangoproject.com/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- A code editor (like [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/))

### Installation

1. Clone The Repository:
   https://github.com/monkey-d-siyam/Sudoku_Game.git
2. Set Up the Virtual Environment:
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies:
   pip install -r requirements.txt
4. Run Migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start the Server:
   python manage.py runserver

**Usage**
1. Generate a Sudoku Puzzle: Click the "Generate Sudoku" button to create a new puzzle.
2. Input your Solution: Fill in the grid with numbers between 1 and 9.
3. Check your Solution: Click the "Check Sudoku" button to validate your solution. If there are mistakes, a notification will appear, and the "Show Solution" button will be visible.
4. Show the Solution: Click the "Show Solution" button to reveal the correct solution for the current puzzle.

**Contributing**
Contributions are welcome! Please create a pull request with your changes and provide a detailed work description.

**Contact**
Don't hesitate to contact me at [juborajahmed0213@gmail.com] for any questions or suggestions.
