from Tkinter import*
import tkMessageBox
import sqlite3
root=Tk()
con=sqlite3.Connection('q2')
cur=con.cursor()
cur.execute("create table if not exists record(cid integer primary key AUTOINCREMENT,cfname varchar(50),cmname varchar(50),clname varchar(50),cconame varchar(50),caddr varchar(50),ccity varchar(40),cpin number(6),cweb varchar(50),cdob varchar(10),cptype varchar(10),cphone varchar(10),cetype varchar(10),cemail varchar(50))")
img=PhotoImage(file="Man.gif")
root.geometry("850x430")
img = img.zoom(13)
img = img.subsample(30) 
Label(root,image=img).grid(row=0,column=1)
Label(root,text="    ABOUT THE DEVELOPER",font='Arial 15',fg='red').grid(sticky="NW",row=0,column=10)
Label(root,text="  189301008",font='Arial 15',fg='blue').grid(row=0,column=10)
Label(root,text="    Manav Bhagwani",font='Arial 15',fg='black').grid(row=0,column=5)
Label(root,text="CSE-C         ",font='Arial 15',fg='orange').grid(row=0,column=15)
Label(root,text="PhoneBook project of Database",font='Arial 15',fg='black').grid(row=17,column=10)
Label(root,text="Make mouse movement over this screen to close",font="Arial 13",fg='brown').grid(row=50,column=10)

