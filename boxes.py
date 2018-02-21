# Jaclyn Setina and Daniel Verlaque
# D
#


import rosegraphics as rg
import math


def go_along_row(row_size, rsx, rsy, width, color, window):
    square_x, square_y = rsx, rsy
    for k in range(row_size):
        draw_square(square_x, square_y, width, color, window)
        square_x = square_x + width


def go_along_column(column_size, csx, csy, width, color, window):
    square_x, square_y = csx, csy
    for k in range(column_size):
        draw_square(square_x, square_y, width, color, window)
        square_y= square_y + width


def draw_square(top_left_x, top_left_y, width, color, window):
    top_left_point = rg.Point(top_left_x, top_left_y)
    lower_right_x = top_left_x + width
    lower_right_y = top_left_y + width
    lower_right_point = rg.Point(lower_right_x, lower_right_y)
    sqr = rg.Rectangle(top_left_point, lower_right_point)
    sqr.fill_color = color
    sqr.attach_to(window)
    window.render()


def squares(starting_square, n, colors, window):
    ss_topleft = starting_square.get_bounding_box().get_upper_left_corner()
    starting_x = ss_topleft.x
    starting_y = ss_topleft.y
    width = starting_square.get_width()

    row_start_x = starting_x
    row_start_y = starting_y
    for k in range(n): # for row in rows loop
        # for each row... we expect row_start_x, row_start_y to have row's top left corner
        # draw the row
        ring_size = 2*k + 1

        # Upper Row
        go_along_row(ring_size, row_start_x, row_start_y, width, colors[k % len(colors)], window)

        # Left column
        go_along_column(ring_size, row_start_x, row_start_y, width, colors[k % len(colors)], window)

        # Lower Row
        lower_x = row_start_x
        lower_y = row_start_y + width * (ring_size - 1)
        go_along_row(ring_size, lower_x, lower_y, width, colors[k % len(colors)], window)

        # Right column
        upper_right_x = row_start_x + width * (ring_size - 1)
        upper_right_y = row_start_y
        go_along_column(ring_size, upper_right_x, upper_right_y, width, colors[k % len(colors)], window)

        # after we drew the row...
        row_start_x = row_start_x - width
        row_start_y = row_start_y - width



window1 = rg.RoseWindow(1600, 900, "squares 1")
squares(rg.Rectangle(rg.Point(450,450),rg.Point(475,475)),15, ['cyan','pink','blue'], window1)
window1.close_on_mouse_click()


