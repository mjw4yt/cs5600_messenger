from tkinter import *

root = Tk()
root.title('EasyChat Login')

input_username = Entry(root, width=50)
input_password = Entry(root, width=50)
user_label = Label(root, text="Enter your username:")
password_label = Label(root, text="Enter your password:")
user_label.grid(row=0,column=0)
password_label.grid(row=1,column=0)
input_username.grid(row=0, column=1)
input_password.grid(row=1, column=1)
def check_inputs():
    if input_username.get() == "username":
        if input_password.get() == "password":
            open()
            input_username.delete(0, 'end')
            input_password.delete(0, 'end')
        else:
            my_label = Label(root, text="Your Password is Incorrect")
            my_label.grid(row=4, column=0, columnspan=2)
            input_username.delete(0, 'end')
            input_password.delete(0, 'end')
            my_label.forget()
    else:
        my_label = Label(root, text="Your Username does not exist")
        my_label.grid(row=4,column=0,columnspan=2)
        input_username.delete(0, 'end')
        input_password.delete(0, 'end')
        my_label.forget()

def open():
	top = Toplevel()
	top.title('Global Chat')
	my_label = Label(top, text="Welcome, "+input_username.get()).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()

submit_button = Button(root, text="Login in", command=check_inputs)
submit_button.grid(row=2,column=0,columnspan=2)


mainloop()