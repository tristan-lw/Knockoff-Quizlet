import tkinter as tk
from tkinter import *
from PIL import Image
import cv2
import numpy as np
import random
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
    text = english_words[counter]
    question(text)

def ask_question_spanish():
    text = spanish_words[counter]
    question(text)

def question(text):
    question = tk.Label(root, text=text)  
    question.pack(ipadx=10, ipady=10, fill=tk.X)

def get_answer_english():
    global counter
    print(spanish_words[counter])
    if answer.get() == spanish_words[counter]:
        print("Correct")
    else:
        print("Incorrect")
    counter += 1
    ask_question_english()

def get_answer_spanish():
    global counter
    print(spanish_words[counter])
    if answer.get() == english_words[counter]:
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
    n = len(spanish_words)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        temp = spanish_words[i]
        spanish_words[i] = spanish_words[j]
        spanish_words[j] = temp
        temp = english_words[i]
        english_words[i] = english_words[j]
        english_words[j] = temp
    for word in spanish_words:
        spanish_words[spanish_words.index(word)] = word.replace("\n", "")
    for word in english_words:
        english_words[english_words.index(word)] = word.replace("\n", "")
    print(spanish_words)
    print(english_words)

def preprocess(image):
    # Preprocessing - grayscale, Gaussian blur, Otsu's threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #cv2.imwrite(path + "gray.png", gray)
    #cv2.imwrite(path + "blur.png", blur)
    #cv2.imwrite(path + "thresh.png", thresh)
    return thresh

# Initialisation
# -1 = null, 0 = english, 1 = spanish
root = tk.Tk()
root.geometry("500x500")
root.bind("<Return>", enter_key_pressed)
answer = tk.StringVar()
path = "C:/Users/Tristan/source/repos/Python/Knockoff Quizlet/"
lang = -1
counter = 0
english = cv2.imread(path + "english_image.jpg")
spanish = cv2.imread(path + "spanish_image.jpg")

english = preprocess(english)
spanish = preprocess(spanish)

data = tess.image_to_string(english, lang='eng',config='--psm 6')
lines = data.split('\n')
english_words = list(filter(None, lines))
print(english_words)

data = tess.image_to_string(spanish, lang='eng',config='--psm 6')
lines = data.split('\n')
spanish_words = list(filter(None, lines))
print(spanish_words)

#with open(path + "spanish words.txt") as file:
#    spanish = file.readlines()
#with open(path + "english words.txt") as file:
#    english = file.readlines()

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