import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random

def entry_box():
    answer_entry = tk.Entry(window, textvariable = answer)
    answer_entry.pack(ipadx=10, ipady=10, fill=tk.X)

def question(text):
    question = tk.Label(window, text=text)  
    question.pack(ipadx=10, ipady=10, fill=tk.X)


def initialize_english():
    english_button.pack_forget()
    spanish_button.pack_forget()
    global lang
    lang = 0
    entry_box()
    ask_question_english(counter)

def initialize_spanish():
    english_button.pack_forget()
    spanish_button.pack_forget()
    global lang
    lang = 1
    entry_box()
    ask_question_spanish()

def ask_question_english(counter):
    text = english[counter]
    question(text)

def ask_question_spanish():
    text = spanish[0]
    question(text)

def get_answer_english(counter):
    print(spanish[counter+1])
    if answer.get() == spanish[counter+1]:
        print("Correct")
    else:
        print("Incorrect")
    counter += 1
    ask_question_english(counter)

def get_answer_spanish():
    if answer.get() == english[0]:
        print("Correct")
    else:
        print("Incorrect")

def enter_key_pressed(event):
    if lang == 0:
        print("get answer english")
        get_answer_english(counter)
    elif lang == 1:
        print("get answer spanish")
        get_answer_spanish()

# Create window
window = tk.Tk()
window.geometry("500x500")
window.bind("<Return>", enter_key_pressed)

# Initialise variables and arrays
path = "C:/Users/Tristan/Documents/"
lang = -1
#global counter_global
counter = 0
# -1 = null, 0 = english, 1 = spanish
spanish = []
english = []
with open(path + "spanish words.txt") as file:
    spanish = file.readlines()
with open(path + "english words.txt") as file:
    english = file.readlines()

# Fisher-Yates shuffle algorithm
n = len(spanish)
for i in range(n-1, 0, -1):
    j = random.randint(0, i)
    temp = spanish[i]
    spanish[i] = spanish[j]
    spanish[j] = temp
    temp = english[i]
    english[i] = english[j]
    english[j] = temp
print(spanish)
print(english)
for word in spanish:
    spanish[spanish.index(word)] = word.replace("\n", "")
for word in english:
    english[english.index(word)] = word.replace("\n", "")
print(spanish)
print(english)

answer = tk.StringVar()
english_button = tk.Button(window, text = "English", fg = 'white', bg = 'gray', command = initialize_english)
spanish_button = tk.Button(window, text = "Spanish", fg = 'white', bg = 'gray', command = initialize_spanish)
english_button.pack(ipadx=10, ipady=10, fill=tk.X)
spanish_button.pack(ipadx=10, ipady=10, fill=tk.X)

window.mainloop()