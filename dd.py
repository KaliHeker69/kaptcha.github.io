from tkinter import *

root = Tk()
root.title("KAPTCHA")
root.iconbitmap(r'C:/Users/gaura/Desktop/favicon.ico')
##### Dark Mode#####


root.geometry("800x600")
root.config(bg="white")
button_mode=True
def customize():
    global button_mode
    if button_mode:
        button.config(image=off, bg="#282828" , activebackground="#282828")
        root.config(bg="#282828")
        button_mode=False
    else:    
        button.config(image=on, bg="white" , activebackground="white")
        root.config(bg="white")
        button_mode=True

on=PhotoImage(file="C:\\Users\\gaura\\Desktop\\py\\light.png")
off=PhotoImage(file="C:\\Users\\gaura\\Desktop\\py\\dark.png")
button=Button(root,image=on,bd=0,bg="white",activebackground="white",command=customize)
button.pack(padx=50,pady=50)


##########

label1 = Label(root,text="Tata Tiagon ev - 8.49L")
label2 = Label(root,text="hyundai grand i10 nios - 8.55L") 
label3 = Label(root,text="Mahindra XUV 400 - 18L") 
label4 = Label(root,text="MG hector - 21.73L")
label5 = Label(root,text="Tata punch EV - 12L")
label6 = Label(root,text="Maruti suzuki brezza - 14L")
label7 = Label(root,text="tata harrier EV - 25L")
label8 = Label(root,text="Jeep Compass - 31.29L")

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)
label5.grid(row=2,column=0)
label6.grid(row=2,column=1)
label7.grid(row=3,column=0)
label8.grid(row=3,column=1)

root.mainloop()