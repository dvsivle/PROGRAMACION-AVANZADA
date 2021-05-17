# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:10:32 2020

@author: MERANONIMOK
"""

#%%


import tkinter as tk
import tkinter.ttk as ttk
from random import randrange, uniform

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Tk Animation App')
        self.master.resizable(0,0)
       
        
        self.WIDTH = 300
        self.HEIGHT = 400
        self.SIZE = 10
        
        self.x = randrange(1,self.WIDTH)
        self.y = randrange(1,self.HEIGHT)
        self.dx = uniform(-10,10)
        self.dy = uniform(-10,10)
        
        
        self.canvas = tk.Canvas(self.master, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        
        self.canvas.create_oval(self.x, self.y, self.x + self.SIZE,self.y + self.SIZE, fill='blue')
           
        
        self.animate_canvas()   #Método 2 para iniciar la animación
        
    def animate_canvas(self):
        self.update_graph()
        
    def update_graph(self):
        self.canvas.delete(tk.ALL)
        
        if self.x < 0 or self.WIDTH < (self.x +self.SIZE):
            self.dx = -self.dx
            
        if self.y < 0 or self.HEIGHT < (self.y +self.SIZE):
            self.dy = -self.dy
            
        self.x = self.x + self.dx
        self.y = self.y + self.dy
            
        self.canvas.create_oval(self.x, self.y, self.x + self.SIZE,self.y + self.SIZE, fill='blue')
        
        self.master.after(50, self.animate_canvas)
            
        
        
        
        
        
root = tk.Tk()
app = App(root)
#app.animate_canvas()   #Método 1 para iniciar la animación
root.mainloop()
