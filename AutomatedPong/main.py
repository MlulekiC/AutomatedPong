from tkinter import *

from play_with_comp import PlayWithComp
from play_with_friend import playWithFriend


def main():
    root = Tk()
    root.title("Play Pong")
    root.geometry("300x100")

    Label(root, text="Play with computer or friend?[c or f]:").pack()
    e = Entry(root, width=100)
    e.pack()

    def show():
        if e.get() == "f":
            root.destroy()
            obj = playWithFriend()
            obj.play()

        elif e.get() == "c":
            root.destroy()
            obj1 = PlayWithComp()
            obj1.play()

    button = Button(root, text="Play", command=show)
    button.pack()

    root.mainloop()


main()