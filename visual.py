import tkinter as tk
from tkinter.constants import *
import prettytable as pt
class Table_repr:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Визуализация свойств чисел")
        self.root.geometry('1000x600')
        self.root.minsize(1000, 600)
        txt_frm = tk.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        txt_frm.grid_propagate(False)
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)
        self.txt = tk.Text(txt_frm, borderwidth=3, relief=SUNKEN)
        self.txt.config(font=("Courier New", 12), undo=True, wrap=NONE)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scrollb = tk.Scrollbar(txt_frm, orient=HORIZONTAL, command=self.txt.xview)
        scrollb.grid(row=1, column=0, sticky='nsew')
        self.txt['xscrollcommand'] = scrollb.set

def wrap(iterable):
    string = ""
    pattern = ';\n'
    for elem in iterable:
        string += str(elem)
        string += pattern
    return string

def visual_representation(ND, rct, unus, isEx, suf, isS, factorization, num, smooth, repr_sqrt2, repr_pow2, roman, bit):
    repr_ = pt.PrettyTable(title="Визуализация свойств чисел".upper())
    titles = ['Делители числа', 'Число простое?', 'Число прямоугольное?', 'Число необычное?',
              'Кол-во простых делителей < 10',
              'Число избыточное?', 'Число недостаточное?', 'Квадрат числа:', "Корень из числа:",
              "Римское представление:",
              "Двоичное представление:"]
    values = [ [wrap(factorization())] , [f'{str(isS).lower()}'], [f'{str(rct).lower()}'], [f'{str(unus).lower()}'],
              [f'{smooth()[59:]}'], [f'{str(isEx).lower()}'], [f'{str(suf).lower()}'], [f'{repr_pow2()[28:]}'],
              [f'{repr_sqrt2()[30:]}'],
              [f'{roman(num)}'], [f'{str(bin(num))[2:]}']]
    for t, v in zip(titles, values):
        repr_.add_column(t, v)

    t = Table_repr()
    t.txt.insert(1.0, repr_.get_string())
    t.root.mainloop()

if __name__ == '__main__':
    pass