import curses
import math
import random
import time
from termios import IEXTEN


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_color(14, 0, 900, 0)
    curses.init_color(15, 0, 700, 0)
    curses.init_color(16, 0, 500, 0)
    curses.init_color(17, 0, 300, 0)
    curses.init_color(18, 0, 100, 0)
    curses.init_pair(4, 14, curses.COLOR_BLACK)
    curses.init_pair(5, 15, curses.COLOR_BLACK)
    curses.init_pair(6, 16, curses.COLOR_BLACK)
    curses.init_pair(7, 17, curses.COLOR_BLACK)
    curses.init_pair(8, 18, curses.COLOR_BLACK)
    my, mx = stdscr.getmaxyx()
    px = 25
    py = 25
    pa = 0
    vf = math.pi / 3

    enemy_x = random.randint(3, 47)
    enemy_y = random.randint(3, 47)

    mapa = (
        [
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        ]
        + [[1] + [0] * 48 + [1] for _ in range(48)]
        + [
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        ]
    )

    shot_dist = 0

    mapa[enemy_y][enemy_x] = 2
    while True:
        key = stdscr.getch()
        if key == ord("q"):
            break
        if key == ord("w"):
            if (
                px + math.cos(pa) * 0.1 >= 0
                and px + math.cos(pa) * 0.1 < 50
                and py + math.sin(pa) * 0.1 >= 0
                and py + math.sin(pa) * 0.1 < 50
                and mapa[int(py + math.sin(pa) * 0.1)][int(px + math.cos(pa) * 0.1)]
                == 0
            ):
                px += math.cos(pa) * 0.1
                py += math.sin(pa) * 0.1
        if key == ord("s"):
            if (
                py - math.sin(pa) * 0.1 >= 0
                and py - math.sin(pa) * 0.1 < 50
                and px - math.cos(pa) * 0.1 >= 0
                and px - math.cos(pa) * 0.1 < 50
                and mapa[int(py - math.sin(pa) * 0.1)][int(px - math.cos(pa) * 0.1)]
                == 0
            ):
                px -= math.cos(pa) * 0.1
                py -= math.sin(pa) * 0.1
        if key == ord("a"):
            pa -= 0.1
        if key == ord("d"):
            pa += 0.1

        stdscr.erase()
        for ix in range(mx):
            hit = 0
            ch = " "
            color = curses.color_pair(0)
            ra = (pa - vf / 2) + (ix / mx) * vf
            dist = 0
            while True:
                dist += 0.05
                cx = px + math.cos(ra) * dist
                cy = py + math.sin(ra) * dist
                if int(cx) < 0 or int(cx) >= 50 or int(cy) < 0 or int(cy) >= 50:
                    break
                if mapa[int(cy)][int(cx)] == 1:
                    hit = 1
                    break

            dist = dist * math.cos(ra - pa)
            if dist < 0.1:
                dist = 0.1
            wall_h = int(my / dist)
            start = int((my - wall_h) / 2) - my // 4
            end = int((my + wall_h) / 2) - my // 4
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            if hit == 1:
                ch = "#"
                if dist <= 10 and dist >= 0:
                    color = curses.color_pair(8)
                elif dist > 10 and dist <= 20:
                    color = curses.color_pair(7)
                elif dist > 20 and dist <= 30:
                    color = curses.color_pair(6)
                elif dist > 30 and dist <= 40:
                    color = curses.color_pair(5)
                elif dist > 40:
                    color = curses.color_pair(4)
            if hit != 0:
                if hit == 1:
                    for y in range(start, end):
                        try:
                            stdscr.addch(y, ix, ch, color)
                        except curses.error:
                            pass
        startx = mx // 4
        endx = 3 * startx
        for j in range(startx, endx):
            hit = 0
            ch = " "
            color = curses.color_pair(0)
            ra = (pa - vf / 2) + (j / mx) * vf
            dist = 0
            while True:
                dist += 0.05
                ox = px + math.cos(ra) * dist
                oy = py + math.sin(ra) * dist
                if int(ox) < 0 or int(ox) >= 50 or int(oy) < 0 or int(oy) >= 50:
                    break
                if mapa[int(oy)][int(ox)] == 2:
                    hit = 2
                    break
            dist = dist * math.cos(ra - pa)

            if dist < 0.1:
                dist = 0.1
            wall_h = int(my / dist)
            start = int((my - wall_h) / 2) - my // 4
            end = int((my + wall_h) / 2) - my // 4
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            if hit == 2:
                ch = "@"
                color = curses.color_pair(1)
                for y in range(start, end):
                    try:
                        stdscr.addch(y, j, ch, color)
                    except curses.error:
                        pass

        dx = px + math.cos(pa) * shot_dist
        dy = py + math.sin(pa) * shot_dist
        if mapa[int(dy)][int(dx)] != 1 and mapa[int(dy)][int(dx)] != 2:
            shot_dist += 0.05
        if mapa[int(dy)][int(dx)] == 2:
            mapa[int(dy)][int(dx)] = 0
            enemy_x = random.randint(3, 47)
            enemy_y = random.randint(3, 47)
            mapa[enemy_y][enemy_x] = 2
        if (
            dy < 0
            or dy > 49
            or dx < 0
            or dx > 49
            or mapa[int(dy)][int(dx)] == 1
            or mapa[int(dy)][int(dx)] == 2
        ):
            shot_dist = 0
        x = mx / 2
        y = my - shot_dist * 5
        if y < my // 2:
            shot_dist = 0
        else:
            try:
                stdscr.addstr(int(y), int(x), "o", curses.color_pair(3))
            except curses.error:
                pass
        stdscr.refresh()
        time.sleep(0.03)


curses.wrapper(main)
