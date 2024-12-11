import tkinter

window = tkinter.Tk()
window.title("Miles to Km Convertor")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def answer():
    ans = entry.get()
    km = int(ans)*1.609
    text3.config(text=km)

text1 = tkinter.Label(text="is equal to", font=("arial", 15, "bold"))
text1.grid(column=0, row=1)
text1.config(pady=10, padx=10)

text2 = tkinter.Label(text="Miles", font=("arial", 15, "bold"))
text2.grid(column=3, row=0)
text2.config(pady=10, padx=10)

text3 = tkinter.Label(text=" ", font=("arial", 15, "bold"))
text3.grid(column=1, row=1)
text3.config(pady=10, padx=10)

text4 = tkinter.Label(text="KM", font=("arial", 15, "bold"))
text4.grid(column=3, row=1)
text4.config(pady=10, padx=10)

entry = tkinter.Entry()
entry.grid(column=1, row=0)
entry.configure(borderwidth=3, width=10, background="lightblue", justify='center', font=("arial", 15, "bold"))

butt = tkinter.Button(text="Convert", font=("arial", 15, "bold"), command=answer)
butt.grid(column=1, row=2)
butt.config(pady=10, padx=10)

window.mainloop()