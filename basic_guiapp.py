from Tkinter import *
from importedfunc import *
from tkMessageBox import *
from PIL import ImageTk, Image
import os





root = Tk()
root.title("Megamic - Internship")
mainframe = Frame(root)
mainframe.grid(column = 0,row = 0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
tkvar = StringVar(root)
name = StringVar(root)
genderm = StringVar(root)
genderf = StringVar(root)
c = IntVar(root)


def reset_data():
	name.set("")
	tkvar.set("")
	genderm.set("")
	genderf.set("")
	c.set(0)
#new page for creating new window
def New_page():
	d = os.getcwd() +"/python.jpg"
	popup = Toplevel()
	popup.title("Megamic - Internship second Window")
	img = ImageTk.PhotoImage(Image.open(d))
	panel = Label(popup, image = img)  
	panel.grid(row = 0,column = 1)
	Label(popup,text = "This is example for\n displaying few line of\ntext in new window").grid(row = 1,column = 0)  
	link = Label(popup, text = "Learn More about Python", fg = "green", cursor = "hand2")
        link.grid(row = 2,column = 0)
        link.bind("<Button-1>", webhyper)
	popup.grab_set()



#configuring and defining menu
menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "open new window", command = New_page)
filemenu.add_command(label = "Open...")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)
# Dropdown selector configruations
choices = { 'Testing','Development','Support','API'}
tkvar.set('Development') # set the default option
#label for name
Label(mainframe,text = "Enter your name").grid(row = 0, column = 0)
Entry(mainframe,width = 20,textvariable = name).grid(row = 0,column = 1)
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text = "Choose Your Domain").grid(row = 1, column = 0)
popupMenu.grid(row = 1, column = 1) 

#label for checkbutton
Label(mainframe,text = "Have you done any internship?").grid(row = 2,column = 0)
Checkbutton(mainframe, text = "Yes", variable = c).grid(row = 2,column = 1)

#label for radio button
Label(mainframe,text = "Gender").grid(row = 3,column = 0)
Radiobutton(mainframe, 
              text = "Male",
              variable = genderm, 
              value = "Male").grid(row = 3 ,column = 1)
Radiobutton(mainframe, 
              text = "Female",
              variable = genderf, 
              value = "Female").grid(row = 3,column = 2)






#adding data and validating data
def adddata():
	'''function for validating empty fields'''
	if (tkvar.get() and name.get() and(genderm.get() or genderf.get())):
		writedata(name.get(),tkvar.get(),genderm.get(),genderf.get(),c.get())
		showinfo("Message", "Data Entered Sucessfully.")
		reset_data()
	else:
		showerror("Error", "Please fill all the fields")





#for displaying Data
def show():
	'''function for showing data from file'''
	configfile.insert(INSERT, "Name,Domain,Gender,Intern\n")
	with open('data_file.csv', 'r') as f:
		configfile.insert(INSERT, f.read())	




#submit Button
Button(mainframe, text = "Submit", command = adddata, relief = GROOVE,fg = 'green').grid(row = 4,column = 1)
#display Button
Button(mainframe, text ="Display", command = show,relief= GROOVE,fg='blue').grid(row = 5,column = 1)
Label(mainframe,text="Displaying Data").grid(row = 6,column = 1)
configfile = Text(mainframe, wrap=WORD, width = 40, height = 10)
configfile.grid(row = 7,column = 1)

 
root.mainloop()
