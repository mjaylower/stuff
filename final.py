import pickle
import tkinter
import tkinter.messagebox


class NameAndAddress:

    def __init__(self):

        # CREATE MAIN WINDOW
        self.main_window = tkinter.Tk()
        self.main_window.title('Name and Address Directory')
        self.main_window.geometry('500x300')

        # DEFINE FRAMES TO BE USED
        self.header_frame = tkinter.Frame(self.main_window)  # HEADER FRAME TO EXPLAIN PROGRAM
        self.first_frame = tkinter.Frame(self.main_window)  # FRAME TO DISPLAY BUTTON OPTIONS
        self.second_frame = tkinter.Frame(self.main_window)  # FRAME TO DISPLAY IN BOX TEXT/LABEL
        self.third_frame = tkinter.Frame(self.main_window)  # FRAME TO DISPLAY OK AND EXIT BUTTONS

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='NAME AND EMAIL DIRECTORY', width=50)

        # PACK HEADER FRAME
        self.header_label.pack()

        # FIRST FRAME
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        self.lookup_radio_button = tkinter.Radiobutton(self.first_frame, text='LOOKUP', variable=self.radio_var, value=1)
        self.add_radio_button = tkinter.Radiobutton(self.first_frame, text='ADD', variable=self.radio_var, value=2)
        self.change_radio_button = tkinter.Radiobutton(self.first_frame, text='CHANGE', variable=self.radio_var, value=3)
        self.delete_radio_button = tkinter.Radiobutton(self.first_frame, text='DELETE', variable=self.radio_var, value=4)
        self.quit_save_radio_button = tkinter.Radiobutton(self.first_frame, text='SAVE', variable=self.radio_var, value=5)

        # PACK FIRST FRAME RADIO BUTTONS
        self.lookup_radio_button.pack()
        self.add_radio_button.pack()
        self.change_radio_button.pack()
        self.delete_radio_button.pack()
        self.quit_save_radio_button.pack()

        # SECOND FRAME
        self.name_entry_label = tkinter.Label(self.second_frame, text='NAME ')
        self.name_entry = tkinter.Entry(self.second_frame, width=25)
        self.email_entry_label = tkinter.Label(self.second_frame, text='EMAIL')
        self.email_entry = tkinter.Entry(self.second_frame, width=30)

        self.name_entry_label.pack()
        self.name_entry.pack()
        self.email_entry_label.pack()
        self.email_entry.pack()

        # THIRD FRAME
        self.ok_button = tkinter.Button(self.third_frame, text='OK', command=self.main)
        self.save_exit_button = tkinter.Button(self.third_frame, text='EXIT', command=self.quit_and_save and self.main_window.destroy)

        self.ok_button.pack()
        self.save_exit_button.pack()

        self.header_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()

        # INITIATE WINDOW LOOP
        tkinter.mainloop()

    def main(self):

        try:
            input_file = open('name_and_email.dat', 'rb')  # TRIES TO OPEN DATA FILE WITH 'RB' SO IT CAN PICKLE
            name_and_email = pickle.load(input_file)  # DATA FOUND ON FILE WILL BE MAPPED TO VARIABLE
            print(name_and_email)  # USED TO TEST CONTENT OF FILE TO ENSURE READING DATA CORRECTLY
        except (FileNotFoundError, IOError):  # IF EITHER ERROR OCCURS, FOLLOWING WILL TAKE PLACE
            name_and_email = {}  # CREATES AN EMPTY DICTIONARY SINCE ONE DOESN'T EXIST YET BASED ON ERROR OCCURRENCE
            print('File Not Found, Please Add Data To Create New File')  # SAYS NO FILE FOUND, NEED TO CREATE AND SAVE WITHIN PROGRAM

        choice = self.radio_var.get()  # RUN THE 'GET_MENU_CHOICE' FUNCTION AND RETURN 'ANSWER'

        if choice == 1:  # IF 1 IS SELECTED, RUN THE 'LOOK_UP' FUNCTION
            self.lookup(name_and_email)
        elif choice == 2:  # IF 2 IS SELECTED, RUN THE 'ADD' FUNCTION
            self.add(name_and_email)
        elif choice == 3:  # IF 3 IS SELECTED, RUN THE 'CHANGE' FUNCTION
            self.change(name_and_email)
        elif choice == 3:  # IF 4 IS SELECTED, RUN THE 'DELETE' FUNCTION
            self.delete(name_and_email)
        elif choice == 5:  # IF 5 IS SELECTED, RUN THE 'QUIT_AND_SAVE' FUNCTION - PROGRAM ENDS
            self.quit_and_save(name_and_email)

    def lookup(self, name_and_email):
        name = self.name_entry.get()

        if name in name_and_email:
            tkinter.messagebox.showinfo('Information', name_and_email.get(name))
        else:
            tkinter.messagebox.showinfo('Information', name + ' Was Not Found')

# ADD NAME AND EMAIL TO 'NAME_AND_EMAIL' DICTIONARY
    def add(self, name_and_email):
        name = self.name_entry.get()
        email = self.email_entry.get()  # ASK USER TO ENTER AN EMAIL (WILL BE THE VALUE)
        print(name, email)

        if name not in name_and_email:  # IF NAME DOESN'T EXIST, ADD NEW KEY-VALUE PAIR TO NAME_AND_EMAIL DICTIONARY
            name_and_email[name] = email
            tkinter.messagebox.showinfo('Information', name + ' has been added to your database')

        else:
            tkinter.messagebox.showinfo('Information', name + ' already exists. Please select the "CHANGE" option to make an update to ' + name + "'s email OR, please specify further which ' + name + ' you\'re referring to.")

    # CHANGE EMAIL OF EXISTING NAME FROM NAME_AND_EMAIL DICTIONARY
    def change(self, name_and_email):

        name = self.name_entry.get()

        if name in name_and_email:  # IF NAME EXIST IN DICTIONARY, ASK USER FOR NEW EMAIL
            email = self.email_entry.get()
            tkinter.messagebox.showinfo('Information', 'Thank you, ' + name + "'s email has been updated.")

            # UPDATE EMAIL IN THE KEY-VALUE PAIR IN NAME_AND_EMAIL DICTIONARY
            name_and_email[name] = email

        else:
            tkinter.messagebox.showinfo('Information', name + ' Was Not Found\nPlease select the "ADD" option to add ' + name + ' to the database.')

    # DELETE NAME AND EMAIL FROM DICTIONARY
    def delete(self, name_and_email):

        name = self.name_entry.get()

        if name in name_and_email:  # IF NAME EXIST IN DICTIONARY, DELETE KEY-VALUE PAIR
            del name_and_email[name]
            print(name + ' has been deleted.')
        else:
            print(name + ' Was Not Found')
            print('Looks like you don\'t need to delete ' + name + ' after all!')

    # SAVE DATA TO FILE AND EXIT PROGRAM
    def quit_and_save(self, name_and_email):
        print('bye')

        save_file = open('name_and_email.dat', 'wb')  # OPEN FILE AND ENABLE BINARY WRITING 'WB'
        pickle.dump(name_and_email, save_file)  # DUMP NEW DATA FROM DICTIONARY INTO FILE
        save_file.close()  # CLOSE FILE
        # self.main_window.quit


my_gui = NameAndAddress()
