import logging
import tkinter as tk

import settings
from cell import Cell
from utils import percent_height, percent_width


def main():
    root = tk.Tk()
    # Override window settings
    root.configure(bg='black')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Minesweeper')
    root.resizable(False, False)

    # create frames
    top_frame = tk.Frame(
        root,
        bg='black',
        width=settings.WIDTH,
        height=percent_height(25)
    )
    top_frame.place(x=0, y=0)

    left_frame = tk.Frame(
        root,
        bg='black',
        width=percent_width(25),
        height=percent_height(75)
    )
    left_frame.place(x=0, y=percent_height(25))

    center_frame = tk.Frame(
        root,
        bg='black',
        width=percent_width(75),
        height=percent_height(75)
    )
    center_frame.place(x=percent_width(25), y=percent_height(25))

    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell()
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(
                column=x, row=y
            )

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    logging.basicConfig(filename='main.log', level=logging.DEBUG)
    main()
