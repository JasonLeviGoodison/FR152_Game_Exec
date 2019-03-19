import Tkinter as tk
import random
import os
from cols import allCols

curIndex = 0

# READ THE FILES
"""
for i in range(1, 7):
    path = os.path.realpath(__file__)
    with open(path[:len(path) - 7] + "/../columns/" + str(i) + ".txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    allCols[i - 1] = content
"""

def nextWord():
    global curIndex, label
    length = len(allCols[curIndex])
    i = random.randint(0, length - 1);
    label.config(text="From column " + str(curIndex + 1) + ": " + allCols[curIndex][i])
    #print "Element I got was " + )
    curIndex = (curIndex + 1) % 6
    #print "next index is " + str(curIndex)


root = tk.Tk()
root.title("Bingo game")
label = tk.Label(root, fg="dark green")

button = tk.Button(root, text="Next", width=25, command=nextWord)
label.pack()
button.pack()
root.mainloop()
