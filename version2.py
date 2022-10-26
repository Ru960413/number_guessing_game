# Add GUI using Tkinter
import tkinter as tk
import random


window = tk.Tk()
window.title("Number Guessing Game")
#set the window size and where it is positioned on screen
window.geometry("700x500+500+300")
window.resizable(False, False)
window.config(bg="#000000")

# implement the logic
TARGET = 1
RETRIES = 0

# update result
def update_result(text):
    result.configure(text=text)

# start a new game
def new_game():
    # activate the guess btn
    guess_btn.config(state="normal")

    global TARGET, RETRIES
    TARGET = random.randint(0,500)
    RETRIES = 0
    update_result(text="Guess a number between 0 and 500")

# game logic
def play_game():
    global RETRIES

    guess = int(entry_field.get())

    if guess != TARGET:
        RETRIES += 1
        result = "Wrong!\nTry Again!"

        if guess > TARGET:
            # hint = "The required number lies between 0 and {}".format(TARGET)
            hint = "Too Large"
        
        elif guess < TARGET:
            # hint = "The required number lies between {} and 500".format(guess)
            hint = "Too Small"
        result += "\nHINT: \n" + hint
        
    else:
        result=f"Congrats! You got it after {RETRIES} times!"
        guess_btn.configure(state="disabled")

        result += "\nClick on Play to start game"
            
        
    update_result(result)


exit_btn = tk.Button(window, text='Exit', font=("Arial", 20, "bold"),command=exit)
exit_btn.place(x=350, y=300)

# Creating titles
title = tk.Label(window, text="Number Guessing Game", font=("Arial", 30, "bold"), fg="White")
result = tk.Label(window, text="Click on Play to start game", font=("Arial", 16, "bold"), justify=tk.LEFT)
title.place(x=170, y=50)
result.place(x=180, y=210)

# Setting up the location of buttons
play_btn = tk.Button(text="Play", font=("Arial", 20, "bold"), command=new_game)
guess_btn = tk.Button(text="Guess", font=("Arial", 20, "bold"), state="disabled", command=play_game)

guess_btn.place(x=350, y=147)
play_btn.place(x=170, y=300)

# create a object to store the value in entry field
guessed_number = tk.StringVar()

# create an entry field and attach it the guessed number object that stores the value
entry_field= tk.Entry(window, font=("Arial", 12), textvariable=guessed_number)

# place the entry field
entry_field.place(x=180, y=150)
window.mainloop()

