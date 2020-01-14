import speech_recognition as sr
import tkinter as tk




# This records the speech, interprets it
# and prints it on to the label/screen
# of the GUI.
def record_speech(bottom_button2, file):
    
    # This creates a file based on the
    # name the user inputed
    current_file = open(file[0], "w+")
    
    # Initialize recognizer.
    r = sr.Recognizer()

    # Uses Microphone as a source.
    with sr.Microphone() as source:
        
        # Adjusts for ambient noise. 
        r.adjust_for_ambient_noise(source)

    

        # records what the users says thoguh their mic. 
        # stores it in audio varialble.
        audio = r.listen(source)

        # convert audio into text with recognizer.
        try:
            label['text'] += "You have said : \n " + \
                r.recognize_google(audio) + "\n"
            current_file.write(label['text'])
        
        #throws exception if it can't interpret it.     
        except Exception as e:
            label['text'] = "Error : " + str(e)
            current_file.write(label['text'])


# This class is used to create a place holder for the
# entry. (entry) is the place where the user enters the file name.
# It gives them and example they can type over (placeholder) i.e test_file.txt        
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='#484747'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()



# Height and Weight of the window. 
HEIGHT = 700
WIDTH = 800



# This function is triggered via the setfile button.
# It sets a file name, where we save the text.
def set_file_name(file_name, r_file):
    r_file[0] = file_name


# This function clears the text on the GUI's screen.
def clear_text():
    label['text'] = ""



# Start of gui app
root = tk.Tk()
######################################


# This creates a canvas to which 
# adjusts the size of the window.
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
canvas.winfo_toplevel().title("Note Taking APP")


# This is is the background of the canvas 
background_label = tk.Label(root, bg='#0099ff')
background_label.place(relwidth=1, relheight=1)



# This creates a frame which acts as a header that says
# "TIME TO RECORD YOUR NOTES" 
upper_frame = tk.Frame(root, bg='#0099ff', bd=15)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.15, anchor='n')
upper_frame_label = tk.Label(upper_frame, bg='#0099ff', justify='center', text="TIME TO RECORD YOUR NOTES")
upper_frame_label.pack()
upper_frame_label.config(justify='center', font=("Courier", 34))



# This frame contains the label where 
# the interpreted speech will be listed. 
top_frame = tk.Frame(root, bg='#abc1ff', bd=15)
top_frame.place(relx=0.5, rely=0.20, relwidth=0.75,relheight=0.45, anchor='n')


#Label that is placed in the top frame.        
label = tk.Label(top_frame, anchor='nw', justify='left', bd=4)
label.config(font=("Courier", 20))
label.place(relwidth=1, relheight=1)


# The center_frame has the entry where the user 
# types the name of the file they want to save.
# and a button to set the file name.
center_frame = tk.Frame(root, bg='#abc1ff', bd=15)
center_frame.place(relx=0.5, rely=0.70, relwidth=0.75,relheight=0.1, anchor='n')

# This is the label that creates a background for the center frame 
# and add the text: "Name Your Save File:"
center_frame_label = tk.Label(center_frame, bg='#abc1ff', justify='center', text="Name Your Save File:")
center_frame_label.place(relwidth=0.30, relheight=1.2, rely=-0.1, relx=0)
center_frame_label.config(font=("Courier", 13))

# This creates a placeholder within the entry.
entry = EntryWithPlaceholder(center_frame, 'file_name.txt')
entry.place(relwidth=0.45, relheight=1.2, rely=-0.1, relx=0.33)
entry.config(font=("Courier", 16))

# This array stores the file name as a string at index 0.
file = [0]

# This button sets the file name using the set_file_name function.
center_button = tk.Button(center_frame, text="SET FILE",bg='#abc1ff', command=lambda: set_file_name(entry.get(), file))
center_button.place(relwidth=0.20, relheight=1.2, rely=-0.1, relx=0.8)



# Creates frame below the center_frame.
bottom_frame = tk.Frame(root, bg='#abc1ff', bd=15)
bottom_frame.place(relx=0.5, rely=0.85, relwidth=0.75,relheight=0.1, anchor='n')

#Button which clears the text off the screen, is placed in the bottom_frame.
bottom_button1 = tk.Button(bottom_frame, text="CLEAR TEXT",bg='#abc1ff', command=lambda: clear_text())
bottom_button1.place(relwidth=0.20, relheight=1.2, rely=-0.1, relx=0)

#Button which records the speech, is placed in the bottom_frame.
bottom_button2 = tk.Button(bottom_frame, text="SPEAK",command=lambda: record_speech(bottom_button2, file))
bottom_button2.place(relwidth=0.20, relheight=1.2, rely=-0.1, relx=0.8)



########################################
root.mainloop()
# End of gui app
