# converting chuck norris jokes into a tkinter program
from tkinter import *
import requests

root = Tk()
root.geometry("1500x550")
root.title("Chuck Norris Jokes Generator")
root.config(bg="#32dd6e")
# tkinter labels
label = Label(root, text="Chuck Norris Jokes", bg="#32dd6e", fg="white", font=("Helvertica", 25, "bold"))
label.place(relx=0.39, rely=0.1)
# chuck norris joke label
joke = Label(root, fg="white", bg="#32dd6e")
joke.place(relx=0.1, rely=0.25)
# generator function
def generate():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    data = response.json()
    joke.config(text=data['value'], font=("Helvertica", 12, "bold"))

# button
btn = Button(root, text="Push Me", fg="white", bg="#32dd6e", font=("Helvertica", 15), padx=15, pady=10, borderwidth=5, command=generate)
btn.place(relx=0.47, rely=0.45)

root.mainloop()