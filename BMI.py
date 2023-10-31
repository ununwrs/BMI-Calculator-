# BMI.py
#chayanan wareesri!!!
from tkinter import *
from tkinter import ttk, messagebox
import math 

FONT1 = ('impact', 20)
FONT2 = ('Angsana New', 15)
GUI = Tk()
GUI.title('หาค่า BMI')
GUI.geometry('700x500')
GUI.iconbitmap('BMI.ico')

L = ttk.Label(GUI, text='กรอกตัวเลขลงช่องว่างเพื่อหาค่า BMI ', font=FONT2).pack(pady=10)
v_weight = StringVar()
v_height = StringVar()

L = ttk.Label(GUI, text='น้ำหนัก (KG)').pack()
E1 = ttk.Entry(GUI, textvariable=v_weight, font=FONT1)
E1.pack(pady=20)
E1.focus()
L = ttk.Label(GUI, text='ส่วนสูง (CM)').pack()
E2 = ttk.Entry(GUI, textvariable=v_height, font=FONT1)
E2.pack(pady=20)


def Calculate(event=None):
    try:
        weight = float(v_weight.get())
        height = float(v_height.get())
        h = height / 100
        bmi = (weight/(math.pow(h,2)))
        text = 'BMI = {:,.2f} '.format(bmi)
        print(text)
        v_result.set(text)
        v_weight.set('')
        v_height.set('')
    except:
        messagebox.showwarning('Error', 'โปรดกรอกตัวเลขให้ครบทั้งสองช่องนะครับ ')
        v_weight.set('')
        v_height.set('')
        E1.focus()


B1 = ttk.Button(GUI, text='คำนวณ', command=Calculate)
B1.pack(ipadx=20, ipady=10)

E1.bind('<Return>', Calculate)
v_result = StringVar()
v_result.set('---ผลลัพธ์---')
R1 = ttk.Label(GUI, textvariable=v_result, font=FONT2, foreground='blue')
R1.pack(pady=20)

GUI.mainloop()