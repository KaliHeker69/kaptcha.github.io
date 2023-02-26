from tkinter import *
import webbrowser
root = Tk()
root.title("KAPTCHA")
root.iconbitmap(r'C:/Users/gaura/Desktop/favicon.ico')
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

def callback(url):
   webbrowser.open_new_tab(url)


link = Label(root, text="Click Here for Further information",font=('Open Sans', 15), fg="blue",bg="white", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))

root.mainloop()
