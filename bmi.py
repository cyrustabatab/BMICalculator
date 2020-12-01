import tkinter
from tkinter import messagebox




def calculate():
    weight,height = weight_variable.get(),height_variable.get()
    if not weight or not height:
        messagebox.showerror(title="Error",message="Please enter values for both weight and height!")
    try:
        weight,height = float(weight),float(height)
    except ValueError:
        messagebox.showerror(title="Error",message="Please enter NUMBERS")
    else:
        bmi = (weight/  height**2) * 703
        bmi = round(bmi,2)
        bmi_label['text'] = bmi
        bmi_label.grid()


def reset(*args):
    if bmi_label['text'] != '':
        bmi_label['text'] = ''





title_font = ("Arial",40,"bold")
normal_font = ("Arial",40,"normal")

window = tkinter.Tk()
window.title("BMI Calculator")
window.configure(padx=50,pady=50)



title_label = tkinter.Label(text="BMI CALCULATOR",font=title_font)
title_label.grid(row=0,column=0,columnspan=2)


weight_label = tkinter.Label(text="Weight(lb):",font=normal_font)
weight_label.grid(row=1,column=0,pady=20)

weight_variable = tkinter.StringVar()
weight_entry = tkinter.Entry(font=normal_font,textvariable=weight_variable)
weight_entry.focus_set()
weight_entry.grid(row=1,column=1,padx=20,pady=20)
weight_variable.trace('w',reset)


height_variable = tkinter.StringVar()
height_label = tkinter.Label(text="Height(inches):",font=normal_font)
height_label.grid(row=2,column=0,pady=20)

height_entry = tkinter.Entry(font=normal_font,textvariable=height_variable)
height_entry.grid(row=2,column=1,padx=20,pady=20)

height_variable.trace('w',reset)


calculate_button = tkinter.Button(text="CALCULATE",font=title_font,command=calculate)
calculate_button.grid(row=3,column=0,columnspan=2,pady=20)


bmi_label = tkinter.Label(text='',font=title_font)
bmi_label.grid(row=4,column=0,columnspan=2)
bmi_label.grid_remove()





window.mainloop()
