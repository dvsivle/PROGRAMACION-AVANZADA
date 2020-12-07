# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:55:29 2020

@author: MERANONIMOK
"""
#%%

import tkinter as tk
import tkinter.ttk as ttk
from random import randrange

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Tk Animation App')
        self.master.resizable(0,0)
        #self.master.geometry('+100+150')
        
        self.WIDTH = 300
        self.HEIGHT = 400
        self.SIZE = 10
        
        self.x = randrange(1,self.WIDTH)
        self.y = randrange(1,self.HEIGHT)
        
        self.canvas = tk.Canvas(self.master, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        
        self.canvas.create_oval(self.x, self.y, self.x + self.SIZE,self.y + self.SIZE, fill='blue')
        self.canvas.create_rectangle(10,10,30,30)
        self.canvas.bind('<Button-1>', self.update_graph)
        
    def update_graph(self, handle):
        xpos, ypos = handle.x, handle.y
        
        if self.x < xpos < self.x +self.SIZE and self.y < ypos <self.y + self.SIZE:
            self.canvas.delete(tk.ALL)
            self.x = randrange(1,self.WIDTH)
            self.y = randrange(1,self.HEIGHT)
            self.canvas.create_oval(self.x, self.y, self.x + self.SIZE,self.y + self.SIZE, fill='blue')
        
            
        
        
        
        
root = tk.Tk()
app = App(root)
root.mainloop()
