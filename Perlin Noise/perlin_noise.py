from random import randint

import pyglet as pyg
from noise.perlin import SimplexNoise
width = 600
height = 250
window = pyg.window.Window(resizable=True, width=width, height=height)
noisee = SimplexNoise()
colorsss = []


def calculate_perlin(p_list):
    rate = 250
    for y in range(window.height+1):
        column = []
        for x in range(window.width+1):
            x_coord = x/rate+1901
            y_coord = y/rate+1901
            point = [('v2f', (x, y)), ("c3f", (noisee.noise2(x_coord, y_coord),
                                               noisee.noise2(x_coord, y_coord),
                                               noisee.noise2(x_coord, y_coord)))]
            column.append(point)
        p_list.append(column)


@window.event
def on_draw():
    calculate_perlin(colorsss)


@window.event()
def on_mouse_press(x, y, button, modifiers):
    for column in colorsss:
        for point in column:
            pyg.graphics.draw(1, pyg.gl.GL_POINTS, (point[0]), (point[1]))

    #pyg.image.get_buffer_manager().get_color_buffer().save('perlin_screenshot.png')


pyg.app.run()
