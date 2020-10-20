import platform
import re
from tkinter import *


class PyWrite:
    __root = Tk()
    __root.attributes("-fullscreen", True)
    __root.minsize(400, 400)
    __thisFullscreenState = False
    __thisWidth = 500
    __thisHeight = 700
    __thisTextArea = Text(__root,
                          font=('*Font', '14'),
                          padx=0,
                          pady=0,
                          borderwidth=0,
                          highlightthickness=0,
                          relief=FLAT,
                          wrap=WORD)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __thisStatusBar = Label(__root,
                            font=('*Font', '14'),
                            padx=0,
                            pady=0,
                            borderwidth=0,
                            highlightthickness=0,
                            relief=FLAT)
    __thisMenuBar = Menu(__root)
    __thisAppMenu = Menu(__thisMenuBar, name='apple')
    __thisMenuBar.add_cascade(menu=__thisAppMenu)
    __file = None
    __charCount = 0
    __charCountGoal = None
    __wordCount = 0
    __wordCountGoal = None

    def __init__(self, **kwargs):
        # icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Foreground and Background
        try:
            self.__thisTextArea['background'] = kwargs['bgcolor']
            self.__root['background'] = kwargs['bgcolor']
            self.__thisStatusBar['background'] = kwargs['bgcolor']
            if kwargs['bgcolor'] == "black":
                self.__thisTextArea['insertbackground'] = 'white'
        except KeyError:
            pass
        try:
            self.__thisTextArea['foreground'] = kwargs['fgcolor']
            self.__thisStatusBar['foreground'] = kwargs['fgcolor']
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
        self.__thisTextArea.grid(sticky=N + E + W + S)
        self.__thisStatusBar.grid(sticky=W + S)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        if platform.system() == 'Darwin':
            # Add Apple Menubar
            # this still shows as 'Python' by default, instead of PyWrite.
            # according to https://tkdocs.com/tutorial/menus.html, renaming the binary should fix this
            self.__root['menu'] = self.__thisMenuBar
        elif platform.system() == 'Linux':
            # Linux Menu Options Here
            pass
        else:
            # Windows Menu Options by Default
            pass

        # Add Commands
        self.__thisTextArea.bind("<Key>", self.__key)
        self.__thisTextArea.bind("<Control-A>", self.__ctrl)

        # Set title
        self.__root.title("PyWrite - [New Document]")

    def __toggleFullscreen(self, event=None):
        self.__thisFullscreenState = not self.__thisFullscreenState
        self.__root.attributes("-fullscreen", self.__thisFullscreenState)
        return "break"

    def __ctrl(self, event=None):
        print("Still trying to figure out how control bindings work...")
        pass

    def __key(self, event=None):
        if event:
            pass
        allText = self.__thisTextArea.get("1.0", "end-1c")
        self.__charCount = len(allText)
        self.__wordCount = len(allText.strip().split(" "))

        charCountLabel = f"{self.__charCount}" if not self.__charCountGoal \
            else f"{self.__charCount} / {self.__charCountGoal}"

        wordCountLabel = f"{self.__wordCount}" if not self.__wordCountGoal \
            else f"{self.__wordCount} / {self.__wordCountGoal}"

        self.__thisStatusBar['text'] = charCountLabel + "\t" + wordCountLabel

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


pyWrite = PyWrite(width=800, height=800, fgcolor="green", bgcolor="black")
pyWrite.run()
