# Terminal Raycasting Demo

A simple first-person 3D renderer written in Python using the `curses` library.

The project uses a basic raycasting algorithm (similar to early games like Wolfenstein 3D) to render a 2D map as a pseudo-3D scene directly in the terminal.


![gameplay](game_1.png)


## Features

- First-person camera
- Collision detection
- Raycasting renderer
- Terminal graphics using `curses`
- Keyboard movement
- Adjustable field of view
- Perspective wall rendering
- Radar
- Floor shading
- Score and enemy respawn system
- Medkit, health and armor system
- Timer
- Best time is stored in file `best_time_ascii_3d.txt`
- Map loading


## Controls

| Key | Action |
|------|--------|
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| Q | Quit |
| E | Use medkit |
| X | Shot |
| ↑ | Rotate up |
| ↓ | Rotate down |



## How to play


**How to win:** Kill 10 enemies to win, medkits appear as blue pickups: get close to one to pick it up, each medkit gives you +20 health.

**Ammunition:** Yellow pickups are ammo. Adds one bullet per pickup, you can carry up to 8 ammo.


**Armor:** Protect you from taking demage, The orange pickups is armor.

**How to lose:** If an enemy is near you, your health will decrease, the game is over when it reaches 0.


**The first bar is for score, the second is for health**


## Requirements

- Python 3
- Linux 
- Architecture : `x86_64`


## Important Notes

* **Terminal Size:** Ensure your terminal window is maximized (not small), otherwise the 3D projection rendering may break.
* **Colors:** This game is optimized for `xterm`. If colors look washed out or incorrect, make sure your terminal emulator supports 256 colors.
* **Font Size:** For the best visual experience and sharper 3D graphics, use a smaller terminal font size.

## Run

```bash
python3 main3d.py
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
- `2` = enemy

**Map can be any list of lists with 0 and 1 and you can make your own in file `mapa_ascii_3d.json`, map can be as long as you want but it have to have same number of columns and rows, one list is one row, file named `mapa_ascii_3d.json` is template, if game wouldn't find any map with that name , map will be generated**


## Troubleshooting

### Game fails with `ValueError: Color number is greater than COLORS-1 (7)`

This means your terminal is running in 8-color mode. The game requires a terminal with 256-color support.

Check your terminal color support:

```bash
tput colors
```

The output should be `256` or higher.

If it shows only `8`, check that your terminal is configured for 256 colors:

```bash
export TERM=xterm-256color
```

or run the game directly with:

```bash
TERM=xterm-256color  python3 main3d.py
```
