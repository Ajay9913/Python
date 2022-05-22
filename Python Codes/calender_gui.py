#Ajay Bandgar

from tkinter import *
import calendar

def showCalendar():
    gui = Tk()
    gui.config(background = 'grey')
    gui.title("calender for the Year")
    gui.geometry("1980x1080")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text = gui_content, font = "Consoles 10 bold")
    calYear.grid(row = 5, column = 1, padx = 20)
    gui.mainloop()
    
if __name__ == '__main__':
    new = Tk()
    new.config(background ='grey')
    new.title("Calender of Ajay")
    new.geometry("200x180")
    cal = Label(new,text = "Calender", bg='grey', font= ("times",28,"bold"))
    year = Label(new,text="Enter Year", bg = 'dark grey')
    year_field = Entry(new)
    button = Button(new, text = 'Show Cal', fg='Black', bg='Light Blue', command=showCalendar)
    Exit = Button(new, text='Exit',fg='Black', bg='Light Blue', command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    new.mainloop()
    
