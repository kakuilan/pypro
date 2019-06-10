#!/usr/bin/python3
# coding: utf-8
# 简单的GUI文本编辑器

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import matplotlib

def load():
  with open(filename.get()) as file:
    contents.delete('1.0', END)
    contents.insert(INSERT, file.read())

def save():
  with open(filename.get(), 'w') as file:
    file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

matplotlib.use('Agg')
mainloop()

