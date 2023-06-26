import tkinter as tk
import pyTesseract
import numpy as np
from tkinter import *
import random
from PIL import Image

def initialize_english():
    hide_buttons()
    global lang
    lang = 0
    entry_box()
    ask_question_english()

def initialize_spanish():
    hide_buttons()
    global lang
    lang = 1
    entry_box()
    ask_question_spanish()

def hide_buttons():
    english_button.pack_forget()
    spanish_button.pack_forget()

def entry_box():
    answer_entry = tk.Entry(root, textvariable = answer)
    answer_entry.pack(ipadx=10, ipady=10, fill=tk.X)

def ask_question_english():
    text = english[counter]
    question(text)

def ask_question_spanish():
    text = spanish[counter]
    question(text)

def question(text):
    question = tk.Label(root, text=text)  
    question.pack(ipadx=10, ipady=10, fill=tk.X)

def get_answer_english():
    global counter
    print(spanish[counter])
    if answer.get() == spanish[counter]:
        print("Correct")
    else:
        print("Incorrect")
    counter += 1
    ask_question_english()

def get_answer_spanish():
    global counter
    print(spanish[counter])
    if answer.get() == english[counter]:
        print("Correct")
    else:
        print("Incorrect")
    counter += 1
    ask_question_spanish()

def enter_key_pressed(event):
    if lang == 0:
        print("get answer english")
        get_answer_english()
    elif lang == 1:
        print("get answer spanish")
        get_answer_spanish()

def shuffle():
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

# Initialisation
# -1 = null, 0 = english, 1 = spanish
root = tk.Tk()
root.geometry("500x500")
root.bind("<Return>", enter_key_pressed)
answer = tk.StringVar()
path = "C:/Users/Tristan/Documents/"
lang = -1
counter = 0
spanish = []
english = []
with open(path + "spanish words.txt") as file:
    spanish = file.readlines()
with open(path + "english words.txt") as file:
    english = file.readlines()
shuffle()

english_button = tk.Button(
    root,
    text = "English",
    fg = 'white',
    bg = 'gray',
    command = initialize_english)
english_button.pack(
    ipadx=10,
    ipady=10,
    fill=tk.X)
spanish_button = tk.Button(
    root,
    text = "Spanish",
    fg = 'white',
    bg = 'gray',
    command = initialize_spanish)
spanish_button.pack(
    ipadx=10,
    ipady=10,
    fill=tk.X)

root.mainloop()