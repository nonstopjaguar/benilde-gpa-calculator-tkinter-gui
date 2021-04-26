from tkinter import * 
import tkinter.messagebox


check = "benilde"
def options():
    global check
    if subject_grade.get() == 1 :
        Number_Options.grid_forget()

subject_number = 0
def Add_Subject():
    global subject_number ,check ,point
    grade = DoubleVar()
    points = DoubleVar()
    if check == "" :
                subject_number += 1
                subject_number_Display.configure(text = subject_number)
                unitsList.append(units.get())
                units_number_Display.configure(text = sum(unitsList))
                gradeList.append(points)
                grade = points
                all_List.append( float(grade * units.get()) )

            

    elif check == "benilde" :
        subject_number += 1
        subject_number_Display.configure(text = subject_number)
        unitsList.append(units.get())
        units_number_Display.configure(text = sum(unitsList))
        gradeList.append(Number_Points.get(number.get()))
        grade = Number_Points.get(number.get())
        all_List.append( float(grade * units.get()) )

def Undo_Subject() :
    global subject_number
    if len(all_List) != 0 :
        unitsList.pop()
        gradeList.pop()
        all_List.pop()
        subject_number -= 1
        if subject_number == 0 and sum(unitsList) == 0 :
            subject_number_Display.configure(text = "")
            units_number_Display.configure(text = "")
            alpha.configure(text = "")
        else :
            subject_number_Display.configure(text = subject_number)
            units_number_Display.configure(text = sum(unitsList))

    else: tkinter.messagebox.showwarning("ERROR!" ,"You must add a subject before you undo!")

def calculate_gpa() :
    if sum(unitsList) != 0 :
        gpa = float(sum(all_List)/sum(unitsList))
        print ("Grade Points:")
        print (sum(all_List))
        print("")
        print ("Units:")
        print (sum(unitsList))
        print("")
        print ("General Point Average:")
        print (sum(all_List)/sum(unitsList))
        grade = StringVar()
        f_color = StringVar()
        let = StringVar()
        
        if gpa >= 3.5 and gpa <= 4.0 :
            grade = "1st Honors!"
            f_color = "green"
            let = ":)"
        elif gpa >= 3.0 and gpa < 3.5 :
            grade = "2nd Honors!"
            f_color = "green"
            let = ":)"
        elif gpa >= 0.0 and gpa < 3.0 :
            grade = "Not Qualified"
            f_color = "red"
            let = ":("
        else :
            grade = ""
            let = ""

        general_Display.configure(text = round(gpa ,3))
        Grade_Display.configure(text = grade ,fg = f_color)
        alpha.configure(text = let)

    else :tkinter.messagebox.showwarning("ERROR!" ,"You must add a subject before you calculate!")

def New_Input():
    global check ,subject_number
    subject_number = 0
    Number_Options.grid(row = 0 ,column = 1)
    check = "benilde"
    subject_number_Display.configure(text = "")
    units_number_Display.configure(text = "")
    general_Display.configure(text = "")
    Grade_Display.configure(text = "")
    alpha.configure(text = "")
    
    gradeList.clear()
    unitsList.clear()
    all_List.clear()

def About():
    root.maxsize(width = 280 ,height = 400)
    tkinter.messagebox.showinfo("" ,"This General Point Average (GPA) Calculator is a partnership project of the Benilde Central Student Government, and the Computer Business Association.")
    tkinter.messagebox.showinfo("" ,"Created by: Lance Salen")
    root.maxsize(width = 280 ,height = 270)

def Help():
    root.maxsize(width = 280 ,height = 400)
    tkinter.messagebox.showinfo("" ,"To add a subject, choose the equivalent grade in the dropdown list.")
    tkinter.messagebox.showinfo("" ,"Choose the number of units of your subject, then click the Add Subject button.")
    tkinter.messagebox.showinfo("" ,"After adding all your subjects, click the Calculate button to continue.")
    tkinter.messagebox.showinfo("" ,"If you had a wrong input of your subject, you can click the Undo Subject button.")
    tkinter.messagebox.showinfo("" ,"If you want to compute a new set of subjects, just click the New Input button and input your new subjects.")
    tkinter.messagebox.showinfo("" ,"Thank you! If you have any concerns, email me at lancebert.salen@benilde.edu. ph.")
    root.maxsize(width = 280 ,height = 270)



