from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decrytion")
        screen2.geometry("400x200")
        screen2.configure(bg="#7cfc00")

        message = text1.get(1.0,END)
        decode_message = message.encode('ascii')
        base64_byte = base64.b64decode(decode_message)
        decrypt = base64_byte.decode('ascii')

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#7cfc00").place(x=10,y=0)
        text2 = Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password == '':
        messagebox.showerror("encryption",'input Password')

    elif password != "1234":
        messagebox.showerror("encryption",'invalid Password')

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encrytion")
        screen1.geometry("400x200")
        screen1.configure(bg="#ff4040")

        message = text1.get(1.0,END)
        encode_message = message.encode('ascii')
        base64_byte = base64.b64encode(encode_message)
        encrypt = base64_byte.decode('ascii')

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password == '':
        messagebox.showerror("encryption",'input Password')

    elif password != "1234":
        messagebox.showerror("encryption",'invalid Password')





def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x600")
    screen.title('Encrption-App')

    #icon
    image = screen.wm_iconbitmap('encryption.ico')

    def reset():
        code.set('')
        text1.delete(1.0,END)

    Label(text="Enter the text For Encryption And Decryption ",fg="black",font=("calbri,14")).place(x=10,y=10)
    text1 = Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret Key For Encryption And Decryption",fg="black",font=("calibri" ,13)).place(x=10,y=170)
    code = StringVar()
    Entry(textvariable=code,width=19,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ff2400",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#7cfc00",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text='RESET',height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)






    screen.mainloop()

main_screen()
