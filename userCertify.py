# #User certificate
import tkinter as tk #for graphics
from PIL import Image, ImageDraw, ImageFont,ImageTk

from tkinter import messagebox #a part of tkinter that lets you show pop‑up messages.
def userCertify():
    label1.config(text = "")
    # for name in userName:
    # bold = tk.Button(rootWn,text=userName ,color = "Blue" )
def buttonAction():
    image = Image.open("googlepay.png")
    draw = ImageDraw.Draw(image)
    imaging = image.resize((100,100))
    images = ImageTk.PhotoImage(imaging)
    popupwn = tk.Toplevel(rootWn)#new window
    popupwn.title("certificate")
    image_label = tk.Label(popupwn,image=images)
    textShowing =tk.Label(popupwn,text= f"This is to certify that {username}\n  a student of Government Engineering College, Munger, has successfully \ncompleted a comprehensive 2-week offline\n Internship in Artificial Intelligence with INTELLIO INTERN (01/09/2026 - 15/09/2026).\n\t Grade Achieved: A+(97%).\n\t We wish her every success in all her future professional endeavors.",font=("Arial", 14, "bold"),pady=10,fg="red")
    textShowing.pack()
    image_label.pack(padx=20, pady=20)
    image_label.image = images
    

#     #messagebox.showinfo("This is your Certificate")open that exact separate small window to deliver alerts.
#     #messagebox.showerror("may error found")alternative displaying
#     #messagebox.showwarning("might be warninig")
rootWn = tk.Tk() #making a root window
rootWn.title("-----User Certificate-----")
#rootWn.geometry("100 , 700") wn ka ek standard size set kiya
label1 = tk.Label(rootWn,text = "Enter Your Name Here" , font = ("Trebuchet MS", 28, "bold", "italic"))
label1.place(x=600,y = 50)
#label1.pack()ithout this the text won't be appear
# #for taking user input on gui we use entry
entryName = tk.Entry(rootWn ,width = 10 ,font = ("Trebuchet MS", 12, "bold", "italic"),fg="red")
username = entryName.get()
font = ImageFont.truetype("arial.ttf", 40)
entryName.pack()#to show it (taking user name)
label1.config(text= "==Give Your Name==",fg = "blue",font = ("Trebuchet MS",28,"bold","italic"))
entryName.place(x=700,y=200)
# #when we use config then the text will be updated(the above text)
# #making a button
buttons = tk.Button(rootWn,text = "show my certificate",command=buttonAction)#in the cmd if i give the () it firstly run btn popUP
buttons.place(x=700,y=500)
# buttons.pack()
# image_label.pack(x=50,y=30)

# imaging =tk.Image('images','create')
# images.place(x=800,y=500)


rootWn.mainloop()