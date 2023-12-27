import tkinter


def convert(miles):
    try:
        return miles * 1.609344
    except:
        return ''


def onClick():
    # print(type(input.get()))
    out.config(text=convert(float(input.get())))
    return


window = tkinter.Tk()
window.title(string='Miles to kilometer convertor')
window.minsize(width=300, height=300)
window.config(padx=10, pady=10)

input = tkinter.Entry()
input.grid(column=1, row=0)
miles = tkinter.Label(text=' Miles')
miles.grid(column=2, row=0)
is_equal_to = tkinter.Label(text='is equal to')
is_equal_to.grid(column=0, row=1)
out = tkinter.Label(text=0)
out.grid(column=1, row=1)
km = tkinter.Label(text=' Kms')
km.grid(column=2, row=1)
calc = tkinter.Button(text='Calculate', command=onClick)
calc.grid(column=1, row=2)
window.mainloop()
