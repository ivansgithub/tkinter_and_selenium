from tkinter import Button, Label, Tk, StringVar, Entry, ttk
import time
from tkinter import HORIZONTAL
from seleniumappre import entrando, reporte





def send_data():
  entrando(username.get(),password.get())
  
  
  reporte()
      
  label_1= Label(mywindow,text='Reporte Listo')
  label_1.pack()
  



mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("CRM Report")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "CRM Report", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


username_label = Label(text = "Username", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Password", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)


username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()


username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")

 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)



mywindow.geometry("620x400")



bar= ttk.Progressbar(mywindow, orient=HORIZONTAL, length=300)
bar.pack(pady=170)


submit_btn = Button(mywindow,text = "Submit", width = "30", height = "2", command =send_data , bg = "#00CD63")



submit_btn.place(x = 22, y = 320)






mywindow.mainloop()