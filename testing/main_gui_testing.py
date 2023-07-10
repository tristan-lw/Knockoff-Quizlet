import tkinter as tk

root = tk.Tk()
root.geometry("500x250")

choose_language_label = tk.Label(root,text="Choose your language",bg="green",fg="white")
english_button = tk.Button(root, text="English",bg="blue",fg="white")
spanish_button = tk.Button(root, text="Spanish",bg="red",fg="white")

choose_language_label.pack(ipadx=20,ipady=20,padx=10,pady=20,fill=tk.X,expand=True)
english_button.pack(ipadx=50,ipady=10,padx=50,pady=50,side="left")
spanish_button.pack(ipadx=50,ipady=10,padx=50,pady=50,side="left")

root.mainloop()