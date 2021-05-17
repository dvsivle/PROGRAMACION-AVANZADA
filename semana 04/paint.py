# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:32:42 2020

@author: MERANONIMOK
"""

#%%

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import tkinter.messagebox
import tkinter.font
    
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint App")
        
        self.drawing_tool = 'pencil'
        self.left_but = 'up'
        self.x_pos, self.y_pos = None, None
        self.x_ini, self.y_ini = None, None
        self.drawing_color = 'black'
        
        self.canvas = tk.Canvas(self.master, width=800, height=800, bg='white')
        self.canvas.pack()
        
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_button_up)
        self.canvas.bind("<Motion>", self.motion)
        self.canvas.bind("<ButtonPress-3>", self.pick_color)
        
        
    def pick_color(self, handle):
        color_selected = askcolor()
        self.drawing_color = color_selected[1]
        
        
    def left_but_down(self, handle):
        self.left_but = 'down'
        
    
    def left_button_up(self, handle):
        self.left_but = 'up'
    
        self.x_pos, self.y_pos = None, None
    
    
    def motion(self, handle):
        # Se mueve el puntero con el boton presionado
        if self.drawing_tool == 'pencil':
            self.pencil_draw(handle)
            
    
    def pencil_draw(self, handle):
        if self.left_but == 'down':
            if self.x_pos is not None and self.y_pos is not None:
                self.canvas.create_line(self.x_pos, self.y_pos, 
                                        handle.x, handle.y, 
                                        smooth=tk.TRUE, fill=self.drawing_color)
            
            self.x_pos = handle.x
            self.y_pos = handle.y
            
    
    
        
root = tk.Tk()
app = App(root)
root.mainloop()