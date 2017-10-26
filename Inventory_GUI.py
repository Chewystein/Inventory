from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *

Audit_File_Path = "C:\\Users\\taubeg\\Documents\\Python Scripts\\Inventory Audits\\missing\\"

Program_path = "C:\\Users\\taubeg\\Documents\\Python Scripts\\Inventory Audits\\python_output\\"


class Main_Window(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Bad vs Missing")
        self.pack(fill=BOTH, expand=True)


        def openfile():
            return filedialog.askopenfilename()

        button = ttk.Button(text="Open", command=openfile)
        button.pack(side=TOP)


def main():
    root = Tk()
    root.geometry("750x500+100+100")
    root.configure(background='black')
    app = Main_Window()
    root.mainloop()


if __name__ == '__main__':
    main()
