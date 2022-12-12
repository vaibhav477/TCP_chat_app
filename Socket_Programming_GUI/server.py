from tkinter import *
from tkinter import messagebox as mbox
import socket

win=Tk()
win.title('               SERVER          ')
win.configure(bg='#BC8F8F')
win.geometry('320x500')

typemsg=Listbox(win,height=25,width=45)
typemsg.place(x=10,y=15)

updsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
updsocket.bind(("localhost",5555))
mbox.showinfo('',"UPD server is up and listening")
pair = updsocket.recvfrom(1024)
res = pair[0]
add = pair[1]
typemsg.insert(END,'Client : '+res.decode())
mbox.showinfo('Address of client',add)

updsocket.sendto(str.encode("Connected to Server!"), add)
    
def send():
        pair = updsocket.recvfrom(1024)
        res = pair[0]
        add = pair[1]
        typemsg.insert(END,"Client: "+res.decode())
        message = matter_name.get()
        if message == "":
            mbox.showerror('ERROR','Enter message')
        typemsg.insert(END,"Server: "+message)
        updsocket.sendto(str.encode(message), add)
        matter_entrybox.delete(0,END)

matter_name=StringVar()
matter_entrybox=Entry(win,width=35,textvariable=matter_name,border=4,font=('arial','10'))
matter_entrybox.place(x=10,y=440)

send_button=Button(win,text='Send',command=send,borderwidth=0,bg="#20B2AA",fg="gold" ,font=("times new roman",13) )
send_button.place(x=275,y=440)

win.mainloop()





