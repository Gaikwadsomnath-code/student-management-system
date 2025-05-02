from tkinter import *
from tkinter import messagebox # it used for show error message in box
from PIL import ImageTk  #  PIL means pillow and import ImageTK

def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields can not be empty')
    elif usernameEntry.get()=='somnath' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')

        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')


window = Tk()

window.geometry('1280x700+0+0')
window.title('Login System of Student Management System')
window.resizable(False, False)

# Load the background image
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

# Create a label with the background image
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)
#create login frame and their size
loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)
#insert logo image
logoImage=PhotoImage(file='logo.png')


#insert username logo image
logoLabel=Label(loginFrame,image=logoImage,bg='white')
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')#insert username icon

#merge both text and image and give font and size to username
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,
                    font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

#create entry field to corresponding to username and their font and size
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


# to create a password icon ,box ,name,
passwordImage=PhotoImage(file='password.png')#insert password icon

#merge both text and image and give font and size to password
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

#create entry field to corresponding to password and their font and size
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

#  login button  colour,size,font,baheviar of button
loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue'
                   ,activeforeground='white',cursor='hand2',command=login) #pass command for valid login
loginButton.grid(row=3,column=1,pady=10)





window.mainloop()



