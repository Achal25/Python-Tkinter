from tkinter import *
from tkinter import messagebox


import sqlite3




 
root = Tk()
root.geometry('760x500')
root.title("WELCOME TO World Wrestling Entertainment")
 

bg = PhotoImage(file = 'img//second.png')
bg1 = PhotoImage(file = 'img//dusri.png')
bgi=PhotoImage(file='img//lal.png')
bgid=PhotoImage(file='img//dusri.png')
photo=PhotoImage(file = 'img//wwe.png')
photo1=PhotoImage(file = 'img//super.png')
photo2=PhotoImage(file = 'img//titles.png')
photo3=PhotoImage(file = 'img//sch.png')
photo4=PhotoImage(file = 'img//shop1.png')
photo5=PhotoImage(file = 'img//quizzzz.png')
photo6=PhotoImage(file = 'img//worldf.png')
photo7=PhotoImage(file = 'img//uc.png')
photo8=PhotoImage(file = 'img//us.png')
photo9=PhotoImage(file = 'img//smackw.png')
photo10=PhotoImage(file = 'img//raww.png')
photo11=PhotoImage(file = 'img//rawtag.png')
photo12=PhotoImage(file = 'img//tagsmack.png')
photo13=PhotoImage(file = 'img//24.png')
photo14=PhotoImage(file = 'img//nxt.png')
photo15=PhotoImage(file = 'img//crown.png')
photo16=PhotoImage(file = 'img//finn.png')
photo17=PhotoImage(file = 'img//hhh.png')
photo18=PhotoImage(file = 'img//inter.png')
photo19=PhotoImage(file = 'img//stone.png')
photo20=PhotoImage(file = 'img//edge.png')
photo21=PhotoImage(file = 'img//brockac.png')
photo22=PhotoImage(file = 'img//balor.png')
photo23=PhotoImage(file = 'img//shope.png')
photo24=PhotoImage(file = 'img//sajan.png')
photo25=PhotoImage(file = 'img//ticket1.png')
photo26=PhotoImage(file = 'img//ticket2.png')
photo27=PhotoImage(file = 'img//ticket3.png')
photo28=PhotoImage(file = 'img//News11.png')
photo29=PhotoImage(file = 'img//News15.png')
photo30=PhotoImage(file = 'img//News25.png')
photo31=PhotoImage(file = 'img//News27.png')

label7 = Label( root, image = bg)
label7.place(x = 0,y = 0)
  

icon=PhotoImage(file='img//wwe.png') #change icon 
root.iconphoto(True,icon)
 
