import rosegraphics as rg

def shrinking_boxes(starting_square, colors, window):
    pass



def run_tests():
    # test 1
    window_1 = rg.RoseWindow(1600, 900, "test 1")
    colors_1 = [['red'], ['purple','blue'],['green','cyan','red']]
    stsq_1 = rg.Rectangle(rg.Point(450,450),rg.Point(500,500))
    shrinking_boxes(stsq_1, 3, colors_1, window_1)
    window_1.close_on_mouse_click()

    # test2
    window_2 = rg.RoseWindow(1600, 900, "test 2")
    colors_2 = [['red'],['green','cyan','red'],['purple','lime','black','orange'],['pink','blue']]
    stsq_2 = rg.Rectangle(rg.Point(400,400),rg.Point(600,600))
    shrinking_boxes(stsq_2, 8, colors_2, window_2)
    window_2.close_on_mouse_click()

run_tests()