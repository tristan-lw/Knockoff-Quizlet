import tkinter as tk
from tkinter import *
from PIL import Image
import cv2
import numpy as np
import random
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def initialize_english():
    hide()
    question_label.pack(ipadx=10, ipady=10, fill=tk.X, side="top")
    global lang
    lang = 0
    entry_box()
    ask_question_english()

def initialize_spanish():
    hide()
    question_label.pack(ipadx=10, ipady=10, fill=tk.X, side="top")
    global lang
    lang = 1
    entry_box()
    ask_question_spanish()

def hide():
    english_button.place_forget()
    spanish_button.place_forget()
    choose_language_label.pack_forget()
    question_label.pack_forget()
    answer_entry.pack_forget()

def entry_box():
    answer_entry.pack(ipadx=10, ipady=10, expand=True)

def clear_entry_box():
    answer_entry.delete(0,END)

def check_end_of_game():
    if counter == len(english_words):
        hide()
        text_answer = ""
        if lang == 0: # English
            for i in range(len(english_results)):
                if english_results[i] == 1: # Correct answer
                    text_answer += english_words[i] + " ✔\n"
                else: # Incorrect answer
                    text_answer += english_words[i] + " ✘\n"
        elif lang == 1:
            for i in range(len(spanish_results)):
                if spanish_results[i] == 1:
                    text_answer += spanish_words[i] + " ✔\n"
                else:
                    text_answer += english_words[i] + " ✘\n"
        text_answer += f"Score: {score}"
        final = Label(text=text_answer)
        final.place(relx=0.5,rely=0.5,anchor="center")

def ask_question_english():
    check_end_of_game()
    text = english_words[counter]
    question(text)

def ask_question_spanish():
    check_end_of_game()
    text = spanish_words[counter]
    question(text)

def question(text):
    questionVar.set(text)

def get_answer_english():
    global counter
    global score
    print(spanish_words[counter])
    if answer.get() == spanish_words[counter]:
        print("Correct")
        score += 1
        english_results[counter] = 1
    else:
        print("Incorrect")
        english_results[counter] = 0
    counter += 1
    clear_entry_box()
    ask_question_english()

def get_answer_spanish():
    global counter
    global score
    print(spanish_words[counter])
    if answer.get() == english_words[counter]:
        print("Correct")
        score += 1
        spanish_results[counter] = 1
    else:
        print("Incorrect")
        spanish_results[counter] = 0
    counter += 1
    clear_entry_box()
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
    # Preprocessing - Grayscale, Gaussian blur, Otsu's threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    cv2.imwrite(path + "gray.png", gray)
    cv2.imwrite(path + "blur.png", blur)
    cv2.imwrite(path + "thresh.png", thresh)
    cv2.imwrite(path + "opening.png", opening)
    cv2.imwrite(path + "invert.png", invert)
    return invert

# Initialisation
# -1 = null, 0 = english, 1 = spanish
root = tk.Tk()
root.geometry("500x250")
root.title("Knockoff Quizlet")
root.bind("<Return>", enter_key_pressed)
root.resizable(False, False)

answer = tk.StringVar()
answer_entry = tk.Entry(root, textvariable = answer)

questionVar = StringVar()
question_label = tk.Label(root, textvariable=questionVar)

path = "C:/Users/Tristan/source/repos/Python/Knockoff Quizlet/"
lang = -1
counter = 0
score = 0
english = cv2.imread(path + "english_image.jpg")
spanish = cv2.imread(path + "spanish_image.jpg")

english = preprocess(english)
spanish = preprocess(spanish)

data = tess.image_to_string(english, lang='eng')
#config='--psm 6'
lines = data.split('\n')
english_words = list(filter(None, lines))
print(english_words)

data = tess.image_to_string(spanish, lang='eng')
lines = data.split('\n')
spanish_words = list(filter(None, lines))
print(spanish_words)

english_results = [None] * len(english_words)
spanish_results = [None] * len(spanish_words)

shuffle()

choose_language_label = Label(root,text="Choose language", font=("Arial", 25))
choose_language_label.pack(ipadx=10, ipady=10, fill=tk.X, side="top")
#choose_language_label.place(x=124, y = 40)
english_button = tk.Button(
    root,
    text = "English",
    height = 5,
    width = 20,
    fg = "white",
    bg = "blue",
    command = initialize_english)
english_button.place(x=70, y=120)
#english_button.pack(
#    ipadx=10,
#    ipady=10,
#    fill=tk.X)
spanish_button = tk.Button(
    root,
    text = "Spanish",
    height = 5,
    width = 20,
    fg = 'yellow',
    bg = 'red',
    command = initialize_spanish)
spanish_button.place(x=280,y=120)
#spanish_button.pack(
#    ipadx=10,
#    ipady=10,
#    fill=tk.X)

root.mainloop()