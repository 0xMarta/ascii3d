import curses
import math
import time


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    my, mx = stdscr.getmaxyx()
    px = 12.5
    py = 12.5
    pa = 0
    vf = math.pi / 3
    mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    while True:
        key = stdscr.getch()
        if key == ord("q"):
            break
        if key == ord("w"):
            px += math.cos(pa) * 0.1
            py += math.sin(pa) * 0.1
        if key == ord("s"):
            px -= math.cos(pa) * 0.1
            py -= math.sin(pa) * 0.1
        if key == ord("a"):
            pa -= 0.1
        if key == ord("d"):
            pa += 0.1
        stdscr.erase()
        for ix in range(mx):
            ra = (pa - vf / 2) + (ix / mx) * vf
            dist = 0
            while True:
                dist += 0.05
                cx = px + math.cos(ra) * dist
                cy = py + math.sin(ra) * dist
                if int(cx) < 0 or int(cx) >= 25 or int(cy) < 0 or int(cy) >= 25:
                    break
                if mapa[int(cy)][int(cx)]:
                    break
            dist = dist * math.cos(ra - pa)
            if dist < 0.1:
                dist = 0.1
            wall_h = int(my / dist)
            start = int((my - wall_h) / 2)
            end = int((my + wall_h) / 2)
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            for y in range(start, end):
                try:
                    stdscr.addch(y, ix, "#")
                except curses.error:
                    pass

        stdscr.refresh()
        time.sleep(0.03)


curses.wrapper(main)
