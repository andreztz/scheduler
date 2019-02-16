import os
import subprocess

from tkinter import Button
from tkinter import Frame
from tkinter import Menu
from tkinter import Label
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Tk
from tkinter import TOP
from tkinter import Toplevel
from tkinter import X
from tkinter import YES
from tkinter import Scrollbar

from tkinter.ttk import Treeview

from PIL import Image, ImageTk

from gui.form import Form

from core.setup_data import read_data

APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

IMAGE_DIR = os.path.join(APPLICATION_DIR, "img")


class NewWindow(Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        Form(master)

    def close_windows(self):
        self.master.destroy()


class ConfigView(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Config Page").grid()
        self.grid(row=1, columnspan=4, sticky="nsew")


class ListView(Treeview):
    def __init__(self, master):

        super().__init__(master, columns=("Name", "Time", "Message", "Path"))
        self.data = read_data()
        self.items = 0
        self.vsb = Scrollbar(orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.vsb.set)
        self.hsb = Scrollbar(orient="horizontal", command=self.xview)
        self.configure(xscrollcommand=self.hsb.set)

        self.heading("#0", text="Name")
        self.heading("#1", text="Time")
        self.heading("#2", text="Messages")
        self.heading("#3", text="Path")
        self.column("#0", stretch=YES)
        self.column("#1", stretch=YES)
        self.column("#2", stretch=YES)
        self.column("#3", stretch=YES)
        self.grid(row=1, columnspan=4, sticky="nsew")
        self.vsb.grid(row=1, column=1, sticky="nsew", in_=self.master)
        self.hsb.grid(row=2, column=0, sticky="nsew", in_=self.master)
        self.after(1000, self.update)

    def update(self):
        items = len(read_data())
        if self.items != items:
            self.data = read_data()
            self.delete(*self.get_children())
            for i in self.data:
                self.insert(
                    "",
                    "end",
                    text=i["name"],
                    values=(i["time"], i["messages"], i["path"]),
                )
            self.items = len(read_data())

        self.after(1000, self.update)


class MenuBar(Menu):
    def __init__(self, master):
        super().__init__(master)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(menu=fileMenu, underline=0, label="Menu", state="normal")
        fileMenu.add_command(
            label="Add task",
            command=lambda m=master: (Main.new_window(master)),
            state="normal",
            underline=1,
        )
        fileMenu.add_separator()
        fileMenu.add_command(label="sair", command=self.sair, state="normal")

        cad_menu = Menu(self, tearoff=False)
        self.add_cascade(menu=cad_menu, underline=0, label="Opções", state="normal")
        cad_menu.add_command(
            label="Lista",
            command=lambda m=master: (Main(master).control(ListView)),
            state="normal",
            underline=1,
        )
        cad_menu.add_command(
            label="Configurações",
            command=lambda m=master: (Main(master).control(ConfigView)),
            state="normal",
        )

        alt_menu = Menu(self, tearoff=False)
        self.add_cascade(menu=alt_menu, underline=0, label="Ajuda", state="normal")
        alt_menu.add_command(
            label="Documentaçõa", command=None, state="normal", underline=1
        )
        alt_menu.add_command(label="Ver Licença", command=None, state="normal")
        alt_menu.add_command(label="Sobre", command=None, state="normal")

    def sair(self):
        self.vazar = messagebox.askyesno(title="Sair", message="Deseja realmente sair?")
        if self.vazar:
            self.master.destroy()
        else:
            print("vazar")


class Tollbar(Frame):
    def __init__(self, master):
        super().__init__(master, bd=1, relief="raised")

        self.img_add = Image.open(IMAGE_DIR + "/add.png")
        addimg = ImageTk.PhotoImage(self.img_add)
        addButton = Button(
            self,
            image=addimg,
            relief="flat",
            command=lambda m=master: (Main.new_window(master)),
        )
        addButton.image = addimg
        addButton.grid(row=0, column=0)

        self.grid(row=0, column=0, sticky="nsew", columnspan=1, in_=self.master)


class Main(Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)

        self.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def control(self, View):
        View(self)

    def new_window(self):
        NewWindow(Toplevel(self))


class Application:
    def __init__(self, master, geometry="600x320", **kwargs):
        fonte1 = ("Verdana", "14", "bold")

        self.master = master
        self.master.title("Application")
        # self.master.geometry("600x320")
        self.master.geometry(geometry)
        # self.master.resizable(width=False,height=False)
        self.menubar = MenuBar(self.master)
        self.master.config(menu=self.menubar)

        Tollbar(master)
        Main(self.master).control(ListView)
        # Main(self.master).control(ConfigView)

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)


def get_screen_size():
    proc1 = subprocess.Popen(["xrandr"], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(["grep", "*"], stdin=proc1.stdout, stdout=subprocess.PIPE)
    stdout_data, stderr_data = proc2.communicate()
    return stdout_data.decode().split()


def main():
    root = Tk()
    # root.withdraw()
    # root.update_idletasks()
    x = (1440 - 720) / 2
    y = (900 - 450) / 2
    root.geometry("+%d+%d" % (x, y))
    # root.deiconify()
    Application(root, "720x450")
    root.mainloop()


if __name__ == "__main__":
    main()
