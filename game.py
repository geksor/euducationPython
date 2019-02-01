import tkinter

# constans
ZERRO = 0
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
MAIN_BALL_RADIUS = 30
MAIN_BALL_COLOR = 'blue'
INIT_DX = 3
INIT_DY = 3
DELAY = 100


# Balls class
class Balls:
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=self.color)

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=BG_COLOR, outline=BG_COLOR)

    def move(self):
        # colliding with walls
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERRO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERRO):
            self.dy = -self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


# mouse_events
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' in globals():
            main_ball.dx = -main_ball.dx
        else:
            main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            main_ball.draw()
    elif event.num == 3:
        if 'main_ball' in globals():
            main_ball.dy = -main_ball.dy
    elif event.keycode == 37:
        if 'main_ball' in globals():
            main_ball.dx = -INIT_DX
    elif event.keycode == 39:
        if 'main_ball' in globals():
            main_ball.dx = INIT_DX
    elif event.keycode == 38:
        if 'main_ball' in globals():
            main_ball.dy = -INIT_DY
    elif event.keycode == 40:
        if 'main_ball' in globals():
            main_ball.dy = INIT_DY
    else:
        main_ball.hide()


# main loop game
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(DELAY, main)


root = tkinter.Tk()
root.title('Colliding Balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind_all('<Left>', mouse_click)
canvas.bind_all('<Right>', mouse_click)
canvas.bind_all('<Up>', mouse_click)
canvas.bind_all('<Down>', mouse_click)
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click)
if 'main_ball' in globals():
    del main_ball
main()
root.mainloop()
