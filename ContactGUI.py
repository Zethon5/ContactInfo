import pandas as pd
import csv
from tkinter import *

win = Tk()
win.title('Contacts')
win.minsize(width = 300, height=370)

#-----FUNCTIONS---------------
def contactDisplay():
    col_names = ['Name', 'Phone', 'Email', 'Address']
    data = pd.read_csv('contactlist.csv', names=col_names)
    data.set_index('Name', inplace=True)
    nameSearch = str(entryName.get())
    if nameSearch in data.index:
        #MY BUNK WAY OF ERASING THE DISPLAY OF PREVIOUS SEARCH
        nameLabel = Label(win, text='                                                           ')
        nameLabel.grid(row=3, column=1, pady=2)
        phoneLabel = Label(win, text='                                                          ')
        phoneLabel.grid(row=4, column=1, pady=2)
        emailLabel = Label(win, text='                                                           ')
        emailLabel.grid(row=5, column=1, pady=2)
        addressLabel = Label(win, text='                                                         ')
        addressLabel.grid(row=6, column=1, pady=2)

        #THIS IS WHAT THE SEARCH ULTIMATELY DISPLAYS
        nameLabel = Label(win, text=nameSearch)
        nameLabel.grid(row=3, column=1, pady=2)
        nameLabel1 = Label(win, text='NAME:     ')
        nameLabel1.grid(row=3, column=0, pady=2)

        phoneLabel = Label(win, text=str(data.loc[nameSearch]['Phone']))
        phoneLabel.grid(row=4, column = 1, pady=2)
        phoneLabel1 = Label(win, text='PHONE:    ')
        phoneLabel1.grid(row=4, column=0, pady=2)

        emailLabel = Label(win, text=str(data.loc[nameSearch]['Email']))
        emailLabel.grid(row=5, column = 1, pady =2)
        emailLabel1 = Label(win, text='EMAIL:    ')
        emailLabel1.grid(row=5, column=0, pady=2)

        addressLabel = Label(win, text =str(data.loc[nameSearch]['Address']))
        addressLabel.grid(row=6, column = 1, pady= 2)
        addressLabel1 = Label(win, text='ADDRESS:')
        addressLabel1.grid(row=6, column=0, pady=2)

    else:
        def enterTheInfo():
            nameSearch = str(entryName.get())
            newPhone = str(phoneEntry.get())
            newEmail = str(emailEntry.get())
            newAddress = str(addressEntry.get())
            with open('contactlist.csv', 'a') as df:
                writer = csv.writer(df)
                writer.writerow([nameSearch, newPhone, newEmail, newAddress])
            nameLabel2.destroy()
            phoneLabel.destroy()
            phoneEntry.destroy()
            emailLabel.destroy()
            emailEntry.destroy()
            addressLabel.destroy()
            addressEntry.destroy()
            nameLabel.destroy()
            buttonEnter.destroy()

        nameLabel = Label(win, text=nameSearch + ' not found.')
        nameLabel.grid(row=7, column = 0, pady =2)
        nameLabel2= Label(win, text='Enter info Below')
        nameLabel2.grid(row=7, column = 1, pady =2)
        phoneLabel = Label(win, text='PHONE:')
        phoneLabel.grid(row=8, column=0, pady=2)
        phoneEntry = Entry(bg='#F2F4F4')
        phoneEntry.grid(row=8, column=1, pady=2)
        emailLabel = Label(win, text='EMAIL:')
        emailLabel.grid(row=9, column=0, pady=2)
        emailEntry = Entry(bg='#F2F4F4')
        emailEntry.grid(row=9, column=1, pady=2)
        addressLabel = Label(win, text='ADDRESS:')
        addressLabel.grid(row=10, column=0, pady=2)
        addressEntry = Entry(bg='#F2F4F4')
        addressEntry.grid(row=10, column=1, pady=2)
        buttonEnter = Button(win, text='Enter Info', command = enterTheInfo)
        buttonEnter.grid(row=11, columnspan = 2, pady=2)

#-------LABELS--------------
titleLabel = Label(win, text ='Welcome, please enter first and last name in the box.')
titleLabel.grid(row = 0, columnspan =2 )

#------ENTRY POINT----------
entryName = Entry(bg='#F2F4F4')
entryName.grid(row = 1, columnspan = 2, pady = 3)

#------THE BUTTONS----------
buttonSearch = Button(win, text='Search', command = contactDisplay)
buttonSearch.grid(row=2, columnspan = 2, pady =3)

win.mainloop()