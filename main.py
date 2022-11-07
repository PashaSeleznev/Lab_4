import tkinter
from PIL import Image
import time
import pygame
pygame.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)

def game():
    code_symbols = []
    for i in range(10):
        code_symbols.append(i)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in alphabet:
        code_symbols.append(i)

    middle = 9

    def block(k):
        from random import randint
        interval = k * middle
        summa = 0
        result = ''
        while summa <= interval:
            summa = 0
            result = ''
            for i in range(k):
                a = randint(0, 35)
                summa += a
                result += str(code_symbols[a])
        return result

    def clicked():
        lbl = tkinter.Label(window, text="Успешно! Ваш код: " + block(5) + '-' + block(4) + '-' + block(4),
                            font=("Arial Bold", 25),
                            bg='Gray')
        lbl.grid(column=0, row=0)


    window = tkinter.Tk()
    window.title("Добро пожаловать в генерацию кода")

    window.geometry('1313x833')

    window.image = tkinter.PhotoImage(file='gta.png')
    bg_gta = tkinter.Label(window, image=window.image)
    bg_gta.grid(column=0, row=0)

    btn_1 = tkinter.Button(window, text="Сгенерировать код", font=("Arial Bold", 15), bg='Gray', command=clicked)
    btn_1.grid(column=0, row=0)
    window.mainloop()


def animation(count, k):
    global anim
    global frames
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    k += 1
    time.sleep(0.5)
    if count == frames:
        count = 0
    if k == frames + 1:
        root.destroy()
        game()
    anim = root.after(50, lambda: animation(count, k))


root = tkinter.Tk()
root.title('Мы начинаем!')
file = "10.gif"
root.geometry('627x627')
info = Image.open(file)
frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tkinter.PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

count = 0
k = 0
anim = None

gif_label = tkinter.Label(root, image="")
gif_label.pack()


btn_2 = tkinter.Button(root, text="СТАРТ", font=("Arial Bold", 15), command=lambda: animation(count, k))
btn_2.pack()


root.mainloop()

