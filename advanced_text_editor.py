from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from tkinter.font import Font 
from tkinter import dialog
from tkinter import dnd
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import tix
from tkinter import ttk
from tkinter import colorchooser
from tkinter import commondialog
from tkinter import constants 
import time 
import os
import sys

window = Tk()
window.title("Text Editor")

main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)


canvas1 = Canvas(main_frame)
canvas1.pack(side=RIGHT, fill=BOTH, expand=1)

out_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas1.yview)
out_scrollbar.pack(side=LEFT, fill=Y)


canvas1.configure(yscrollcommand=out_scrollbar.set)
canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))

sec_frame  = Frame(canvas1)

canvas1.create_window((0, 0), window=sec_frame, anchor="nw")

global opened_name

def new_file():
    te.delete("1.0", END)
    window.title("Untitled")
    status_bar.config(text="New File        ")
    global opened_name
    opened_name = False

def open_file():
    
    text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("C++ Files", "*.cpp"), ("Document Files", "*.docs"), ("All Files", "*.*")))
    
    if text_file:
        te.delete("1.0", END)
        global opened_name
        opened_name = text_file

    name = text_file
    status_bar.config(text=f"{name}     ")
    window.title(f"{name} - Text Editor")
    
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    te.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfile(defaultextension=".*", title="Save File", filetypes=(("All Files", "*.*"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("C++ Files", "*.cpp"), ("Document Files", "*.docs"), ("Text Files", "*.txt")))
    if text_file:
        # msg_open = simpledialog.askstring("Where your file be saved?", "Choose a file or create it here")
        
        # my_dir = os.mkdir("C:/Users/Zaid/Desktop/{}".format(msg_open))
        name = text_file
        status_bar.config(text=f"Saved: {name}     ")
        window.title(f"{name} - Text Editor")
        
        
        text_file = open({name}, 'w')
        text_file.write(te.get(1.0, END))
        text_file.close()
    
    else:
        pass

def save_file(e):
    global opened_name
    if opened_name:
        text_file = open(opened_name, 'w')
        text_file.write(te.get(1.0, END))
        text_file.close()
        status_bar.config(text=f"Saved: {opened_name}       ")
    else:
        save_as_file()

def full_screen_text():
    window.attributes("-fullscreen", True)
    te.config(width=126, height=40)

    def exit_fullscreen_text():
        te.config(width=126, height=31)
        window.attributes("-fullscreen", False)
        btn_exit.destroy()

    btn_exit = Button(frame, text="Exit fullscreen text", padx=10, font="Calibri 15 bold", command=exit_fullscreen_text)
    btn_exit.grid(row=0, column=5)

    def hover5(e):
        btn_exit.config(bg="black", fg="white")

    def leave5(e):
        btn_exit.config(bg="SystemButtonFace", fg="black")

    btn_exit.bind("<Enter>", hover5)
    btn_exit.bind("<Leave>", leave5)


def full_screen():
    window.attributes("-fullscreen", True)

    def exit_full_screen():
        window.attributes("-fullscreen", False)
        btn100.destroy()

    btn100 = Button(frame, text="Exit full screen", padx=16, font="Calibri 15 bold", command=exit_full_screen)
    btn100.grid(row=0, column=4)

    def hovers4(e):
        btn100.config(bg="black", fg="white")

    def leaves4(e):
        btn100.config(bg="SystemButtonFace", fg="black")

    btn100.bind("<Enter>", hovers4)
    btn100.bind("<Leave>", leaves4)

def cut_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    else:
        if te.selection_get():
            selected = te.selection_get()
            te.delete("sel.first", "sel.last")
            window.clipboard_clear()
            window.clipboard_append(selected)
        

def copy_text(e):
    global selected
    if e:
        selected = window.clipboard_get()

    if te.selection_get():
        selected = te.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)


def paste_text(e):  
    global selected
    if e:
        selected = window.clipboard_get()
    else:
        if selected:
            position = te.index(INSERT)
            te.insert(position, selected)

