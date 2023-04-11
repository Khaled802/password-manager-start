import tkinter
from PIL import Image, ImageTk
import random

# ==========================
# global variables

LABEL_FONT = ('Gadugi', 16, 'bold')
BG_COLOR = '#ffedda'
BTN_BG = '#FFB830'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SPECIAL_CHARS = '@.#&*-+'


# functions

def generate_password():
    global UPPER_LETTERS, LOWER_LETTERS, DIGITS, SPECIAL_CHARS
    upper = list(UPPER_LETTERS)
    lower = list(LOWER_LETTERS)
    dig = list(DIGITS)
    special = list(SPECIAL_CHARS)
    all_cat = [upper, lower, dig, special]
    word_len = random.randint(16, 25)
    password = []
    for i in range(word_len):
        cat = random.choice(all_cat)
        char = cat.pop(random.randrange(0, len(cat)))
        password.append(char)
        if len(cat) == 0:
            all_cat.remove(cat)
    return ''.join(password)


# generate a password by click on generator_btn

def text_password():
    password = generate_password()
    v.set(password)

# put the data in file


def put_in_file():
    password = v.get()
    _mail = mail.get()
    _website = website.get()
    if password and _mail and _website:
        file = open('data.txt', 'a')
        file.write(f'{_website} | {_mail} | {password}\n')
        file.close()
        v.set('')
        mail.set('')
        website.set('')
        pop_up('Added successfully')
    else:
        pop_up('There are some fields not filled')


def pop_up(s):
    top = tkinter.Toplevel(window)
    top.geometry("350x150")
    top.title('state')
    tkinter.Label(top, text=s, font=('Arial', 16), pady=20).pack()
    tkinter.Button(top, text='ok', font=('Arial', 16), command=lambda: top.destroy()).pack()

# =========================


window = tkinter.Tk()
window.minsize(width=600, height=350)
window.config(bg=BG_COLOR)
window.title('Password Generator')
# variables to deal with entry content
v = tkinter.StringVar()
mail = tkinter.StringVar()
website = tkinter.StringVar()

# canvas for image
canvas = tkinter.Canvas(width=130, height=110, bg=BG_COLOR,
                        highlightthickness=0)
img = (Image.open("password_manager.png"))

# Resize the Image using resize method
resized_image = img.resize((100, 100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

password_image = canvas.create_image(50, 50, image=new_image)
canvas.grid(column=1, row=0, sticky='W')

# Label for the website
mail_label = tkinter.Label(font=LABEL_FONT, text='Website', bg=BG_COLOR)
mail_label.config(pady=10, padx=50)
mail_label.grid(column=0, row=1, sticky='W')

# Label for the mail
mail_label = tkinter.Label(font=LABEL_FONT, text='Mail/Username', bg=BG_COLOR)
mail_label.config(pady=10, padx=50)
mail_label.grid(column=0, row=2, sticky='W')

# Label for the password
password_label = tkinter.Label(font=LABEL_FONT, text='Password', bg=BG_COLOR)
password_label.config(pady=10, padx=50)
password_label.grid(column=0, row=3, sticky='W')

# entry for website
website_entry = tkinter.Entry(width=50, textvariable=website)
website_entry.grid(column=1, row=1)

# entry for website
mail_entry = tkinter.Entry(width=50, textvariable=mail)
mail_entry.grid(column=1, row=2)


# entry for password
password_entry = tkinter.Entry(width=35, textvariable=v)
password_entry.grid(column=1, row=3, sticky='W')

# button generator
generator_btn = tkinter.Button(text='Generate', bg=BTN_BG, command=text_password)
generator_btn.grid(column=1, row=3, sticky='E')

# button add
add_btn = tkinter.Button(text='Add', bg=BTN_BG, pady=10, width=20, command=put_in_file)
add_btn.grid(column=1, row=5, sticky='W')


window.mainloop()
