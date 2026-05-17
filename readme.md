# Chess Game

A Python chess board renderer built with Pygame. Renders a classic 8x8 chessboard with alternating black and white squares at 60 FPS.

## Requirements

- Python 3.x
- Pygame

**Confirmed working on:** Arch Linux (omarchy), Windows 11

## Installation

Python needs to be installed.

Then install Pygame by running this in your terminal:

```bash
pip install pygame
```

If you're on Linux and `pip` doesn't work, try `pip3` instead. On Arch you can also install it through pacman:

```bash
sudo pacman -S python-pygame
```

Once that's done, just run the game with:

```bash
python main.py
```

## How It Works

The six chess piece types are defined as named variables at the top of `main.py`, and two lists represent the standard starting rows — the back rank and the pawn row.

The board itself is an 800x800 window split into a 8x8 grid of 100x100 pixel squares. Each row alternates which color starts first, giving you the classic chessboard pattern. The whole board is redrawn every frame, capped at 60 FPS using Pygame's clock.

The main loop handles three things: listening for the quit event, clearing and redrawing the board each frame, and flipping the display buffer to show the result.

## Project Structure

```
chess-game/
└── pieces
    └── pieces.png (multiple)
├── board.py
├── main.py
└── README.md
```

## Sources

- [Pygame - Import and Initialization](https://www.pygame.org/docs/tut/ImportInit.html)
- [GeeksforGeeks - How to Draw a Rectangle in Pygame](https://www.geeksforgeeks.org/python/how-to-draw-rectangle-in-pygame/)
- [Blender Stack Exchange - Toggle a Boolean Property](https://blender.stackexchange.com/questions/23040/how-to-easily-toggle-a-boolean-property)
- [StackOverflow - How to call function from another .py file](https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file)
- [GeeksforGeeks - Create a chess game in python](https://www.geeksforgeeks.org/python/create-a-chess-game-in-python/)
