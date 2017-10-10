import pyglet as pyg
from random import randint

window = pyg.window.Window(width=1000, height=600)
window.set_caption('PRINT 10')


def randomic():
    casual = randint(0, 1)
    return casual


class Pencil:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0
        self.size = 10

    def draw_maze(self):
        while self.y_offset <= window.height:
            lor = randomic()
            if lor == 0:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset, self.x_offset + self.size,
                                                               self.y_offset + self.size)))
            elif lor == 1:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset + self.size,
                                                               self.x_offset + self.size, self.y_offset)))
            if self.x_offset < window.width:
                self.x_offset += self.size
            else:
                self.x_offset = 0
                self.y_offset += self.size


@window.event
def on_mouse_press(x, y, button, modifiers):
    window.clear()
    Pencil().draw_maze()

    # Optional line to export a screenshot.
    pyg.image.get_buffer_manager().get_color_buffer().save('print10_screenshot.png')


pyg.app.run()