import pyglet as pyg
from random import randint

window = pyg.window.Window(width=1000,height=600)

def randomic():
    casuale = randint(0,1)
    return casuale

class Matita():
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0
        self.size = 15
        
    def disegna(self):
        while self.y_offset <= window.height:
            lor = randomic()
            if lor == 0:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset, self.x_offset + self.size, self.y_offset + self.size)))
            elif lor == 1:
                pyg.graphics.draw(2, pyg.gl.GL_LINES, ('v2i', (self.x_offset, self.y_offset + self.size, self.x_offset + self.size, self.y_offset)))
            if self.x_offset < window.width:
                self.x_offset += self.size
            else:
                self.x_offset = 0
                self.y_offset += self.size

@window.event
def on_draw():
    Matita().disegna()

pyg.app.run()