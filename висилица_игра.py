import tkinter as tk
import random
attempt = 1
words =[i for i in open(r"C:\Users\Misha\Downloads\Telegram Desktop\russian_nouns.txt", "r",  encoding="utf-8").read().split("\n") if len(i) == 4]
print('Правила игры: нажимай на буквы , чтобы угадать слово.')
def letter(letter):
    global word, word_2, attempt
    flag = True
    canvas.create_text(250, 50, text="_ _ _ _", font=("Arial", 16), fill="blue")
    for i in range(len(word)):
        if letter == word[i]:
            word_2[i] = word[i]
            flag = False
            if ''.join(word_2) == word:
                canvas.create_text(200, 100, text='YOU WIN', font=("Arial", 16), fill="green")
    if flag:
        if attempt == 1:
            circle = canvas.create_oval(75, 100, 125, 150, outline="black")
        elif attempt == 2:
            line = canvas.create_line(100, 150, 100, 200, width=3, fill="black")
        elif attempt == 3:
            line = canvas.create_line(100, 200, 70, 250, width=3, fill="black")
        elif attempt == 4:
            line = canvas.create_line(100, 200, 130, 250, width=3, fill="black")
        elif attempt == 5:
            line = canvas.create_line(100, 170, 70, 200, width=3, fill="black")
        elif attempt == 6:
            line = canvas.create_line(100, 170, 130, 200, width=3, fill="black")
            canvas.create_text(200, 100, text='GAME OVER', font=("Arial", 16), fill="red")
        attempt += 1
    canvas.create_text(250, 50, text=word_2, font=("Arial", 16), fill="blue")
def create_button(text, x, y):
    button = tk.Button(
        root,   
        text=text, 
        command=lambda l=text: letter(l),
        bg="lightblue",
        fg="black",
        font=("Arial", 12),
        width=x,
        height=y
    )
    button.pack(side=tk.LEFT, padx=2)
root = tk.Tk()
root.geometry("1100x500")
for i in words:
    if len(i) != 4:
        words.remove(i)
word = words[random.randint(0, len(words)-1)]
word_2 = ['_', '_', '_', '_']
button_frame = tk.Frame(root)
button_frame.pack()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.create_text(250, 50, text="_ _ _ _", font=("Arial", 16), fill="blue")
russian_lower = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
russian_upper = [letter.lower() for letter in russian_lower]
for i in russian_upper:
    create_button(i, 2, 1)
line = canvas.create_line(50, 250, 50, 50, width=3, fill="black")
line2 = canvas.create_line(50, 50, 100, 50, width=3, fill="black")
line2 = canvas.create_line(100, 50, 100, 100, width=3, fill="black")
tk.mainloop()