import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import message_box

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.configure(bg = "teal")

login_username_entry = Entry(registration_window)
login_password_entry = Entry(registration_window)

def login(): 
    print("login function")
    global login_username_entry
    global login_password_entry
    username = login_username_entry.get()
    password = login_password_netry.get()
    encrypt_pass = hashlib.md5(password.encode())
    hex_pass = encrypt_pass.hexdigest()
    get_password = firbase.get('/', username)
    print(hex_pass)
    
    if(get_password != None) :
        if(get_password == hex_pass) :
            messagebox.showinfo('Successfully Logged In.')
            
        else :
            messagebox.showinfo('Please check your password.')
    else :
        messagebox.showinfo('User now registered', 'Get yourself registered first to login.')
    
    registration_window.destroy(1.0, END)
    login_window.configure(bg = "teal")
    log_heading_label = Label(login_window, bg = "teal", fg = "white")
    login_username_label = Label(login_window, bg = "teal", fg = "white")
    login_password_label = Label(login_window, bg = "teal", fg = "white")
    btn_login = Button(login_window, text = "Login", bg = "teal", fg = "white")
    
def register(): 
    print("register function")
    username = login_username_entry.get()
    password = login_password_entry.get()
    var1 = password.encode()
    var2 = hashlib.md5(var1)
    var3 = var2.hexdigest()
    print(var3)
    firebase.put("https://project-188-3d11a-default-rtdb.firebaseio.com", username, var3)
    
def login_window():
    login_window = Tk()
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', bg = "teal", fg = "white")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg = 'teal', fg = "white")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg = "teal", fg = "white")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10, bg = "teal", fg = "white")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT, bg = "teal", fg = "white")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()