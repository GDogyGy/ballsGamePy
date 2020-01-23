import tkinter as tk
from tkinter import simpledialog, messagebox
from random import randint

WIDTH = 300
HEIGHT = 200

class Ball:
    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(1, WIDTH - self.R)
        self.y = randint(1, HEIGHT - self.R)
        self.dx, self.dy = (+2, +3)
        self.points = {'red': 20, 'orange': 32, 'yellow': 50, 'green': 20, 'blue': 100}
        self.pick_color = list(self.points.keys())[randint(0,4)]
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill= self.pick_color )

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


class User:
    def __init__(self, name , points):
        self.name = name
        self.points = points

    def remember_user(self):
        f = open('user.txt', 'a')  # toDO попробовать pickle или json
        data = str(self.name) + ":" + self.points
        f.write(data + '\n')
        f.close()
    def find_user(self):
        f = open('user.txt', 'r')
        for line in f:
            if self.name == line.split(':')[0]:
                self.lastPoints = line.split(':')[1]
                return self.lastPoints



def canvas_click_handler(event):
    for ball in balls:
        if (((ball.x - event.x) ** 2 ) ** 0.5)+(((ball.y - event.y) ** 2) ** 0.5) <= ball.R: # По теореме пифогора расстояние между 2 точками
            canvas.delete(ball.ball_id)
            #del ball # TODO проверить удаляет ли экземпляр класса
            print(canvas)
            print(ball)
            print(type(ball))
            break


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


def main():
    global root, canvas, balls, name
    root = tk.Tk()
    name = simpledialog.askstring("Input", "What is your first name?", parent=root)
    user = User(name,'0')
    if user.find_user():
        messagebox.showinfo("Information", "Привет "+ user.name +" я тебя помню!\nТы набрал:" + user.lastPoints + " очков!")
    else:
        pass
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind("<Button-1>", canvas_click_handler)
    balls = [Ball() for i in range(5)]
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()





