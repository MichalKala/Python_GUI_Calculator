#Create basic window
from tkinter import *
gui = Tk()
gui.title("Michal's calculator")
gui.geometry('540x360')
#gui.configure(background = "gray")

#Add main display (textbox)
display = Entry(gui, width = 75, font = 'Calibri 26')
display.place(x=0, y=0)
display.configure(state='readonly')


#Add info label
myLabel = Label(gui, text = 'My name is Michal and \nI am trying to code a calculator!', font=("Arial", 10), justify=LEFT)
#Set position of the Label
myLabel.place(x=300, y=60)


#Add buttons and define what they do
btnheight = 2
btnwidth = 4

def button1_Handle():
    display.configure(state="normal")
    display.insert("end", "7")
    display.configure(state="readonly")

button1 = Button(gui, text = "7", background = 'white', height=btnheight, width=btnwidth, command=button1_Handle)
button1.place(x=0, y=60)

def button2_Handle():
    display.configure(state="normal")
    display.insert("end", "8")
    display.configure(state="readonly")

button2 = Button(gui, text = "8", background = 'white', height=btnheight, width=btnwidth, command=button2_Handle)
button2.place(x=60, y=60)

def button3_Handle():
    display.configure(state="normal")
    display.insert("end", "9")
    display.configure(state="readonly")

button3 = Button(gui, text = "9", background = 'white', height=btnheight, width=btnwidth, command=button3_Handle)
button3.place(x=120, y=60)

def button4_Handle():
    display.configure(state="normal")
    display.insert("end", "4")
    display.configure(state="readonly")

button4 = Button(gui, text = "4", background = 'white', height=btnheight, width=btnwidth, command=button4_Handle)
button4.place(x=0, y=120)

def button5_Handle():
    display.configure(state="normal")
    display.insert("end", "5")
    display.configure(state="readonly")

button5 = Button(gui, text = "5", background = 'white', height=btnheight, width=btnwidth, command=button5_Handle)
button5.place(x=60, y=120)

def button6_Handle():
    display.configure(state="normal")
    display.insert("end", "6")
    display.configure(state="readonly")

button6 = Button(gui, text = "6", background = 'white', height=btnheight, width=btnwidth, command=button6_Handle)
button6.place(x=120, y=120)

def button7_Handle():
    display.configure(state="normal")
    display.insert("end", "1")
    display.configure(state="readonly")

button7 = Button(gui, text = "1", background = 'white', height=btnheight, width=btnwidth, command=button7_Handle)
button7.place(x=0, y=180)

def button8_Handle():
    display.configure(state="normal")
    display.insert("end", "2")
    display.configure(state="readonly")

button8 = Button(gui, text = "2", background = 'white', height=btnheight, width=btnwidth, command=button8_Handle)
button8.place(x=60, y=180)

def button9_Handle():
    display.configure(state="normal")
    display.insert("end", "3")
    display.configure(state="readonly")

button9 = Button(gui, text = "3", background = 'white', height=btnheight, width=btnwidth, command=button9_Handle)
button9.place(x=120, y=180)

def button0_Handle():
    display.configure(state="normal")
    display.insert("end", "0")
    display.configure(state="readonly")

button0 = Button(gui, text = "0", background = 'white', height=btnheight, width=btnwidth, command=button0_Handle)
button0.place(x=0, y=240)

def buttondivide_Handle():
    global firstnmb
    global selectedoperation
    firstnmb = display.get()
    firstnmb = float(firstnmb)
    selectedoperation = "divide"
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

buttondivide = Button(gui, text = "/", background = 'white', height=btnheight, width=btnwidth, command=buttondivide_Handle)
buttondivide.place(x=180, y=60)

def buttontimes_Handle():
    global firstnmb
    global selectedoperation
    firstnmb = display.get()
    firstnmb = float(firstnmb)
    selectedoperation = "times"
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

buttontimes = Button(gui, text = "*", background = 'white', height=btnheight, width=btnwidth, command=buttontimes_Handle)
buttontimes.place(x=180, y=120)

def buttonminus_Handle():
    global firstnmb
    global selectedoperation
    firstnmb = display.get()
    firstnmb = float(firstnmb)
    selectedoperation = "minus"
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

buttonminus = Button(gui, text = "-", background = 'white', height=btnheight, width=btnwidth, command=buttonminus_Handle)
buttonminus.place(x=180, y=180)

def buttonplus_Handle():
    global firstnmb
    global selectedoperation
    firstnmb = display.get()
    firstnmb = float(firstnmb)
    selectedoperation = "plus"
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

buttonplus = Button(gui, text = "+", background = 'white', height=btnheight, width=btnwidth, command=buttonplus_Handle)
buttonplus.place(x=180, y=240)

def buttonresult_Handle():
    finalresult = 0
    finalresult = float(finalresult)
    secondnmb = display.get()
    secondnmb = float(secondnmb)
    if selectedoperation == "plus":
        finalresult = firstnmb + secondnmb
    elif selectedoperation == "minus":
        finalresult = firstnmb - secondnmb
    elif selectedoperation == "divide":
        finalresult = firstnmb / secondnmb
    elif selectedoperation == "times":
        finalresult = firstnmb * secondnmb
    display.configure(state="normal")
    display.delete(0, "end")
    display.insert("end", finalresult)
    display.configure(state="readonly")

buttonresult = Button(gui, text = "=", background = 'white', height=btnheight, width=btnwidth, command=buttonresult_Handle)
buttonresult.place(x=120, y=240)

def buttonclear_Handle():
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

buttonclear = Button(gui, text = "C", background = 'white', height=btnheight, width=btnwidth, command=buttonclear_Handle)
buttonclear.place(x=60, y=240)

#Display the window
gui.mainloop()
