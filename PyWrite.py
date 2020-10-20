import os
from tkinter import *


class PyWrite:
    __root = Tk()
    __thisWidth = 500
    __thisHeight = 700
    __thisTextArea = Text(__root)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __thisStatusBar = Label(__root)
    __appleMenuBar = Menu(__root)
    __appleMenuBarDropDown = Menu(__appleMenuBar, name="apple")
    __appleMenuBar.add_cascade(menu=__appleMenuBarDropDown)
    __file = None
    __charCount = 0

    def __init__(self, **kwargs):
        # icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Foreground and Background
        try:
            self.__thisTextArea['background'] = kwargs['bgcolor']
            if kwargs['bgcolor'] == "black":
                self.__thisTextArea['insertbackground'] = 'white'
        except KeyError:
            pass
        try:
            self.__thisTextArea['foreground'] = kwargs['fgcolor']
        except KeyError:
            pass

        # Width and Height
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Center the Window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry(f"{self.__thisWidth}x{self.__thisHeight}+{int(left)}+{int(top)}")

        # Make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add Controls
        self.__thisTextArea.grid(sticky=N + E + S + W)
        self.__thisStatusBar.grid(sticky=W + S)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # Add Apple Menubar
        # see https://tkdocs.com/tutorial/menus.html

        # Add Commands
        self.__thisTextArea.bind("<Key>", self.__key)
        self.__thisTextArea.bind("<Control-A>", self.__ctrl)

        # Set title
        self.__root.title("PyWrite - [New Document]")

    def __ctrl(self, event):
        print("Gotcha bitch!")
        pass

    def __key(self, event):
        self.__charCount = len(self.__thisTextArea.get("1.0", "end-1c"))
        self.__thisStatusBar['text'] = self.__charCount
        pass

    def __quit(self):
        self.__root.destroy()

    def __newFile(self):
        pass

    def __saveFile(self):
        pass

    def __openFile(self):
        pass

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()


pyWrite = PyWrite(width=600, height=800, fgcolor="green", bgcolor="black")
pyWrite.run()
