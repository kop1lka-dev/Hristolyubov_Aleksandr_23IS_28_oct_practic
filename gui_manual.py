import tkinter as tk
from tkinter import ttk

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

окно = tk.Tk()
окно.title("Алканы — органическая химия")
окно.geometry("680x420")

надпись = ttk.Label(окно, text="Каталог алканов")
надпись.pack(pady=10)

кнопка_очистки = ttk.Button(
    окно,
    text="Очистить таблицу",
    command=очистить_таблицу
)
кнопка_очистки.pack(pady=5)

таблица = ttk.Treeview(
    окно,
    columns=("name", "formula", "carbon_count"),
    show="headings",
    height=10
)
таблица.heading("name", text="Название")
таблица.heading("formula", text="Формула")
таблица.heading("carbon_count", text="Атомов углерода")

таблица.column("name", width=220, anchor="w")
таблица.column("formula", width=160, anchor="center")
таблица.column("carbon_count", width=180, anchor="center")

таблица.pack(padx=15, pady=10, fill="both", expand=True)

таблица.insert("", tk.END, values=("Метан", "CH4", 1))
таблица.insert("", tk.END, values=("Этан", "C2H6", 2))
таблица.insert("", tk.END, values=("Пропан", "C3H8", 3))

окно.mainloop()