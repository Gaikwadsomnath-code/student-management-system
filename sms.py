from itertools import count
from tkinter import *
import time
import ttkthemes#for apply theme on button
from tkinter import ttk,messagebox,filedialog # filedialog is used for export page dialog
import pymysql
from PIL.ImageChops import screen
import pandas

#functionality part
# for exit button
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass




# for export data
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]# in newlist all data present into this list
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

# data convert into tabular form using pd
    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)#data will be save in csv file
    messagebox.showinfo('Success','Data will be saved succesfully')



# uses multiple times single block of code that's why we create function when need a code just call function
def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()  # it not allow to click somewhere else until the  toplevel window open
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10)

    student_button = ttk.Button(screen, text=button_text,command=command)
    student_button.grid(row=7, columnspan=2, pady=15)

    if title=='Update Student':
        # we call one function for update any record for show info in form (show datailes in window)
        indexing = studentTable.focus()

        print(indexing)
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])



#  for update  student
# for updating data in treeview
def update_data():
    query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                        genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id{idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()




# for show student
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


#for  delete student
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())#it use for not showing previes data if deleting id's
    for data in fetched_data:
        studentTable.insert('',END,values=data)


#for search student

def search_data():#
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)



# for adding student add window for insert detailes

def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)#if anyfeild are empty it will show the messege & all feilds are required

    else:

        try:# try & except block use for any duplicate id insert show messege error
            query='INSERT INTO student values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                         genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            # form ask yes-no if choose yes the if condition will be true
            result=messagebox.askyesno('Confirm','Data added successfully.Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return


        query='select *from student'# for fetche data
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        #it use for previes data delete from treeview if inserted new
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:# it convert tuple into list
            datalist=list(data) # ones you get data form of list now you can insert this data  inside our treeview and it object name of treeview
            studentTable.insert('',END,values=datalist)



#use for connect to database
def connect_database():
    def connect():
        global mycursor,con
        try:
           con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
           mycursor=con.cursor()
        except:
              messagebox.showerror('Error','Invalid Details',parent=connectWindow)
              return
        try:
            query='create database studentmanagementsystems'
            mycursor.execute(query)
            query='use studentmanagementsystems'
            mycursor.execute(query)
            query='create table student(id int not null primary key, name varchar(30),mobile varchar(10),email varchar(30),'\
                    'address varchar(100),gender varchar(30),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystems'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)
        connectWindow.destroy()#db connect window will be destroy and all  button will be normal
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)



    connectWindow=Toplevel()
    #connectWindow.grab_set()#if use this dont minimize window of connecting db window
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

#creating host name ,entry, password
    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
#  host entry field
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

#create username
    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
#user entry field
    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

#create password
    passwordLabel=Label(connectWindow,text='Password ',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
#password entry field
    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

#create button
    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():#slider create and one by one latter print
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]#s
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(100,slider)#after 100 ml sec change

 # difine function for dtae and time
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    # config method used to update something and f string used to concatenate string to the variable
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)# update every second

#GUI Part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')



root.geometry('1174x680+0+0')#asign size of window
root.resizable(0,0)
root.title('Student Management System')# name of page

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()#call function
s='Student Management System'#s[count]=S when count is 0
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

#connecting db
connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)
leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')#just place it
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,command=lambda :toplevel_data('Add Studnet','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,command=lambda :toplevel_data('Search Student','Search Student',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,command=lambda :toplevel_data('Update Student','Update ',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton=ttk.Button(leftFrame,text='Exit Student',width=25,command=iexit)
exitstudentButton.grid(row=7,column=0,pady=20)

# create a right frame
rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

#create scrollbar
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)


#it under the ttk class and this is treeview
studentTable=ttk.Treeview(rightFrame,column=('Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)#it can use for working scrollbar
#used for view data
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

# scrollbar show
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
# pack method use for add something new in this
studentTable.pack(fill=BOTH,expand=1)

#heading of column in stored in db
studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')
#provide width of titles
studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

# give bg colour to entry's in db
style=ttk.Style()

# treeview styleing
style.configure('Treeview', rowheight=40, font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='red')




studentTable.config(show='headings')

root.mainloop()

