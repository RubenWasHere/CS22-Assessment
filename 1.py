"""Julie's party hire"""

#import tkinter to make a GUI
from tkinter import *
from tkinter import ttk

window_width = 300
window_height = 200

#quit function for the quit button
def quit():
    main_window.destroy()
#printing the entry details
def print_details():
    #variables used
    global details, total_entries, info
    info=0
    #making column headings
    Label(main_window,text='Full Name').grid(column=0,row=7)
    Label(main_window,text='Receipt Number').grid(column=1,row=7)
    Label(main_window,text='Item Hired',).grid(column=2,row=7)
    Label(main_window,text='Quantity').grid(column=3,row=7)
    Label(main_window,text='Row').grid(column=4,row=7)
                        
    #adding each item in the list into their own row
    while info < total_entries:
        Label(main_window,text=info).grid(column=4,row=info+8)
        Label(main_window,text=(details[info][0])).grid(column=0,row=info+8)
        Label(main_window,text=(details[info][1])).grid(column=1,row=info+8)
        Label(main_window,text=(details[info][2])).grid(column=2,row=info+8)
        Label(main_window,text=(details[info][3])).grid(column=3,row=info+8)
        info+= 1

#appending the customer details
def append_details():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    #append each deteails to its own area of list
    details.append([entry_customer_name.get(),
                    entry_receipt_number.get(),
                    entry_item_held.get(),
                    entry_number_hired.get(),
                    delete_item.get()])
                    
    #clearing the boxes
    entry_customer_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_item_held.delete(0,'end')
    entry_number_hired.delete(0,'end')
    delete_item.delete(0,'end')
    total_entries +=1
#deleting row from the list
def delete_row():
    #variables used
    global details,delete_item,total_entries,info
    #find which row to be deleted
    del details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    #clearing the last detail displayed on the GUI
    Label(main_window, text="                                                       ").grid(column=0, row=info+7)
    Label(main_window, text="                                                       ").grid(column=1, row=info+7)
    Label(main_window, text="                                                       ").grid(column=2, row=info+7)
    Label(main_window, text="                                                       ").grid(column=3, row=info+7)
    Label(main_window, text="                                                       ").grid(column=4, row=info+7)
    #print every item in the list
    print_details()
#creating buttons and labels
def buttons():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,delete_item,total_entries
    #creating buttons
    Button(main_window,text='Quit', command=quit, width=10).grid(column=2,row=1,sticky=W)
    Button(main_window,text='Append Details',command=check).grid(column=0,row=1,sticky=W)
    Button(main_window,text='Print Details',command=print_details,width=10).grid(column=1,row=1)
    #creating empty entry boxes and putting labels
    Label(main_window,text='Customer Name').grid(column=0,row=2)
    entry_customer_name=Entry(main_window)
    entry_customer_name.grid(column=1,row=2)
    Label(main_window,text='Receipt Number').grid(column=0,row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1,row=3)
    Label(main_window,text='Item Hired').grid(column=0,row=4)
    #creating a combo box for the items held
    item_held=StringVar()
    entry_item_held=ttk.Combobox(main_window,textvariable=item_held,state='readonly',
                                 values=('Table, Chair and Linen',
                                         'Crockery and Tableware',
                                         'LED/Neon lights','Backdrop',
                                         'Glassware and Bar','Prop',
                                         'Kids Among Us Party','Chalkboard and signage',
                                         'Wedding and aisle','Ballon garland',
                                         'Themed decoration','Helium and Balloons',
                                         'Catering'),width=17)
    entry_item_held.grid(column=1,row=4)
    Label(main_window,text='Number Hired').grid(column=0,row=5)
    entry_number_hired=Entry(main_window)
    entry_number_hired.grid(column=1,row=5)
    #row deleting
    Label(main_window,text='Delete Row #').grid(column=0,row=6)
    delete_item=Entry(main_window)
    delete_item.grid(column=1,row=6)
    Button(main_window,text='Delete Row',command=delete_row,width=10).grid(column=2,row=6,sticky=W)
#checking if the inputs are all valid
def check():
    #variables used
    global details, entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    entry_check=0
    Label(main_window, text="                                                           ") .grid(column=2, row=2)
    Label(main_window, text="                                                           ") .grid(column=2, row=3)
    Label(main_window, text="                                                           ") .grid(column=2, row=4)
    Label(main_window, text="                                                           ") .grid(column=2, row=5)
    #checking that costumer name is not blank, set error text if blank
    if len(entry_customer_name.get())==0:
        Label(main_window,fg='orange',text='Please enter your name').grid(column=2,row=2,sticky=W)
        entry_check=1
        
    #checking that receipt is not blank and sending error if its blank
    if len(entry_receipt_number.get())==0:
        Label(main_window,fg='orange',text='Please enter your receipt number').grid(column=2,row=3,sticky=W)
        entry_check=1
    #checking that item held is not blank and sending error if its blank
    if len(entry_item_held.get()) == 0:
        Label(main_window,fg='orange',text='Please choose your item').grid(column=2,row=4,sticky=W)
        entry_check=1
    #checking that number hired is not blank and sending error if its blank
    if (entry_number_hired.get().isdigit()):
        if int(entry_number_hired.get()) < 1 or int(entry_number_hired.get()) > 500:
            Label(main_window,fg='orange',text='1 to 500 only').grid(column=2,row=5,sticky=W)
            entry_check=1
    else:
        Label(main_window,fg='orange',text='1 to 500 only').grid(column=2,row=5,sticky=W)
        entry_check=1
    if entry_check ==0:
        append_details()


def image():
        logoimg = PhotoImage(file="logo.png")
        logo = Label(main_window, image = logoimg)
        logo.image = logoimg
        logo.grid(column=1, row=0, columnspan=1)
        


#to start the program
def main():
    #variables used
    global main_window
    global details,entry_customer_name,entry_receipt_number,entry_item_held,entry_number_hired,total_entries
    #creating an empty list for the details
    details=[]
    total_entries=0
    #creating the GUI to start it
    main_window=Tk()
    buttons()
    image()
    main_window.mainloop()

    
main()
