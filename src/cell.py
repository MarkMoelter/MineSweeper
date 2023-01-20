import tkinter as tk


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object: tk.Button = None

    def create_btn_object(self, container):
        btn = tk.Button(
            container,
            text='Text'
        )
        self.cell_btn_object = btn
