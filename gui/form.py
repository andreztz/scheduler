from datetime import datetime

from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import Text
from tkinter import Tk
from tkinter import filedialog

from tkinter.ttk import Combobox
from tkinter.ttk import LabelFrame

from core.setup_data import add_new_task

largura = 30


class Form:
    def __init__(self, master):
        self.master = master

        self.top_frame = Frame(self.master)

        Label(self.top_frame, text="Task Name: ").grid(row=0, column=0, sticky="ne")

        self.task_name = Entry(self.top_frame, width=largura)
        self.task_name.grid(row=0, column=1, sticky="nsew", pady=20, padx=10)

        Label(self.top_frame, text="Description: ").grid(row=1, column=0, sticky="ne")

        self.description = Text(self.top_frame, height=10, width=largura)
        self.description.grid(row=1, column=1, sticky="nsew", pady=20, padx=10)

        self.top_frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=10)

        # Mid Frame

        self.mid_frame = Frame(self.master)

        # Select Path

        self.selected_path_label = Label(self.mid_frame, text="Script path: ").grid(
            row=1, column=1, sticky="ne"
        )

        self.in_file_path = StringVar()
        self.selected_path_entry = Entry(
            self.mid_frame, textvariable=self.in_file_path, width=largura
        ).grid(row=1, column=2, sticky="nsew", pady=20, padx=10)

        self.selected_path_button = Button(
            self.mid_frame, text="Browse", command=self.in_browse_click
        ).grid(row=1, column=3, sticky="nsew", pady=20)

        self.mid_frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=10)
        # Bottom Frame

        self.bottom_frame = Frame(self.master)

        Label(self.bottom_frame, text="Time: ", anchor="w").grid(
            row=0, column=0, sticky="ne"
        )
        # Select Time
        Label(self.bottom_frame, text="Hour: ").grid(row=0, column=1)

        hour_options = [f"{x:02d}" for x in range(1, 25)]
        self.hour_combo_box = Combobox(self.bottom_frame, width=3, values=hour_options)
        self.hour_combo_box.set(hour_options[datetime.now().hour - 1])
        self.hour_combo_box.grid(row=0, column=2, sticky="w")

        Label(self.bottom_frame, text="Minute: ").grid(row=0, column=3, sticky="w")

        minute_options = [f"{x:02d}" for x in range(1, 61)]
        self.minute_combo_box = Combobox(
            self.bottom_frame, width=3, values=minute_options
        )
        self.minute_combo_box.set(minute_options[datetime.now().minute - 1])
        self.minute_combo_box.grid(row=0, column=4, sticky="w")

        Label(self.bottom_frame, text="Second: ").grid(row=0, column=5)

        second_options = [f"{x:02d}" for x in range(1, 61)]
        self.second_combo_box = Combobox(
            self.bottom_frame, width=3, values=second_options
        )
        self.second_combo_box.set(second_options[datetime.now().minute - 1])
        self.second_combo_box.grid(row=0, column=6)

        self.bottom_frame.grid(row=2, column=0, pady=20, padx=10)

        self.button = Button(self.master, text="New", command=self.new_task)
        self.button.grid(row=4)

    def in_browse_click(self):

        file_path = filedialog.askopenfilename(title="select a script")
        self.in_file_path.set(file_path)

    def new_task(self):
        hour = self.hour_combo_box.get()
        min = self.minute_combo_box.get()
        sec = self.second_combo_box.get()

        time = f"{hour}:{min}:{sec}"
        name = self.task_name.get()
        messages = self.description.get("1.0", "end")
        path = self.in_file_path.get() if self.in_file_path else ""
        add_new_task(name=name, time=time, messages=messages, path=path)


class Application:
    def __init__(self, master):
        Form(master)


def main():
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