root = Tk()
root.title("De La Salle-College of Saint Benilde General Point Average Calculator")
root.iconphoto(False, PhotoImage(file='benilde.png'))


number = StringVar()
number.set("4")
units = IntVar()
subject_grade = IntVar()
gradeList = []
unitsList = []
all_List = []
Number_Points = {'4':4.0,'3.5':3.5,'3':3.0,'2.5':2.5,'2':2.0,'1.5':1.5,'1':1.0,'R':0.0,}


Top_Frame = Frame(root)
Top_Frame.pack(side = TOP)

subject_grade_units = LabelFrame(Top_Frame ,relief = FLAT)
subject_grade_units.pack(side = TOP )

subject_grade_LabelFrame = LabelFrame(subject_grade_units ,text = "Subject Grade")
subject_grade_LabelFrame.pack(side = LEFT ,padx = 5)

units_lblFrame = LabelFrame(subject_grade_units ,text = "Number of Units")
units_lblFrame.pack(side = RIGHT ,padx = 5)

Label(subject_grade_LabelFrame ,text = "List:").grid(row =0)


Number_Options = OptionMenu(subject_grade_LabelFrame ,number ,"4" ,"3.5" ,"3" ,"2.5" ,"2" ,"1.5" ,"1" ,"R")
Number_Options.grid(row = 0 ,column = 1)

Radiobutton(units_lblFrame ,text = "2" ,variable = units ,value = 2).pack(side = LEFT)
units_RadioBtn = Radiobutton(units_lblFrame ,text = "3" ,variable = units ,value = 3) 
units_RadioBtn.pack(side = RIGHT)
units_RadioBtn.select()

gpa_grade_frame = Frame(Top_Frame ,relief = FLAT)
gpa_grade_frame.pack(side = BOTTOM ,pady = 5)

Button(gpa_grade_frame ,text = "Add Subject" ,command = Add_Subject ,bg = "#e6e6e6").grid(row = 0 ,pady = 5) 

Button(gpa_grade_frame ,text = "Undo Subject" ,command = Undo_Subject ,bg = "#e6e6e6").grid(row = 1) 
Label(gpa_grade_frame ,text = "Number of Subjects:").grid(row = 0 ,column = 1 ,pady = 2)
subject_number_Display = Label(gpa_grade_frame ,relief = RIDGE ,width = 2) 
subject_number_Display.grid(row = 0, column = 2 ,pady = 2)

Label(gpa_grade_frame ,text = "Number of Units:").grid(row = 1 ,column = 1 ,pady = 2)
units_number_Display = Label(gpa_grade_frame ,relief = RIDGE ,width = 2) 
units_number_Display.grid(row = 1 ,column = 2 ,pady = 2)

Button(gpa_grade_frame ,text = "Calculate" ,width = 15 ,command = calculate_gpa ,bg = "#e6e6e6").grid(row = 2 ,columnspan = 3 ,pady = 5)
Label(gpa_grade_frame ,text = "General Point Average (GPA):").grid(row = 3)

general_Display = Label(gpa_grade_frame ,relief = RIDGE ,width = 15) 
general_Display.grid(row = 3 ,column = 1)

Label(gpa_grade_frame ,text = "Dean's Lister Status:").grid(row = 4)
Grade_Display = Label(gpa_grade_frame ,relief = RIDGE ,width = 15) 
Grade_Display.grid(row = 4 ,column = 1)

alpha = Label(gpa_grade_frame ,relief = RIDGE ,width = 2)
alpha.grid(row = 3 ,rowspan = 2 ,column = 3)

Bottom_Frame = Frame(root)
Bottom_Frame.pack(side = BOTTOM)

buttons_LabelFrame = LabelFrame(Bottom_Frame ,relief = FLAT)
buttons_LabelFrame.pack(side = TOP ,pady = 5)

Button(buttons_LabelFrame ,text = " New Input  " ,command = New_Input ,bg = "#e6e6e6").pack(side =LEFT ,padx = 15) 
root.minsize(width= 280 ,height = 270)

Button(buttons_LabelFrame ,text = "About" ,command = About ,bg = "#e6e6e6").pack(side = RIGHT ,padx = 15)

Button(buttons_LabelFrame ,text = "Help" ,command = Help ,bg = "#e6e6e6").pack(side = RIGHT ,padx = 15)

root.mainloop()
