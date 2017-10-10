import pyglet as pyg
from random import randint

window = pyg.window.Window(width=1000, height=600)
window.set_caption('PRINT 10')


def randomic():
    casual = randint(1, 6)
    return casual


class Pencil:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0
        self.size = 10

    def draw_maze(self):
        while self.y_offset <= window.height:
            lor = randomic()
            # 1st case: diagonal line bottom-left to top-right
            if lor == 1:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset,
                                                               self.x_offset + self.size, self.y_offset + self.size)))
            # 2nd case: diagonal line top-left to bottom-right
            elif lor == 2:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset + self.size,
                                                               self.x_offset + self.size, self.y_offset)))
            # 3rd case: horizontal line on the bottom
            elif lor == 3:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset,
                                                               self.x_offset + self.size, self.y_offset)))
            # 4th case: horizontal line on the top
            elif lor == 4:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset + self.size,
                                                               self.x_offset + self.size, self.y_offset + self.size)))
            # 5th case: vertical line on the left
            elif lor == 5:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset,
                                                               self.x_offset, self.y_offset + self.size)))
            # 6th case: vertical line on the right
            elif lor == 6:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset + self.size, self.y_offset,
                                                               self.x_offset + self.size, self.y_offset + self.size)))

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
    # pyg.image.get_buffer_manager().get_color_buffer().save('print10_screenshot.png')


pyg.app.run()
