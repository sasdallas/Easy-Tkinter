import tkinter
import sys
from tkinter import *
import tkinter.messagebox as tkMessageBox
print("Module: EASY TKINTER Loaded Successfully!")
global Started
Started = False
def init():
    print("Initalized Easy Tkinter")
    started = True
    w = tkinter.Tk()
def window_title(title):
    print("Changing Window Title...")
    w.title(title)
def create_button(text, function):
    print("Started Module Function: Create Button")
    if not function == False:
         b = tkinter.Button(w, text = text, command = function)
    elif function == False:
        b = tkinter.Button(w, text = text)
    b.pack()
def create_canvas(bg, height, width):
    print("Started Module Function: Create Canvas")
    c = tkinter.Canvas(w, bg = bg, height = height, width = width)
    c.pack()
def draw_canvas(coord, color, start, extent):
    print("Started Module Function: Draw On Canvas")
    
    arc = c.create_arc(coord, start = start, extent = extent, fill = color)
def create_checkbutton(text, onvalue, offvalue, height, width):
    print("Started Module Function: Create Checkbutton")
    CheckVar = IntVar()
    chb = tkinter.Checkbutton(w, text = text, varible = CheckVar, onvalue = onvalue, offvalue = offvalue, height = height, width = width)
    chb.pack()
def create_entry(bd):
    print("Started Module Function: Create Entry")
    ent = tkinter.Entry(w, bd = bd)
    ent.pack()
def create_frame():
    print("Started Module Function: Create Frame")
    print("Alert: This Func Is Useless. No buttons will connect to this frame") 
    f = tkinter.Frame(w)
    f.pack()
def create_label(text):
    print("Started Module Function: Create Label")
    lb = tkinter.Label(w, text = text)
    lb.pack()
def create_listbox():
    print("Started Module Function: Create Listbox")
    print("Use add_listitem(number, text) to add items")
    lbox = tkinter.listbox(w)
def add_listitem(number, text):
    print("Started Module Function: Add Listitem")
    lbox.insert(number, text)
def create_menubutton(text):
    print("Started Module Function: Add Menubutton")
    print("Use Add_menucheckbutton to add Menu Checkbutton")
    mbutton = tkinter.menubutton(w, text = text)
    mbutton.grid()
    mbutton.menu = tkinter.menu(mbutton, tearoff = 0)
    mb["menu"] = mb.menu
    mb.pack()
def add_menucheckbutton(label):
    print("Started Module Function: Add Menu Checkbutton")   
    MenuVar = IntVar()
    mb.menu.add_checkbutton(label = label, varible = MenuVar)
def create_menu():
    print("Started Module Function: Create Menu")
    print("Use add_menucommand to add a menu command.")
    print("Use add_menuseparator to add a menu separator")
    print("Use add_menucascade to add a menu cascade")
    print("Menupart is the default cascade")
    menu1 = tkinter.menu(w)
    menupart = tkinter.menu(menu1, tearoff = 0)
    menu1.pack()
def add_menucommand(label, command):
    print("Started Module Function: Add Menucommand")
    menupart.add(label=label, command=command)
    w.config(menu=menu1)
def add_menuseparator(cascade):
    print("Started Module Function: Add Menu Separator")    
    cascade.add_separator()
    w.config(menu=menu1)
def add_menucascade(name, label, menu):
    print("Started Module Function: Add Menu Cascade")  
    menu1.add_cascade(label=label, menu=menu)
    menu = tkinter.menu(menu1, tearoff = 0)
    w.config(menu=menu1)
