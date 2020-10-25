import platform
import re
from tkinter import *


class PyWrite:
    __root = Tk()
    __root.attributes("-fullscreen", False)     # set to false for now until we can get a handle on
    __root.minsize(400, 400)
    __thisFullscreenState = False
    __thisWidth = 500
    __thisHeight = 700
    __thisTextArea = Text(__root,
                          font=('Courier New', '12'),     # Default font needs to be Courier New, 12 pt
                          padx=0,
                          pady=0,
                          borderwidth=0,
                          highlightthickness=0,
                          relief=FLAT,
                          wrap=WORD)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __thisStatusBar = Label(__root,
                            font=('Verdana', '8'),
                            padx=0,
                            pady=0,
                            borderwidth=0,
                            highlightthickness=0,
                            relief=FLAT)
    __thisMenuBar = Menu(__root)
    __thisAppMenu = Menu(__thisMenuBar, name='apple')
    __thisMenuBar.add_cascade(menu=__thisAppMenu)
    __file = None
    __stats = {
        "characters": {
            "re": r".",
            "count": 0,
            "goal": None
        },
        "lines": {
            "re": r"[^\n\r\0]+",
            "count": 0,
            "goal": None
        },
        "paragraphs": {
            "re": r"(\n|^)[^\n\r\0]+",
            "count": 0,
            "goal": None
        },
        "pages": {
            "re": None,
            "formula": None,
            "count": 0,
            "goal": None
        },
        "words": {
            "re": r"\w+",
            "count": 0,
            "goal": None
        }
    }

    def __init__(self, **kwargs):
        # icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Foreground and Background
        try:
            self.__thisTextArea['background'] = "#000000"
            self.__root['background'] = "#000000"
            self.__thisStatusBar['background'] = "#0f0f0f"
        except KeyError:
            pass
        try:
            self.__thisTextArea['foreground'] = "#d1a000"
            self.__thisStatusBar['foreground'] = "#3f3f3f"
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
        # BIG OL TODO HERE:
        # - how to capture special key combinations separately from the global key-capture of the textarea...
        print("Still trying to figure out how control bindings work...")
        pass

    def __key(self, event=None):
        __text = self.__thisTextArea.get("1.0", END)
        final_out = ""
        for stat in [s for s in self.__stats if self.__stats[s]['re']]:
            self.__stats[stat]['count'] = len(re.findall(self.__stats[stat]['re'], __text))
            final_out = final_out + f"{stat.capitalize()}: {self.__stats[stat]['count']}"
            if self.__stats[stat]['goal']:
                final_out = final_out + f" / {self.__stats[stat]['goal']}"
            final_out = final_out + "\t"

        final_out.strip()

        self.__thisStatusBar['text'] = final_out

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


if __name__ == "__main__":
    pyWrite = PyWrite(width=800, height=800)
    pyWrite.run()