def close(e=1):
    root.destroy()
    root1=Tk()
    root1.title("Phone Book")
    root1.geometry("555x400")
    Label(root1,text="PHONEBOOK",font='Arial 20',fg='orange').grid(sticky="NW",row=0,column=1)
    Label(root1,text=" First Name ").grid(row=3,column=0)
    f=Entry(root1)
    f.grid(row=3,column=2)
    Label(root1,text=" Middle Name ").grid(row=5,column=0)
    f1=Entry(root1)
    f1.grid(row=5,column=2)
    Label(root1,text=" Last Name ").grid(row=7,column=0)
    f2=Entry(root1)
    f2.grid(row=7,column=2)
    Label(root1,text=" Company Name ").grid(row=9,column=0)
    f3=Entry(root1)
    f3.grid(row=9,column=2)
    Label(root1,text=" Address ").grid(row=11,column=0)
    f4=Entry(root1)
    f4.grid(row=11,column=2)
    Label(root1,text=" City ").grid(row=13,column=0)
    f5=Entry(root1)
    f5.grid(row=13,column=2)
    Label(root1,text=" Pincode ").grid(row=15,column=0)
    f6=Entry(root1)
    f6.grid(row=15,column=2)
    Label(root1,text=" Website URL ").grid(row=17,column=0)
    f7=Entry(root1)
    f7.grid(row=17,column=2)
    Label(root1,text=" Date of Birth ").grid(row=19,column=0)
    f8=Entry(root1)
    f8.grid(row=19,column=2)
    v1 = IntVar(root1,-1)
    Label(root1,text="Select Phone Type : ",font='Arial 15',fg='blue').grid(row=21,column=0)
    Radiobutton(root1,text="Office",variable=v1,value=0).grid(row=21,column=1)
    Radiobutton(root1,text="Home",variable=v1,value=1).grid(row=21,column=2)
    Radiobutton(root1,text="Mobile     ",variable=v1,value=2).grid(row=21,column=3)
    Label(root1,text=" Phone Number ").grid(row=23,column=0)
    f9=Entry(root1)
    f9.grid(row=23,column=2)
    v2 = IntVar(root1,-1)
    Label(root1,text="Select Email Type : ",font='Arial 15',fg='blue').grid(row=25,column=0)
    Radiobutton(root1,text="Office",variable=v2,value=0).grid(row=25,column=1)
    Radiobutton(root1,text="Personal",variable=v2,value=1).grid(row=25,column=2)
    Label(root1,text=" Email id ").grid(row=26,column=0)
    f10=Entry(root1)
    f10.grid(row=26,column=2)
    def save():
        fname=f.get()
        if fname=='':
            fname=' '
        mname=f1.get()
        if mname=='':
            mname=' '
        lname=f2.get()
        if lname=='':
            lname=' '
        coname=f3.get()
        if coname=='':
            coname=' '
        addr=f4.get()
        if addr=='':
            addr=' '
        city=f5.get()
        if city=='':
            city=' '
        pin=f6.get()
        if pin=='':
            pin=' '
        web=f7.get()
        if web=='':
            web=' '
        dob=f8.get()
        if dob=='':
            dob=' '
        phone=f9.get()
        if phone=='':
            phone=' '
        email=f10.get()
        if email=='':
            email=' '
        p=v1.get()
        if p==0:
            ptype='Office'
        elif p==1:
            ptype='Home'
        else:
            ptype='Mobile'
        e=v2.get()
        if e==0:
            etype='Office'
        else:
            etype='Personal'
        in_tab=[(fname,mname,lname,coname,addr,city,pin,web,dob,ptype,phone,etype,email)]
        cur.executemany("insert into record(cfname,cmname,clname,cconame,caddr,ccity,cpin,cweb,cdob,cptype,cphone,cetype,cemail) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",in_tab)
        con.commit()
        tkMessageBox.showinfo("Success", "Record saved sucessfully")
        f.delete(0, END)
        f1.delete(0, END)
        f2.delete(0, END)
        f3.delete(0, END)
        f4.delete(0, END)
        f5.delete(0, END)
        f6.delete(0, END)
        f7.delete(0, END)
        f8.delete(0, END)
        f9.delete(0, END)
        f10.delete(0, END)
        #cur.execute("select * from record")
        #print cur.fetchall()
    def search():
        root2=Tk()
        root2.title("Search")
        root2.geometry("550x600")
        Label(root2,text="Searching Phone Book",font='Arial 15',fg='blue').grid(row=0,column=0)
        Label(root2,text=" Enter Name :         ").grid(row=1,column=0)
        se=Entry(root2)
        se.grid(row=1,column=1)
        #Lb1 = Listbox(root2)
        Lb1 = Listbox(root2)
        Lb1['height'] = 50
        Lb1['width'] = 40
        def key_press(event):
            key = event.char
            key=str(key)
            skey=str(se.get())
            s1='%'+skey+'%'
            Lb1.delete(0,END)
            cur.execute("select cid,cfname,cmname,clname from record where cfname like ? or cmname like ? or clname like ? or cconame like ? or caddr like ? or ccity like ? or cpin like ? or cweb like ? or cdob like ? or cptype like ? or cphone like ? or cetype like ? or cemail like ?",(s1,s1,s1,s1,s1,s1,s1,s1,s1,s1,s1,s1,s1,))
            lis1=cur.fetchall()
            def showinfo(e=1):
                var=Lb1.curselection()
                newvar=int(var[0])
                #print newvar
                getid=(lis1[newvar][0])
                cur.execute("select * from record where cid = {0}".format(getid))
                lis2=cur.fetchall()
                #print lis2
                root3=Tk()
                root3.title("Info")
                root3.geometry("550x300")
                Label(root3,text="First Name : ").grid(row=1,column=0)
                if lis2[0][1]==' ':
                    x1=' '
                else:
                    x1=str(lis2[0][1])
                Label(root3,text=""+x1).grid(row=1,column=1)
                
                Label(root3,text="Middle Name : ").grid(row=2,column=0)
                if lis2[0][2]==' ':
                    x2=' '
                else:
                    x2=str(lis2[0][2])
                Label(root3,text=""+x2).grid(row=2,column=1)
                
                
                Label(root3,text="Last Name : ").grid(row=3,column=0)
                if lis2[0][3]==' ':
                    x3=' '
                else:
                    x3=str(lis2[0][3])
                Label(root3,text=""+x3).grid(row=3,column=1)
             

                Label(root3,text="Company : ").grid(row=4,column=0)
                if lis2[0][4]==' ':
                    x4=' '
                else:
                    x4=str(lis2[0][4])
                Label(root3,text=""+x4).grid(row=4,column=1)


                
                Label(root3,text="Address : ").grid(row=5,column=0)
                if lis2[0][5]==' ':
                    x5=' '
                else:
                    x5=str(lis2[0][5])
                Label(root3,text=""+x5).grid(row=5,column=1)


                Label(root3,text="City : ").grid(row=6,column=0)
                if lis2[0][6]==' ':
                    x6=' '
                else:
                    x6=str(lis2[0][6])
                Label(root3,text=""+x6).grid(row=6,column=1)


                Label(root3,text="Pin Code : ").grid(row=7,column=0)
                if lis2[0][7]==' ':
                    x7=' '
                else:
                    x7=str(lis2[0][7])
                Label(root3,text=""+x7).grid(row=7,column=1)


                Label(root3,text="Website URL : ").grid(row=8,column=0)
                if lis2[0][8]==' ':
                    x8=' '
                else:
                    x8=str(lis2[0][8])
                Label(root3,text=""+x8).grid(row=8,column=1)


                Label(root3,text="Date of Birth : ").grid(row=9,column=0)
                if lis2[0][9]==' ':
                    x9=' '
                else:
                    x9=str(lis2[0][9])
                Label(root3,text=""+x9).grid(row=9,column=1)


                Label(root3,text="Phone Details...").grid(row=10,column=0)
                if lis2[0][10]==' ':
                    x10=' '
                    Label(root3,text="None").grid(row=11,column=0)
                else:
                    x10=str(lis2[0][10])
                    Label(root3,text=""+x10+"  :").grid(row=11,column=0)
                    if lis2[0][11]==' ':
                        x11=' '
                    else:
                        x11=str(lis2[0][11])
                    Label(root3,text=""+x11).grid(row=11,column=1)


                Label(root3,text="Email Addresses...").grid(row=12,column=0)
                if lis2[0][12]==' ':
                    x12=' '
                    Label(root3,text="None").grid(row=13,column=0)
                else:
                    x12=str(lis2[0][12])
                    Label(root3,text=""+x12+"  :").grid(row=13,column=0)
                    if lis2[0][13]==' ':
                        x13=' '
                    else:
                        x13=str(lis2[0][13])
                    Label(root3,text=""+x13).grid(row=13,column=1)
                def close2():
                    root3.destroy()
                Button(root3,text='Close',command=close2).grid(row=15,column=0)
                def delete():
                    cur.execute("delete from record where cid=?",(lis2[0][0],))
                    tkMessageBox.showinfo("Success", "Record deleted sucessfully")
                    con.commit()
                    root3.destroy()
                    Lb1.delete(0,END)
                def edit():
                    root4=Tk()
                    root4.title("Edit Information")
                    root4.geometry("550x350")
                    Label(root4,text="Edit as per requirement : ").grid(row=0,column=0)
                    Label(root4,text="First Name : ").grid(row=1,column=0)
                    e1 = Entry(root4)
                    e1.insert(END, x1)
                    e1.grid(row=1,column=1)

                
                    Label(root4,text="Middle Name : ").grid(row=2,column=0)
                    e2 = Entry(root4)
                    e2.insert(END, x2)
                    e2.grid(row=2,column=1)


                    Label(root4,text="   Last Name : ").grid(row=3,column=0)
                    e3 = Entry(root4)
                    e3.insert(END, x3)
                    e3.grid(row=3,column=1)


                    Label(root4,text="   Comapany : ").grid(row=4,column=0)
                    e4 = Entry(root4)
                    e4.insert(END, x4)
                    e4.grid(row=4,column=1)


                    Label(root4,text="   Address : ").grid(row=5,column=0)
                    e5 = Entry(root4)
                    e5.insert(END, x5)
                    e5.grid(row=5,column=1)


                    Label(root4,text="   City : ").grid(row=6,column=0)
                    e6 = Entry(root4)
                    e6.insert(END, x6)
                    e6.grid(row=6,column=1)


                    Label(root4,text="   Pin Code : ").grid(row=7,column=0)
                    e7 = Entry(root4)
                    e7.insert(END, x7)
                    e7.grid(row=7,column=1)


                    Label(root4,text="   Website URL : ").grid(row=8,column=0)
                    e8 = Entry(root4)
                    e8.insert(END, x8)
                    e8.grid(row=8,column=1)


                    Label(root4,text="   Date of Birth  : ").grid(row=9,column=0)
                    e9 = Entry(root4)
                    e9.insert(END, x9)
                    e9.grid(row=9,column=1)


                    Label(root4,text="  Phone Details...").grid(row=10,column=0)
                    e10 = Entry(root4)
                    e10.insert(END, x10)
                    e10.grid(row=10,column=1)


                    Label(root4,text="  Phone Number   :").grid(row=11,column=0)
                    e11 = Entry(root4)
                    e11.insert(END, x11)
                    e11.grid(row=11,column=1)
                    

                    Label(root4,text="  Email Address Details   :").grid(row=12,column=0)
                    e12 = Entry(root4)
                    e12.insert(END, x12)
                    e12.grid(row=12,column=1)


                    Label(root4,text="   Email Address  :").grid(row=13,column=0)
                    e13 = Entry(root4)
                    e13.insert(END, x13)
                    e13.grid(row=13,column=1)

                    
                    #tkMessageBox.showinfo("Success", "Record edited sucessfully")
                    def change():
                        #print getid
                        fname=e1.get()
                        if fname=='':
                            fname=' '
                        mname=e2.get()
                        if mname=='':
                            mname=' '
                        lname=e3.get()
                        if lname=='':
                            lname=' '
                        coname=e4.get()
                        if coname=='':
                            coname=' '
                        addr=e5.get()
                        if addr=='':
                            addr=' '
                        city=e6.get()
                        if city=='':
                            city=' '
                        pin=e7.get()
                        if pin=='':
                            pin=' '
                        web=e8.get()
                        if web=='':
                            web=' '
                        dob=e9.get()
                        if dob=='':
                            dob=' '
                        ptype=e10.get()
                        if ptype=='':
                            ptype=' '
                        phone=e11.get()
                        if phone=='':
                            phone=' '
                        etype=e12.get()
                        if etype=='':
                            etype=' '
                        email=e13.get()
                        if email=='':
                            email=' '
                        cur.execute("update record set cfname = ? where cid = ?",(fname,getid,))
                        con.commit()
                        cur.execute("update record set cmname = ? where cid = ?",(mname,getid,))
                        con.commit()
                        cur.execute("update record set clname = ? where cid = ?",(lname,getid,))
                        con.commit()
                        cur.execute("update record set cconame = ? where cid = ?",(coname,getid,))
                        con.commit()
                        cur.execute("update record set caddr = ? where cid = ?",(addr,getid,))
                        con.commit()
                        cur.execute("update record set ccity = ? where cid = ?",(city,getid,))
                        con.commit()
                        cur.execute("update record set cpin = ? where cid = ?",(pin,getid,))
                        con.commit()
                        cur.execute("update record set cweb = ? where cid = ?",(web,getid,))
                        con.commit()
                        cur.execute("update record set cdob = ? where cid = ?",(dob,getid,))
                        con.commit()
                        cur.execute("update record set cptype = ? where cid = ?",(ptype,getid,))
                        con.commit()
                        cur.execute("update record set cphone = ? where cid = ?",(phone,getid,))
                        con.commit()
                        cur.execute("update record set cetype = ? where cid = ?",(etype,getid,))
                        con.commit()
                        cur.execute("update record set cemail = ? where cid = ?",(email,getid,))
                        con.commit()
                        tkMessageBox.showinfo("Success", "Record edited sucessfully")
                        root4.destroy()
                        root3.destroy()
                        root2.destroy()

                    Button(root4,text='Change',command=change).grid(row=15,column=1)                    
                
                Button(root3,text='Delete',command=delete).grid(row=15,column=1)
                Button(root3,text='Edit',command=edit).grid(row=15,column=2)
            for i in lis1:
                 text0=str(i[1])
                 text1=str(i[2])
                 text2=str(i[3])
                 Lb1.insert(END,text0+" "+text1+" "+text2)
                 Lb1.bind('<<ListboxSelect>>',showinfo)
                 Lb1.grid(row=3,column=1)
            #lis1=[]
            #Lb1.grid(row=3,column=1)
            #print key
                
        
        
              
        root2.bind('<Key>', lambda a : key_press(a))
        def close1():
            root2.destroy()
        Button(root2,text='Close',command=close1).grid(row=2,column=1)
    Button(root1,text='Save',command=save).grid(row=29,column=0)
    Button(root1,text='Search',command=search).grid(row=29,column=1)
    def close():
        root1.destroy()
    Button(root1,text='Close',command=close).grid(row=29,column=2)
        
root.bind('<Motion>',close)
mainloop()
