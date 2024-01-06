import tkinter as tk
from venv import create

#pystray and PIL must be imported together, pystray only uses images and .icos from PIL
import pystray 
from PIL import Image

# extending the class tk.Tk, which means we initialize a new one
# (which is what we were going to do anyway to get a window)
# but also we can control the alive-ness of this instance more readily
# and also we have to refer to defs in this class as self.[def]
class Quest(tk.Tk):
    def __init__(self):
        # basically this completes the above comment
        # it makes it so this class inherits from tk.Tk
        # and is SUPPOSED to initalize that but apparently it doesnt wanna
        super().__init__()

        # for .geometry: it's widthxlength and then a + or - determines whether the value after it pushes the window
        # away from the left or right of the screen, or the top or bottom of the screen
        # here, it's -25+25 for 25 pixels from the right of the screen and 25 pixels from the top
        #win.geometry(str(width)+"x"+str(height)+"-25+25")

        self.geometry("500x500-25+25")

        # this is so everything except things we want to show are invisible,
        # so from here on we assume "green" to just be "alpha" or "transparent" like a green screen
        self.attributes("-transparentcolor", "green")
        self.configure(bg="green")

        self.attributes("-topmost", True)
        self.resizable(False, False)

        # hides the close button and top drag bar thing. also hides it from the taskbar
        # which is bad when it's an exe with no console which means no way to close it
        # we fix this by letting you exit the program from the system tray
        self.overrideredirect(True)

# the only thing that is running at the start when you open the program
def createPystray():
    # menu for quitting that shit
    # if you put a () after the self.def, it just runs the def for some reason
    # so i guess you have to not put those when you just want to reference a def
    menu = (
        pystray.MenuItem("Embark on Journey", createNewQuest),
        pystray.MenuItem("Finish thine Quest", quit_that_shit), 
    )

    image = Image.open("test-dogy.ico")

    # we have to tell python a variable is global in the same scope we define it
    # any other configuration than this exact thing below doesnt work
    global icon
    icon = pystray.Icon("name", image, "yeah", menu)

    # believe it or not you need icon.run or it WONT FUCKING RUN
    # (i learned this from experience)

    icon.run()

def quit_that_shit(self):
    icon.stop()
    __win.destroy()


# runs when you pick embark from the system tray
def createNewQuest():
    #init tk.Tk by initializing the extended class Quest
    global __win
    __win = Quest()

    #new window
    global inputwindow
    inputwindow = tk.Toplevel()
    inputwindow.title("Enter quest info")
    inputwindow.geometry("500x300")

    ask1 = tk.Label(inputwindow, text="Name of Quest")
    ask1.pack()

    global entry1
    entry1 = tk.Entry(inputwindow)
    entry1.pack()

    ask2 = tk.Label(inputwindow, text="Completion Requirements")
    ask2.pack()

    global entry2
    entry2 = tk.Entry(inputwindow)
    entry2.pack()

    embarkbutton = tk.Button(inputwindow, text="Embark", command=displayQuest)
    embarkbutton.pack()

    # this should be the last thing that runs always
    # because this is basically the "we're done here send it" bit
    __win.mainloop()

# this is for the embark button, it has to take a def
# here we just add labels with the name and completion requirements
# to the main quest window
def displayQuest():
    display1 = tk.Label(__win, text=entry1.get())
    display1.pack()
    display2 = tk.Label(__win, text=entry2.get())
    display2.pack()

    # we also want to delete the input window
    inputwindow.destroy()


if __name__ == "__main__":
    createPystray()




