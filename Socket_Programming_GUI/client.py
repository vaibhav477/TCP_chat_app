from tkinter import *
from tkinter import messagebox as mbox
import socket

win=Tk()
win.title('               CLIENT         ')
win.configure(bg='#BC8F8F')
win.geometry('320x500')

typemsg=Listbox(win,height=25,width=45)
typemsg.place(x=10,y=15)
udpsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udpsocket.sendto(str.encode("Client is connected!"), ("localhost", 5555))

mbox.showinfo('info',"Client Connected")
req = udpsocket.recvfrom(1024)
typemsg.insert(0,"Server : "+req[0].decode())

def sent():
    message = matter_name.get()
    typemsg.insert(END,"Client : "+message)
    udpsocket.sendto(str.encode(message),("localhost",5555))  
    req = udpsocket.recvfrom(1024)
    typemsg.insert(END,"Server : "+req[0].decode())
    matter_entrybox.delete(0,END)
  
    

matter_name=StringVar()
matter_entrybox=Entry(win,width=35,textvariable=matter_name,border=4,font=('arial','10'))
matter_entrybox.place(x=10,y=440)

send_button=Button(win,text='Send',command=sent,borderwidth=0,bg="#20B2AA",fg="gold" ,font=("times new roman",13) )
send_button.place(x=275,y=440)

win.mainloop()




