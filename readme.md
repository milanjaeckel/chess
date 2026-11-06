# Chess Game

A Python chess board renderer built with Pygame. Aims to be a chess engine fully controlled by your keyboard

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

## Project Structure

```
chess-game/
└── pieces
    └── pieces.png (all 6 in both colours)
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
