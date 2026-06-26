# Terminal Raycasting Demo

A simple first-person 3D renderer written in Python using the `curses` library.

The project uses a basic raycasting algorithm (similar to early games like Wolfenstein 3D) to render a 2D map as a pseudo-3D scene directly in the terminal.

## Features

- First-person camera
- Raycasting renderer
- Terminal graphics using `curses`
- Keyboard movement
- Adjustable field of view
- Perspective wall rendering

## Controls

| Key | Action |
|------|--------|
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| Q | Quit |

## Requirements

- Python 3
- curses (built-in on Linux/macOS)

## Run

```bash
python3 main.py
```

## How it works

The renderer casts one ray for each column of the terminal.

Each ray:
1. Starts at the player's position.
2. Travels forward until it hits a wall.
3. Measures the distance.
4. Calculates the projected wall height.
5. Draws a vertical slice of the wall.

To reduce the fisheye effect, the measured distance is corrected using the cosine of the viewing angle.

## Map

The world is stored as a 2D grid.

- `1` = wall
- `0` = empty space

## Future improvements

- Collision detection
- Floor and ceiling shading
- Textured walls
- Sprites
- Minimap
- Better movement physics