def sss():
    # typc = messagebox.askokcancel("Opening Settings", "Do you want open settings?")
    # if typc == True:
    global window2
    window2 = Tk()
    window2.title("Settings")

    global entry1, entry2, entry3, entry4, entry5, entry6

    main_frame1 = Frame(window2)
    main_frame1.pack(fill=BOTH, expand=1)

    canvas2 = Canvas(main_frame1)
    canvas2.pack(side=LEFT, fill=BOTH, expand=1)

    out_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=canvas2.yview)
    out_scrollbar1.pack(side=RIGHT, fill=Y)

    canvas2.configure(yscrollcommand=out_scrollbar1.set)
    canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

    sec_frame2  = Frame(canvas2)

    canvas2.create_window((0, 0), window=sec_frame2, anchor="nw")

    def fun1():
        tefon = Font(family=entry2.get(),
                     size=entry1.get(),
                     weight=entry3.get())

        te.config(font=tefon, width=126, height=31)

    def fun2():
        te.config(font="Calibri 15 bold", width=139, height=30)

    def fun3():
        te.config(font="Arial 15 bold", height=30, width=126)

    def fun4():
        te.config(font="Times 15 bold", width=139, height=31)
    
    def fun5():
        te.config(font="SansSerif 15 bold", width=126, height=31)

    def fun6():
        te.config(font="SegoeUI 15 bold", width=126, height=30)

    def fun7():
        te.config(font="BankGothicMdBT 15 bold", width=126, height=29)

    def fun8():
        te.config(font="Georgia 15 bold", width=99, height=30)
    
    def fun9():
        te.config(font="impact 15 bold", width=116, height=29)

    frame2 = Frame(sec_frame2)
    frame2.grid()

    ttt = Label(frame2, text="      Font:      ", font="Calibri 15 bold")
    ttt.grid(row=0, column=0, columnspan=13)

    lab = Label(frame2, text="Font Family:    ", font="Calibri 13 bold")
    lab.grid(row=1, column=0, padx=4, pady=5)

    entry2 = Entry(frame2, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry2.grid(row=1, column=1, padx=4, pady=5)

    # btn122 = Button(frame2, text="Apply", font='Calibri 10 bold',  border=1, command=fun1)
    # btn122.grid(row=1, column=1, padx=4, pady=10)


    # lbl1 = Label(entry2, text="Font Family: ", font="Calibri 12 bold", state=DISABLED)

    # entry2.insert(END, lbl1)

    def func1():
        te.config(width=126, height=31, font="Consolas 15 bold")

    def func2():
        tefont = Font(size=entry1.get(), 
                      family=entry2.get(),
                      weight=entry3.get())        

        te.config(font=tefont, width=174, height=40)

    def func3():
        te.config(font=("Consolas", 14), width=139, height=33)

    def func4():
        te.config(font=("Consolas", 16), width=116, height=30)

    def func5():
        te.config(font="Consolas 18", width=107, height=25)

    def func6():
        te.config(font="Consolas 20", width=92, height=22)

    def func7():
        te.config(font="Consolas 24", width=77, height=19)

    def func8():
        te.config(font="Consolas 28", width=69, height=17)

    def func9():
        te.config(font="Consolas 32", width=58, height=14)

    def func10():
        te.config(font="Consolas 36", width=53, height=13)

    def func11():
        te.config(font="Consolas 40", width=48, height=12)

    def func12():
        te.config(font="Consolas 48", width=39, height=10)

    def func13():
        te.config(font="Consolas 72", width=26, height=6)


    frames = Frame(sec_frame2)
    frames.grid()

    label1 = Label(frames, text="      Font Size:      ", font="Calibri 15 bold")
    label1.grid(row=2, column=0, columnspan=13)

    lab1 = Label(frames, text="Size:        ", font="Calibri 13 bold")
    lab1.grid(row=3, column=0, padx=4, pady=10)

    entry1 = Entry(frames, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry1.grid(row=3, column=1, padx=4, pady=10)

    # btn = Button(frames, text="Apply", font='Calibri 10 bold',  border=1, command=func2)
    # btn.grid(row=3, column=2, padx=4, pady=10)

    frm2 = Frame(sec_frame2)
    frm2.grid()

    Lbl = Label(frm2, text="      Text Width & Height:      ", font="Calibri 15 bold")
    Lbl.grid(row=0, column=0, columnspan=13)

    lbls = Label(frm2, text="Width:    ", font="Calibri 13 bold")
    lbls.grid(row=1, column=0, padx=4, pady=5)

    entry4 = Entry(frm2, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry4.grid(row=1, column=1, padx=4, pady=5)
    
    lbls1 = Label(frm2, text="Height:    ", font="Calibri 13 bold")
    lbls1.grid(row=2, column=0, padx=4, pady=5)

    entry5 = Entry(frm2, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry5.grid(row=2, column=1, padx=4, pady=5)


    def apply():
        global tef
        tef = Font(
            family=entry2.get(),
            size=entry1.get(),
            weight=entry3.get(),
            slant=entry6.get()
        )
        te.config(font=tef, width=entry4.get(), height=entry5.get(), cursor=entry7.get())

    def editation():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        gt1 = entry1.get()
        entry1.insert(END, gt1)
        gt2 = entry2.get()
        entry2.insert(END, gt2)
        gt3 = entry3.get()
        entry3.insert(END, gt3)
        gt4 = entry4.get()
        entry4.insert(END, gt4)
        gt5 = entry5.get()
        entry5.insert(END, gt5)
        gt6 = entry6.get()
        entry6.insert(END, gt6)

    frm = Frame(sec_frame2)
    frm.grid()

    labell = Label(frm, text="      Font Style:      ", font="Calibri 15 bold")
    labell.grid(row=0, column=0, columnspan=13)

    lbls2 = Label(frm, text="Bold or normal:    ", font="Calibri 13 bold")
    lbls2.grid(row=1, column=0, padx=4, pady=5)

    entry3 = Entry(frm, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry3.grid(row=1, column=1, padx=4, pady=5)

    lbls3 = Label(frm, text="Italic or roman:    ", font="Calibri 13 bold")
    lbls3.grid(row=2, column=0, padx=4, pady=5)

    entry6 = Entry(frm, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry6.grid(row=2, column=1, padx=4, pady=5)

    lbls4 = Label(frm, text="Cursor Style:    ", font="Calibri 13 bold")
    lbls4.grid(row=3, column=0, padx=4, pady=5)

    entry7 = Entry(frm, width=30, font="Consolas 14", fg="black", bg="white", selectforeground="black", selectbackground="light gray", insertbackground="black", insertwidth=3)
    entry7.grid(row=3, column=1, padx=4, pady=5)

    btn_app = Button(frm, text="Apply all font changes", font='Calibri 10 bold',  border=1, command=apply)
    btn_app.grid(row=4, column=0, padx=4, pady=10)

    button1 = Button(frm, text="Font Defaults", font='Calibri 10 bold', border=1, command=func1)
    button1.grid(row=4, column=2, padx=4, pady=10)

    editation()

    def function1():
        window.geometry("1080x720")

    def function2():
        window.geometry("450x300")

    def function3():
        window.geometry("450x400")

    def function4():
        window.geometry("500x500")

    def function5():
        window.geometry("600x400")

    def function6():
        window.geometry("750x550")

    def function7():
        window.geometry("850x600")

    def function8():
        window.geometry("900x750")    

    def function9():
        window.geometry("1080x720")

    def function10():
        window.geometry("1200x800")

    def function11():
        window.geometry("1280x880")

    def function12():
        window.geometry("1440x880")

    def function13():
        window.geometry("1500x950")

    frm1 = Frame(sec_frame2)
    frm1.grid()

    label2 = Label(frm1, text="      Window Size:      ", font="Calibri 15 bold")
    label2.grid(row=0, column=0, columnspan=15)

    button13 = Button(frm1, text="Default window size", font='Calibri 10 bold', command=function1)
    button13.grid(row=3, column=1, padx=8, pady=10)

    button14 = Button(frm1, text="450x300", font='Calibri 10 bold', command=function2)
    button14.grid(row=3, column=2, padx=4, pady=10)

    button15 = Button(frm1, text="450x400", font='Calibri 10 bold', command=function3)
    button15.grid(row=3, column=3, padx=4, pady=10)

    button16 = Button(frm1, text="500x500", font='Calibri 10 bold', command=function4)
    button16.grid(row=3, column=4, padx=4, pady=10)

    button17 = Button(frm1, text="600x400", font='Calibri 10 bold', command=function5)
    button17.grid(row=3, column=5, padx=4, pady=10)

    button18 = Button(frm1, text="750x550", font='Calibri 10 bold', command=function6)
    button18.grid(row=3, column=6, padx=4, pady=10)

    button19 = Button(frm1, text="850x600", font='Calibri 10 bold', command=function7)
    button19.grid(row=3, column=7, padx=4, pady=10)

    button20 = Button(frm1, text="900x750", font='Calibri 10 bold', command=function8)
    button20.grid(row=3, column=8, padx=4, pady=10)

    button21 = Button(frm1, text="1080x720", font='Calibri 10 bold', command=function9)
    button21.grid(row=3, column=9, padx=4, pady=10)

    button22 = Button(frm1, text="1200x800", font='Calibri 10 bold', command=function10)
    button22.grid(row=3, column=10, padx=4, pady=10)

    button23 = Button(frm1, text="1280x880", font='Calibri 10 bold', command=function11)
    button23.grid(row=3, column=11, padx=4, pady=10)

    button24 = Button(frm1, text="1440x880", font='Calibri 10 bold', command=function12)
    button24.grid(row=3, column=12, padx=4, pady=10)

    button25 = Button(frm1, text="1500x950", font='Calibri 10 bold', command=function13)
    button25.grid(row=3, column=13, padx=4, pady=10)

    

    # def fun01():
    #     te.config(font=())

    # lab1 = Label(frame2, text="      Font Style:      ", font="Calibri 15 bold")
    # lab1.grid(row=2, column=0, columnspan=9)

    # btn10 = Button(frame2, text="Bold", font="Calibri 10 bold", command=fun01)
    # btn10.grid(row=3, column=0, padx=8, pady=10)

    window2.geometry("1000x650")
    window2.mainloop()

    # else:
    #     pass

def rtrt():
    te.delete(1.0, END)

def theme():
    global window3
    window3 = Tk()
    window3.title("Themes")

    frame4 = Frame(window3)
    frame4.grid(row=0, column=0, pady=5)

    def Dark():
        te.config(bg="black", fg="White", width=126, height=31, selectbackground="white", selectforeground="black", insertbackground="White", insertwidth=2)

    def Light():
        te.config(bg="white", fg="black", width=126, height=31, selectforeground="blacK", selectbackground="light gray", insertbackground="black", insertwidth=2)

    def navy_dark():
        te.config(bg='navy', fg="dark orange", width=126, height=31, selectbackground="royalblue", selectforeground="dark orange", insertbackground="White", insertwidth=2)

    def hv(e):
        button1.config(bg="SystemButtonFace", fg="black")

    def lv(e):
        button1.config(bg="black", fg="SystemButtonFace")

    def hv1(e):
        button2.config(bg="black", fg="white")

    def lv1(e):
        button2.config(bg="SystemButtonFace", fg="black")

    def hv2(e):
        button3.config(fg="black", bg="SystemButtonFace")

    def lv2(e):
        button3.config(bg="navy", fg="dark orange")

    mylbl = Label(frame4, text="     Themes:     ", font="Calibri 15 bold")
    mylbl.grid(row=0, column=0)

    button1 = Button(frame4, text="Dark", font="Calibri 15 bold", fg="white", bg="black", command=Dark)
    button1.grid(row=1, column=0, padx=4, ipadx=8)

    button2 = Button(frame4, text="Light", font="Calibri 15 bold", command=Light)
    button2.grid(row=1, column=1, padx=4, ipadx=8)

    Label(frame4, text="\t").grid(row=2, column=0)

    button3 = Button(frame4, text="Navy Dark", fg="dark orange", bg="navy", font="Calibri 15 bold", command=navy_dark)
    button3.grid(row=2, column=0, padx=10, ipadx=1, pady=8)

    button1.bind("<Enter>", hv)
    button1.bind("<Leave>", lv)

    button2.bind("<Enter>", hv1)
    button2.bind("<Leave>", lv1)

    button3.bind("<Enter>", hv2)
    button3.bind("<Leave>", lv2)

    window3.geometry("230x140")
    window3.mainloop()

def hovers(e):
    btn1.config(bg="black", fg="white")

def leaves(e):
    btn1.config(bg="SystemButtonFace", fg="black")

def hovers1(e):
    btn2.config(bg="black", fg="white")

def leaves1(e):
    btn2.config(bg="SystemButtonFace", fg="black")

def hovers2(e):
    btn3.config(bg="black", fg="white")

def leaves2(e):
    btn3.config(bg="SystemButtonFace", fg="black")

def hovers3(e):
    btn4.config(bg="black", fg="white")

def leaves3(e):
    btn4.config(bg="SystemButtonFace", fg="black")


def wait():
    msg = messagebox.askyesno("Exit", "Are you sure that you want to exit this program?")
    if msg == True:
        window.destroy()
    else:
        pass

frame2_out = Frame(sec_frame)
frame2_out.pack(padx=5, pady=5)

text_scroll = Scrollbar(frame2_out)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(frame2_out, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

te = Text(frame2_out, width=126, height=31, borderwidth=2, font="Consolas 15 bold", fg="White", bg="black", selectbackground="white", selectforeground="black", insertbackground="White", undo=True, insertwidth=2, xscrollcommand=hor_scroll.set, yscrollcommand=text_scroll.set, wrap="none")
te.pack(padx=2, pady=2)

text_scroll.config(command=te.yview)
hor_scroll.config(command=te.xview)

frame = Frame(sec_frame)
frame.pack(pady=10)

menu11 = Menu(window)
window.config(menu=menu11)

def exiit():
    e = messagebox.askyesno("Exit program", "Are you sure you want to exit program?")
    if e == False:
        pass
    else:
        window.destroy() 

file_menu = Menu(menu11, tearoff=False)
menu11.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New                            ", command=new_file)
file_menu.add_command(label="Open                           ", command=open_file)
file_menu.add_command(label="Save                ", command= lambda: save_file(False), accelerator="Ctrl+s")
file_menu.add_command(label="Save As                            ", command=save_as_file)
file_menu.add_command(label="Full screen text               ", command=full_screen_text)
file_menu.add_command(label="Full screen                    ", command=full_screen)
file_menu.add_command(label="Settings                       ", command=sss)
file_menu.add_separator()
file_menu.add_command(label="Exit               ", command=exiit, accelerator="Ctrl+w")


edit_menu = Menu(menu11, tearoff=False)
menu11.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut                ", command=lambda: cut_text(False), accelerator="Ctrl+x")
edit_menu.add_command(label="Copy               ", command=lambda: copy_text(False), accelerator="Ctrl+c")
edit_menu.add_command(label="Paste              ", command=lambda: paste_text(False), accelerator="Ctrl+v")
edit_menu.add_command(label="Theme                          ", command=theme)

edit_menu.add_separator()
edit_menu.add_command(label="Undo               ", command=te.edit_undo, accelerator="Ctrl+z")
edit_menu.add_command(label="Redo               ", command=te.edit_redo, accelerator="Ctrl+y")

status_bar = Label(window, text="Ready  ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

btn1 = Button(frame, text="Settings", padx=11, font="Calibri 15 bold", command=lambda: sss())
btn1.grid(row=0, column=0)

btn4 = Button(frame, text="Theme", padx=17, font="Calibri 15 bold", command=theme)
btn4.grid(row=0, column=1)

btn2 = Button(frame, text="Clear", padx=19, font="Calibri 15 bold", command=rtrt)
btn2.grid(row=0, column=2)

btn3 = Button(frame, text="Exit", padx=21, font="Calibri 15 bold", command=wait)
btn3.grid(row=0, column=3)

window.bind("<Control-s>", save_file)

btn1.bind("<Enter>", hovers)
btn1.bind("<Leave>", leaves)

btn2.bind("<Enter>", hovers1)
btn2.bind("<Leave>", leaves1)

btn3.bind("<Enter>", hovers2)
btn3.bind("<Leave>", leaves2)

btn4.bind("<Enter>", hovers3)
btn4.bind("<Leave>", leaves3)


def ii(e):
    e1 = messagebox.askyesno("Exit program", "Are you sure you want to exit program?")
    if e1 == False:
        pass
    else:
        window.destroy()

window.bind("<Control-w>", ii)


window.geometry("1080x720")
window.mainloop()