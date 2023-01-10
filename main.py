import tkinter as tk
from datetime import datetime
from sample_texts import texts
import random

start_time = 0


def highlight_mistake():
    # Get the text entered by the user
    user_text = writing_space.get(1.0, "end").strip()
    # Get the test text
    test_text = text_tk.cget("text").strip()
    # remove new line character '\n' from both texts
    user_text = user_text.replace("\n", " ")
    test_text = test_text.replace("\n", " ")
    # Split both text into list of words
    user_text_list = user_text.split(" ")
    test_text_list = test_text.split(" ")

    for i, word in enumerate(user_text_list):
        if word != test_text_list[i]:
            # Find the index of the wrong word in the user_text
            start = user_text.index(word)
            end = start + len(word)
            # Add a tag to the range of the wrong word
            writing_space.tag_add("mistake", f"1.{start}", f"1.{end}")

    # Configure the appearance of the mistake tag
    writing_space.tag_config("mistake", background="red")


def finish():
    global start_time
    if writing_space.get(1.0, 'end').strip() == text_tk.cget("text").strip():
        end_time = datetime.now()
        time_taken = end_time - start_time
        words = writing_space.get(1.0, "end").strip().split(" ")
        typing_speed = len(words) / (time_taken.total_seconds() / 60)
        label_state.config(text=f"Your speed is: {typing_speed:.3} WPM")
    else:
        label_state.config(text="Please finish the text or make sure you don't have any mistakes.")
        highlight_mistake()


def start():
    global start_time
    start_time = datetime.now()
    writing_space.config(state=tk.NORMAL)
    label_state.config(text="Test in progress.")


window = tk.Tk()
window.title("Typing speed test")
window.minsize(width=800, height=600)

text = random.choice(texts)

text_tk = tk.Label(window, text=text, font=('Arial', 18), wraplength=730)
text_tk.grid(row=0, column=0, padx=50)

write_label = tk.Label(window, text="Write the text that is shown above.", font=('Arial', 14))
write_label.grid(row=1, column=0, pady=20)

start_btn = tk.Button(window, text="Start", padx=20, command=start)
start_btn.grid(row=2, column=0, pady=10)

writing_space = tk.Text(window, wrap='word')
writing_space.config(state=tk.DISABLED)
writing_space.grid(row=3, column=0, pady=10)

finish_btn = tk.Button(window, text="Finish", padx=20, command=finish)
finish_btn.grid(row=4, column=0, pady=10)

label_state = tk.Label(window, text="Test hasn't started.")
label_state.grid(row=5, column=0)

window.mainloop()