Fullname=StringVar()
Email=StringVar()
var = StringVar()
c=StringVar()
var1= StringVar()
 
 
 
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('WWE.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS wrestlers (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Profession TEXT)')
   cursor.execute('INSERT INTO wrestlers (FullName,Email,Gender,country,Profession) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()


def box(): 
     messagebox.showinfo("WELCOME", "LOGIN SUCCESSFUL")


def openNewWindow1():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("760x500")

    label_j = Label(newWindow,image=photo28,width=1600)
    label_j.place(x=0,y=0,height=300)

    label_116 = Label(newWindow,image=photo29,width=1600)
    label_116.place(x=0,y=300,height=600)

    Button(newWindow,text="NEXT",command=NewsT,width=30,bg="blue",fg="white").place(x=700,y=770,height=30)
   

     



 
    # A Label widget to show in toplevel
    #label_a = Label(newWindow, text="World Wrestling Entertainment",width=50,font=("bold", 15),bg="Orange",fg="Black")
    #label_a.place(x=30,y=20) 


def NewsT():

    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("760x500")

    label_j = Label(newWindow,image=photo30,width=1600)
    label_j.place(x=0,y=0,height=300)

    label_112 = Label(newWindow,image=photo31,width=1600)
    label_112.place(x=0,y=300,height=600)


    



def openNewWindow2():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Championships")
 
    # sets the geometry of toplevel
    newWindow.geometry("760x500")
    label12 = Label( newWindow, image = bgid)
    label12.pack()
 
    # A Label widget to show in toplevel  
    label_j = Label(newWindow, text="Chamiopn",image=photo6,bg="blue",fg="red",width=200)
    label_j.place(x=40,y=0,height=200)
    label_k = Label(newWindow, text="World Championship", width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_k.place(x=30,y=180)
    label_m = Label(newWindow, text="Chamiopn",image=photo7,bg="blue",fg="red",width=200)
    label_m.place(x=40,y=250,height=200)
    label_l = Label(newWindow, text="Universal Championship", width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_l.place(x=30,y=430)
    label_n = Label(newWindow, text="Chamiopn",image=photo8,bg="blue",fg="red",width=200)
    label_n.place(x=40,y=500,height=250)
    label_o = Label(newWindow, text="US Championship", width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_o.place(x=30,y=730)
    label_p = Label(newWindow, text="Chamiopn",image=photo9,bg="blue",fg="red",width=200)
    label_p.place(x=600,y=0,height=200)
    label_p = Label(newWindow, text="Smackdown Women's Championship", width=30,font=("bold", 15),bg="Orange",fg="Black")
    label_p.place(x=540,y=180)
    label_q = Label(newWindow, text="Chamiopn",image=photo10,bg="blue",fg="red",width=200)
    label_q.place(x=600,y=250,height=200)
    label_r = Label(newWindow, text="Raw Women's Championship", width=30,font=("bold", 15),bg="Orange",fg="Black")
    label_r.place(x=540,y=430)
    label_s = Label(newWindow, text="Chamiopn",image=photo11,bg="blue",fg="red",width=200)
    label_s.place(x=600,y=500,height=250)
    label_t = Label(newWindow, text="Raw Tag Championship", width=30,font=("bold", 15),bg="Orange",fg="Black")
    label_t.place(x=540,y=730)
    label_u = Label(newWindow, text="Chamiopn",image=photo12,bg="blue",fg="red",width=200)
    label_u.place(x=1150,y=0,height=200)
    label_v = Label(newWindow, text="Smackdown Tag Championship", width=30,font=("bold", 15),bg="Orange",fg="Black")
    label_v.place(x=1080,y=180)
    label_x = Label(newWindow, text="Chamiopn",image=photo13,bg="blue",fg="red",width=200)
    label_x.place(x=1150,y=250,height=200)
    label_y = Label(newWindow, text="24x7 Championship", width=30,font=("bold", 15),bg="Orange",fg="Black")
    label_y.place(x=1080,y=430)
    label_z = Label(newWindow, text="Chamiopn",image=photo14,bg="blue",fg="red",width=200)
    label_z.place(x=1150,y=500,height=250)
    label69 = Label(newWindow, text="NXT Championship", width=30,font=("bold", 15),bg="orange",fg="Black")
    label69.place(x=1080,y=730)




  
def schedule(): 
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Schedule")
 
    # sets the geometry of toplevel
    newWindow.geometry("760x500") 

    label_1 = Label(newWindow, text="Chamiopn",image=photo15,bg="Red",fg="red")
    label_1.pack()
    label_2 = Label(newWindow,bg="Orange")
    label_2.place(x=0,y=0)


def quiz(): 
    newWindow=Toplevel(root)

    newWindow.title("Quiz")

    newWindow.geometry("760x500") 
    label12 = Label( newWindow, image = bgi,bg="Black")
    label12.pack()


    label_20 = Label(newWindow, text="Who won the Royal Rumble 2016?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_20.place(x=10,y=0)
    Button(newWindow,text="Brock Lesnar",command=box2,width=30,bg="blue",fg="white").place(x=170,y=50,height=30)
    Button(newWindow,text="Triple H", command=box1,width=30,bg="blue",fg="white").place(x=170,y=90,height=30)
    Button(newWindow,text="John Cena", command=box2,width=30,bg="blue",fg="white").place(x=170,y=130,height=30)
    Button(newWindow,text="Roman Reigns", command=box2,width=30,bg="blue",fg="white").place(x=170,y=170,height=30)

    label_21 = Label(newWindow, text="Which championship John Cena never held?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_21.place(x=10,y=230)
    Button(newWindow,text="World Championship",command=box4,width=30,bg="blue",fg="white").place(x=170,y=300,height=30)
    Button(newWindow,text="Tag Championship", command=box4,width=30,bg="blue",fg="white").place(x=170,y=340,height=30)
    Button(newWindow,text="Intercontinental Championship", command=box3,width=30,bg="blue",fg="white").place(x=170,y=380,height=30)
    Button(newWindow,text="United States Championship", command=box4,width=30,bg="blue",fg="white").place(x=170,y=420,height=30)

    label_22 = Label(newWindow, text="Who was special guest refree in BrockVSGoldberg match?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_22.place(x=10,y=500)
    Button(newWindow,text="The Rock",command=box6,width=30,bg="blue",fg="white").place(x=170,y=570,height=30)
    Button(newWindow,text="Kurt Angle", command=box6,width=30,bg="blue",fg="white").place(x=170,y=610,height=30)
    Button(newWindow,text="Stone Cold Steve Austin", command=box5,width=30,bg="blue",fg="white").place(x=170,y=650,height=30)
    Button(newWindow,text="Mr.Macmahon", command=box6,width=30,bg="blue",fg="white").place(x=170,y=690,height=30)
    

    label_23 = Label(newWindow, text="Who won inaugural MITB match?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_23.place(x=980,y=0)
    Button(newWindow,text="Kane",command=box8,width=30,bg="blue",fg="white").place(x=1150,y=50,height=30)
    Button(newWindow,text="Edge", command=box7,width=30,bg="blue",fg="white").place(x=1150,y=90,height=30)
    Button(newWindow,text="John Cena", command=box8,width=30,bg="blue",fg="white").place(x=1150,y=130,height=30)
    Button(newWindow,text="CM Punk", command=box8,width=30,bg="blue",fg="white").place(x=1150,y=170,height=30)

    label_24 = Label(newWindow, text="Undertaker Wrestlemania streak was broken by?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_24.place(x=980,y=230)
    Button(newWindow,text="Kane",command=box10,width=30,bg="blue",fg="white").place(x=1150,y=300,height=30)
    Button(newWindow,text="Brock Lesnar", command=box9,width=30,bg="blue",fg="white").place(x=1150,y=340,height=30)
    Button(newWindow,text="John Cena", command=box10,width=30,bg="blue",fg="white").place(x=1150,y=380,height=30)
    Button(newWindow,text="CM Punk", command=box10,width=30,bg="blue",fg="white").place(x=1150,y=420,height=30)
     
    label_25 = Label(newWindow, text="First Ever Universal Champion?",width=50,bg="Gold",fg="Black",font=("bold", 15))
    label_25.place(x=980,y=500)
    Button(newWindow,text="Roman Reigns",command=box12,width=30,bg="blue",fg="white").place(x=1150,y=570,height=30)
    Button(newWindow,text="Brock Lesnar", command=box12,width=30,bg="blue",fg="white").place(x=1150,y=610,height=30)
    Button(newWindow,text="Finn Balor", command=box11,width=30,bg="blue",fg="white").place(x=1150,y=650,height=30)
    Button(newWindow,text="Seth Rollins", command=box12,width=30,bg="blue",fg="white").place(x=1150,y=690,height=30)

def box1(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Triple H",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo17,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=50,height=700)

def box2():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Triple H",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo17,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=50,height=700)


def box3(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Intercontinental Title",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo18,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=50,height=500)

def box4():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Intercontinental Title",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo18,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=50,height=500)
     

def box5(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Stone cold Steve Austin",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo19,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1000)

def box6():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Stone cold Steve Austin",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo19,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1000)
     

def box7(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Edge",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo20,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1400)

def box8():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Edge",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo20,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1400)



def box9(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Brock lesnar",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo21,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=900)

def box10():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Brock Lesnar",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo21,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=900)




def box11(): 
     newWindow=Toplevel(root)
     newWindow.geometry("550x550") 
     Label(newWindow, text="Correct!!The answer is Finn Balor",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0) 
     label_6 = Label(newWindow, text="Chamiopn",image=photo22,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1100)

def box12():
     newWindow=Toplevel(root)
     newWindow.geometry("550x550")
     Label(newWindow, text="Incorrect!!The correct answer is Finn Balor",width=50,bg="Gold",fg="Black",font=("bold", 15)).place(x=0,y=0)
     label_6 = Label(newWindow, text="Chamiopn",image=photo22,bg="Red",fg="red",width=350)
     label_6.place(x=10,y=70,height=1100)



def shop(): 
   newWindow=Toplevel(root)

   newWindow.title("Shop")

   newWindow.geometry("760x500") 
   label41 = Label( newWindow, image = bgi)
   label41.pack()

   label_42 = Label(newWindow, text="Visit the official website for more",width=50,font=("bold", 25),bg="gold",fg="red")
   label_42.place(x=200,y=380)

   

   label_7 = Label(newWindow, text="Chamiopn",image=photo23,bg="Red",fg="red",width=1300)
   label_7.place(x=50,y=10,height=250)

   label_9 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_9.place(x=70,y=250)

   label_18 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_18.place(x=1170,y=250)
     
   label_19 = Label(newWindow, text="50$",bg="gold",fg="red",width=20)
   label_19.place(x=500,y=250)

   label_31 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_31.place(x=300,y=250)

   label_32 = Label(newWindow, text="50$",bg="gold",fg="red",width=20)
   label_32.place(x=730,y=250)
     
   label_33 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_33.place(x=950,y=250)


   label_34 = Label(newWindow, text="Chamiopn",image=photo24,bg="Red",fg="red",width=1300)
   label_34.place(x=50,y=500,height=250)  

   label_35 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_35.place(x=70,y=750)

   label_36 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_36.place(x=1170,y=750)
     
   label_37 = Label(newWindow, text="50$",bg="gold",fg="red",width=20)
   label_37.place(x=500,y=750)

   label_38 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_38.place(x=300,y=750)

   label_39 = Label(newWindow, text="50$",bg="gold",fg="red",width=20)
   label_39.place(x=730,y=750)
     
   label_40 = Label(newWindow, text="99$",bg="gold",fg="red",width=20)
   label_40.place(x=950,y=750)


def tickets():

   newWindow=Toplevel(root)

   newWindow.title("Tickets")

   newWindow.geometry("760x500") 

   label_35 = Label(newWindow, text="Chamiopn",image=photo25,fg="red",width=1400)
   label_35.place(x=0,y=0,height=300)  

   label_36 = Label(newWindow, text="Chamiopn",image=photo26,bg="Red",fg="red",width=1400)
   label_36.place(x=0,y=280,height=280)  
   

   label_37 = Label(newWindow, text="Chamiopn",image=photo27,bg="Red",fg="red",width=1400)
   label_37.place(x=0,y=550,height=280) 



def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")   
 
    # sets the geometry of toplevel
    newWindow.geometry("760x500")
    

    labelb = Label( newWindow, image = bg1)
    labelb.place(x = 0,y = 0)
 
    # A Label widget to show in toplevel
    
    label_a = Label(newWindow, text="World Wrestling Entertainment",width=50,font=("bold", 25),bg="Orange",fg="Black")
    label_a.place(x=300,y=20)
    label_d = Label(newWindow, text="TICKETS",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_d.place(x=620,y=380)
    label_e = Label(newWindow, text="NEWS",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_e.place(x=130,y=380)
    label_f = Label(newWindow, text="CHAMPIONSHIPS",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_f.place(x=1130,y=380)
    label_g = Label(newWindow, text="Schedule",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_g.place(x=115,y=750)
    label_h = Label(newWindow, text="Shop",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_h.place(x=615,y=750)
    label_i = Label(newWindow, text="QUIZ",width=20,font=("bold", 15),bg="Orange",fg="Black")
    label_i.place(x=1120,y=750)
    Button(newWindow,text="Continue",width=280,bg="brown",fg="white",command=openNewWindow1,image=photo).place(x=100,y=100,height=280) 
    Button(newWindow,text="Superstars",width=250,bg="brown",fg="white",image=photo1,compound=BOTTOM,command=tickets).place(x=600,y=100,height=280)
    Button(newWindow,text="championship",width=275,bg="brown",fg="white",image=photo2,command=openNewWindow2).place(x=1100,y=100,height=280)
    Button(newWindow,text="Sch",width=250,bg="brown",fg="white",image=photo3,command=schedule).place(x=100,y=500,height=250)
    Button(newWindow,text="Quizz",width=250,bg="white",fg="white",image=photo4,command=shop).place(x=600,y=500,height=250)
    Button(newWindow,text="Schedule",width=250,bg="brown",fg="white",image=photo5,command=quiz).place(x=1100,y=500,height=250)
    #Button(newWindow,text="Merchandises",width=280,bg="brown",fg="white",image=photo).place(x=100,y=100,height=280)
  
    
    
              
label_0 = Label(root, text="World Wrestling Entertainment",width=50,font=("bold", 15),bg="Orange",fg="Black")
label_0.place(x=30,y=20)
 
 
label_1 = Label(root, text="FullName",width=20,font=("bold", 10),bg="brown",fg="White")
label_1.place(x=80,y=130)
 
entry_1 = Entry(root,textvar=Fullname,width=30)
entry_1.place(x=260,y=130,height=20)
 
label_2 = Label(root, text="Email",width=20,font=("bold", 10),bg="brown",fg="White")
label_2.place(x=80,y=180)
 
entry_2 = Entry(root,textvar=Email,width=30)
entry_2.place(x=260,y=180,height=20)
 
label_3 = Label(root, text="Gender",width=20,font=("bold", 10),bg="brown",fg="White")
label_3.place(x=80,y=230)
 
list1=['Male','Female','Others'];
droplist1=OptionMenu(root,var,*list1)
droplist1.config(width=15)
var.set('Select your Gender')
droplist1.place(x=280,y=225)


label_4 = Label(root, text="country",width=20,font=("bold", 10),bg="brown",fg="White")
label_4.place(x=80,y=280)
 
list1 = ['Philippines','Japan','Los Santos','California','New York','Death Valley'];
 
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select your country') 
droplist.place(x=280,y=275)
 
label_4 = Label(root, text="Role",width=20,font=("bold", 10),bg="brown",fg="White")
label_4.place(x=80,y=330)

list3=['Wrestler','Manager','Owner','Commentator','Refree']; 

droplist3=OptionMenu(root,var1,*list3)
droplist3.config(width=15)
var1.set('Select your Role') 
droplist3.place(x=280,y=328) 

 
Button(root, text='Submit',width=20,bg='brown',fg='white',command=box).place(x=300,y=400)
Button(root,text="Confirm",width=20,bg="brown",fg="white",command=database).place(x=145,y=400)
Button(root,text="Continue",width=20,bg="brown",fg="white",command=openNewWindow).place(x=455,y=400)
root.mainloop()