import curses
import math
import random
import time


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_color(31, 900, 900, 0)
    curses.init_color(32, 700, 700, 0)
    curses.init_color(33, 500, 500, 0)
    curses.init_color(34, 300, 300, 0)
    curses.init_color(35, 100, 100, 0)
    curses.init_pair(20, 31, curses.COLOR_BLACK)
    curses.init_pair(21, 32, curses.COLOR_BLACK)
    curses.init_pair(22, 33, curses.COLOR_BLACK)
    curses.init_pair(23, 34, curses.COLOR_BLACK)
    curses.init_pair(24, 35, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_GREEN)
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
    curses.init_color(19, 900, 0, 0)
    curses.init_color(20, 700, 0, 0)
    curses.init_color(21, 500, 0, 0)
    curses.init_color(22, 300, 0, 0)
    curses.init_color(23, 100, 0, 0)
    curses.init_pair(10, 19, curses.COLOR_BLACK)
    curses.init_pair(11, 20, curses.COLOR_BLACK)
    curses.init_pair(12, 21, curses.COLOR_BLACK)
    curses.init_pair(13, 22, curses.COLOR_BLACK)
    curses.init_pair(14, 23, curses.COLOR_BLACK)
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
                dist += 0.1
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
            start = int((my - wall_h) / 2)
            end = int((my + wall_h) / 2)
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            if hit == 1:
                ch = "┼"
                if dist <= 10 and dist >= 0:
                    color = curses.color_pair(4)
                elif dist > 10 and dist <= 20:
                    color = curses.color_pair(5)
                elif dist > 20 and dist <= 30:
                    color = curses.color_pair(6)
                elif dist > 30 and dist <= 40:
                    color = curses.color_pair(7)
                elif dist > 40:
                    color = curses.color_pair(8)

            if hit != 0:
                if hit == 1:
                    for y_mid in range(start, end):
                        try:
                            stdscr.addch(y_mid, ix, ch, color)
                        except curses.error:
                            pass
                    for y_end in range(end, my):
                        h = 0.5
                        vfvert = vf * (my / mx) * 2.0
                        delta_y = y_end - (my // 2)
                        beta = (delta_y / (my // 2)) * (vfvert / 2)
                        if beta <= 0 or math.isclose(beta, 0):
                            beta = 999.0
                        else:
                            dist2d = h / (math.tan(beta))
                        fx = px + math.cos(ra) * dist2d
                        fy = py + math.sin(ra) * dist2d
                        dist3d = math.sqrt(
                            ((fx - px) ** 2) + ((fy - py) ** 2) + (h * 2)
                        )
                        if dist3d <= 5 and dist3d >= 0:
                            color_floor = curses.color_pair(20)
                        elif dist3d > 5 and dist3d <= 10:
                            color_floor = curses.color_pair(21)
                        elif dist3d > 10 and dist3d <= 15:
                            color_floor = curses.color_pair(22)
                        elif dist3d > 15 and dist3d <= 20:
                            color_floor = curses.color_pair(23)
                        elif dist3d > 20:
                            color_floor = curses.color_pair(24)
                        try:
                            stdscr.addch(y_end, ix, "█", color_floor)
                        except curses.error:
                            pass

        for j in range(mx):
            hit = 0
            ch = " "
            color = curses.color_pair(0)
            ra = (pa - vf / 2) + (j / mx) * vf
            dist = 0
            while True:
                dist += 0.1
                ox = px + math.cos(ra) * dist
                oy = py + math.sin(ra) * dist
                if int(ox) < 0 or int(ox) >= 50 or int(oy) < 0 or int(oy) >= 50:
                    break

                if mapa[int(oy)][int(ox)] == 2:
                    hit = 2
                    break
                stdscr.addstr(int(oy), int(ox), ".", curses.color_pair(9))

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
            if hit == 2:
                ch = random.choice(
                    [
                        "░",
                    ]
                )
                if dist <= 10 and dist >= 0:
                    color = curses.color_pair(10)
                elif dist > 10 and dist <= 20:
                    color = curses.color_pair(11)
                elif dist > 20 and dist <= 30:
                    color = curses.color_pair(12)
                elif dist > 30 and dist <= 40:
                    color = curses.color_pair(13)
                elif dist > 40:
                    color = curses.color_pair(14)
                for y in range(start, end):
                    try:
                        stdscr.addch(y, j, ch, color)
                    except curses.error:
                        pass

        dx = px + math.cos(pa) * shot_dist
        dy = py + math.sin(pa) * shot_dist
        if mapa[int(dy)][int(dx)] != 1 and mapa[int(dy)][int(dx)] != 2:
            shot_dist += 0.1
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
