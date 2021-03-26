from tkinter import *
from tkinter import Label
from typing import List

root = Tk()
root.title("Physics Calculator")

equation = Label(root, text="Q / t = (k * A * deltaT) / L ")
equation.grid(row=0, column=0, columnspan=6)
q1 = Label(root, text="What are you solving for?")
q1.grid(row=1, column=0, columnspan=6)

QLabel = Label(root, text="Q =")
tLabel = Label(root, text="t =")
kLabel = Label(root, text="k =")
T1Label = Label(root, text="T1 =")
T2Label = Label(root, text="T2 =")
ALabel = Label(root, text="A =")
LLabel = Label(root, text="L =")

QEntry = Entry(root)
tEntry = Entry(root)
kEntry = Entry(root)
T1Entry = Entry(root)
T2Entry = Entry(root)
AEntry = Entry(root)
LEntry = Entry(root)

labelList = [QLabel, tLabel, kLabel, T1Label, T2Label, ALabel, LLabel]
entryList = [QEntry, tEntry, kEntry, T1Entry, T2Entry, AEntry, LEntry]

poppedLabel = []
poppedEntry = []


def get_value(x):
    return float(x.get())


def solve_for_q():
    def calculate():
        t = get_value(tEntry)
        k = get_value(kEntry)
        T1 = get_value(T1Entry)
        T2 = get_value(T2Entry)
        delta_T = abs(T2 - T1)
        A = get_value(AEntry)
        L = get_value(LEntry)
        Q = (t * k * A * delta_T) / L
        answer = Label(root, text="Q = " + str(Q) + " J")
        answer.grid(row=10, column=0, columnspan=6)
    if len(labelList) == 7:
        poppedLabel.append(labelList.pop(0))
    else:
        pass
    if len(entryList) == 7:
        poppedEntry.append(entryList.pop(0))
    else:
        pass
    for j in range(len(labelList)):
        labelList[j].grid(row=j + 3, column=0)
        entryList[j].grid(row=j + 3, column=1, columnspan=5)
    submitButton = Button(root, text="Calculate", command=calculate)
    submitButton.grid(row=9, column=0, columnspan=6)


def solve_for_t():
    def calculate():
        Q = get_value(QEntry)
        k = get_value(kEntry)
        T1 = get_value(T1Entry)
        T2 = get_value(T2Entry)
        delta_T = abs(T2 - T1)
        A = get_value(AEntry)
        L = get_value(LEntry)
        t = (Q * L) / (k * A * delta_T)
        answer = Label(root, text="t = " + str(t) + " sec")
        answer.grid(row=10, column=0, columnspan=6)
    if range(len(poppedLabel)) == 1:
        labelList.append(poppedLabel.pop())
    else:
        pass
    if range(len(poppedEntry)) == 1:
        entryList.append(poppedEntry.pop())
    else:
        pass
    if len(labelList) == 7:
        poppedLabel.append(labelList.pop(1))
    else:
        pass
    if len(entryList) == 7:
        poppedEntry.append(entryList.pop(1))
    else:
        pass
    for j in range(len(labelList)):
        labelList[j].grid(row=j + 3, column=0)
        entryList[j].grid(row=j + 3, column=1, columnspan=5)
    submitButton = Button(root, text="Calculate", command=calculate)
    submitButton.grid(row=9, column=0, columnspan=6)


def solve_for_k():
    def calculate():
        t = get_value(tEntry)
        Q = get_value(QEntry)
        T1 = get_value(T1Entry)
        T2 = get_value(T2Entry)
        delta_T = abs(T2 - T1)
        A = get_value(AEntry)
        L = get_value(LEntry)
        k = (Q * L) / (t * A * delta_T)
        answer = Label(root, text="k = " + str(k) + " J/smK")
        answer.grid(row=10, column=0, columnspan=6)
    if range(len(poppedLabel)) == 1:
        labelList.append(poppedLabel.pop())
    else:
        pass
    if range(len(poppedEntry)) == 1:
        entryList.append(poppedEntry.pop())
    else:
        pass
    if len(labelList) == 7:
        poppedLabel.append(labelList.pop(2))
    else:
        pass
    if len(entryList) == 7:
        poppedEntry.append(entryList.pop(2))
    else:
        pass
    for j in range(len(labelList)):
        labelList[j].grid(row=j + 3, column=0)
        entryList[j].grid(row=j + 3, column=1, columnspan=5)
    submitButton = Button(root, text="Calculate", command=calculate)
    submitButton.grid(row=9, column=0, columnspan=6)


heatButton = Button(root, text="Q", command=solve_for_q)
timeButton = Button(root, text="t", command=solve_for_t)
thermalButton = Button(root, text="k", command=solve_for_k)
areaButton = Button(root, text="A")
tempChangeButton = Button(root, text="deltaT")
lengthButton = Button(root, text="L")

buttonList = [heatButton, timeButton, thermalButton, areaButton, tempChangeButton, lengthButton]

for i in range(len(buttonList)):
    buttonList[i].grid(row=2, column=i)

root.mainloop()
