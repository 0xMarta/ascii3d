import curses
import math
import random
import time


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
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
    curses.init_color(15, 0, 800, 0)
    curses.init_color(16, 0, 700, 0)
    curses.init_color(17, 0, 600, 0)
    curses.init_color(18, 0, 500, 0)
    curses.init_color(40, 0, 400, 0)
    curses.init_color(41, 0, 300, 0)
    curses.init_color(42, 0, 200, 0)
    curses.init_color(43, 0, 100, 0)
    curses.init_color(44, 0, 50, 0)
    curses.init_pair(4, 14, curses.COLOR_BLACK)
    curses.init_pair(5, 15, curses.COLOR_BLACK)
    curses.init_pair(6, 16, curses.COLOR_BLACK)
    curses.init_pair(7, 17, curses.COLOR_BLACK)
    curses.init_pair(8, 18, curses.COLOR_BLACK)
    curses.init_pair(30, 40, curses.COLOR_BLACK)
    curses.init_pair(31, 41, curses.COLOR_BLACK)
    curses.init_pair(32, 42, curses.COLOR_BLACK)
    curses.init_pair(33, 43, curses.COLOR_BLACK)
    curses.init_pair(34, 44, curses.COLOR_BLACK)
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
    score = 0
    health = 100
    timer = 0
    horizon = my // 2
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
    wall_number = 0
    for ii in range(5):
        xx = random.randint(6, 42)
        yy = random.randint(6, 42)
        mapa[yy][xx] = 1
    while True:
        xx = random.randint(6, 42)
        yy = random.randint(6, 42)
        if mapa[yy][xx] != 2:
            if (
                mapa[yy - 1][xx] == 1
                or mapa[yy + 1][xx] == 1
                or mapa[yy][xx - 1] == 1
                or mapa[yy][xx + 1] == 1
            ):
                mapa[yy][xx] = 1
                wall_number += 1
        if wall_number == 45:
            break

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
        if key == curses.KEY_UP:
            horizon -= 2
        if key == curses.KEY_DOWN:
            horizon += 2

        stdscr.erase()
        for ix in range(mx):
            hit = 0
            ch = " "
            color = curses.color_pair(0)
            ra = (pa - vf / 2) + (ix / mx) * vf
            dist = 0
            cos_ra = math.cos(ra)
            sin_ra = math.sin(ra)
            delta_dist_x = abs(1 / math.cos(ra)) if cos_ra != 0 else 1e30
            delta_dist_y = abs(1 / math.sin(ra)) if sin_ra != 0 else 1e30
            map_x = int(px)
            map_y = int(py)

            if math.cos(ra) < 0:
                step_x = -1
                side_dist_x = (px - int(px)) * delta_dist_x
            else:
                step_x = 1
                side_dist_x = (int(px) + 1 - px) * delta_dist_x
            if math.sin(ra) < 0:
                step_y = -1
                side_dist_y = (py - int(py)) * delta_dist_y
            else:
                step_y = 1
                side_dist_y = (int(py) + 1 - py) * delta_dist_y
            while True:
                if side_dist_x < side_dist_y:
                    side_dist_x += delta_dist_x
                    map_x += step_x
                    side = 0
                else:
                    side_dist_y += delta_dist_y
                    map_y += step_y
                    side = 1
                if map_x < 0 or map_x >= 50 or map_y < 0 or map_y >= 50:
                    break

                if mapa[map_y][map_x] == 1:
                    hit = 1
                    break
                color_dist = dist
            if side == 0:
                dist = side_dist_x - delta_dist_x
                color_dist = dist + 10
            else:
                dist = side_dist_y - delta_dist_y
                color_dist = dist
            dist = dist * math.cos(ra - pa)
            if dist < 0.1:
                dist = 0.1
            wall_h = int(my / dist)
            start = horizon - wall_h // 2
            end = horizon + wall_h // 2
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            if start < 0:
                start = 0
            if end >= my:
                end = my - 1
            if hit == 1:
                ch = "┼"
                if color_dist <= 5 and color_dist >= 0:
                    color = curses.color_pair(4)
                elif color_dist > 5 and color_dist <= 10:
                    color = curses.color_pair(5)
                elif color_dist > 10 and color_dist <= 15:
                    color = curses.color_pair(6)
                elif color_dist > 15 and color_dist <= 20:
                    color = curses.color_pair(7)
                elif color_dist > 20 and color_dist <= 25:
                    color = curses.color_pair(8)
                elif color_dist > 25 and color_dist <= 30:
                    color = curses.color_pair(30)
                elif color_dist > 30 and color_dist <= 35:
                    color = curses.color_pair(31)
                elif color_dist > 35 and color_dist <= 40:
                    color = curses.color_pair(32)
                elif color_dist > 40 and color_dist <= 45:
                    color = curses.color_pair(33)
                elif color_dist > 45:
                    color = curses.color_pair(34)

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
                        delta_y = y_end - horizon
                        beta = (delta_y / (my // 2)) * (vfvert / 2)
                        if beta <= 0 or math.isclose(beta, 0):
                            beta = 999.0
                            dist2d = 999.0
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
                if mapa[int(oy)][int(ox)] == 1:
                    break
                try:
                    stdscr.addstr(int(oy), int(ox), ".", curses.color_pair(9))
                except curses.error:
                    pass

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
            score += 1
            curses.beep()
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
        if math.hypot(px - enemy_x, py - enemy_y) <= 2:
            health -= 2
        c = 0
        for i in range(50):
            try:
                if c < score * 5:
                    c += 1
                    stdscr.addstr(5, i + int(mx // 4 * 3), "*", curses.color_pair(2))
                    stdscr.addstr(6, i + int(mx // 4 * 3), "*", curses.color_pair(2))
                    stdscr.addstr(7, i + int(mx // 4 * 3), "*", curses.color_pair(2))
                else:
                    stdscr.addstr(5, i + int(mx // 4 * 3), "*", curses.color_pair(1))
                    stdscr.addstr(6, i + int(mx // 4 * 3), "*", curses.color_pair(1))
                    stdscr.addstr(7, i + int(mx // 4 * 3), "*", curses.color_pair(1))
            except curses.error:
                pass
        hlth = 0
        for n in range(40):
            try:
                if hlth < health * 40 // 100:
                    stdscr.addstr(10, n + int(mx // 4 * 3), "*", curses.color_pair(1))
                    stdscr.addstr(11, n + int(mx // 4 * 3), "*", curses.color_pair(1))
                    stdscr.addstr(12, n + int(mx // 4 * 3), "*", curses.color_pair(1))
                else:
                    stdscr.addstr(10, n + int(mx // 4 * 3), "*", curses.color_pair(2))
                    stdscr.addstr(11, n + int(mx // 4 * 3), "*", curses.color_pair(2))
                    stdscr.addstr(12, n + int(mx // 4 * 3), "*", curses.color_pair(2))
                hlth += 1
            except curses.error:
                pass
        health = min(health + 1, 100)
        if timer == 20:
            mapa[enemy_y][enemy_x] = 0
            if enemy_y > int(py):
                enemy_y -= 1
                timer = 0
            elif enemy_y != py:
                enemy_y += 1
                timer = 0
            if enemy_x > int(px):
                enemy_x -= 1
                timer = 0
            elif enemy_x != int(px):
                enemy_x += 1
                timer = 0
            mapa[enemy_y][enemy_x] = 2
        timer += 1
        if health <= 1:
            stdscr.erase()
            stdscr.refresh()
            a = "        XXXXX        XXXX        X X    XX    XXXXXX            XXXXXX       X      X   XXXXXX   XXXXX "
            b = "       X            XX  XX      X   X  X  X   X                X      X      X      X   X        X    X"
            c = "      X     XX     X      X     X    XX   X   XXXXXX          X        X      X    X    XXXXXX   XXXXX "
            d = "       X     X     XXXXXXXX     X         X   X                X      X        X  X     X        X  X  "
            e = "        XXXXX      X      X     X         X   XXXXXX            XXXXXX          XX      XXXXXX   X   X "
            try:
                stdscr.addstr(
                    my // 2 - 5, mx // 2 - len(a) // 2, a, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 4, mx // 2 - len(b) // 2, b, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 3, mx // 2 - len(c) // 2, c, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 2, mx // 2 - len(d) // 2, d, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 1, mx // 2 - len(e) // 2, e, curses.color_pair(1)
                )
            except curses.error:
                pass
            stdscr.refresh()
            time.sleep(5)
            return
        if score == 10:
            stdscr.erase()
            stdscr.refresh()
            f = "X   X       XXXXX     X      X          X       X    X       XX    X"
            g = "X   X      X     X    X      X          X       X    X       X X   X"
            k = " X X       X     X    X      X           X     X     X       X  X  X"
            m = "  X        X     X    X      X           X  X  X     X       X   X X"
            p = "  X         XXXXX      XXXXXX             XX XX      X       X    X "
            try:
                stdscr.addstr(
                    my // 2 - 5, mx // 2 - len(f) // 2, f, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 4, mx // 2 - len(g) // 2, g, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 3, mx // 2 - len(k) // 2, k, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 2, mx // 2 - len(m) // 2, m, curses.color_pair(1)
                )
                stdscr.addstr(
                    my // 2 - 1, mx // 2 - len(p) // 2, p, curses.color_pair(1)
                )
            except curses.error:
                pass
            stdscr.refresh()
            time.sleep(5)
            return
        stdscr.refresh()
        time.sleep(0.03)


curses.wrapper(main)

# "               XXXXX        XXXX        X X    XX    XXXXXX            XXXXXX       X      X   XXXXXX   XXXXX"
# "              X            XX  XX      X   X  X  X   X                X      X      X      X   X        X    X"
# "             X     XX     X      X     X    XX   X   XXXXXX          X        X      X    X    XXXXXX   XXXXX"
# "              X     X     XXXXXXXX     X         X   X                X      X        X  X     X        X  X"
# "                XXXXX     X      X     X         X   XXXXXX            XXXXXX          XX      XXXXXX   X   X"
