
#NAME: ANNE DEBORA NIYONKURU

#APPROACH:
    #1. I used a function to validate the length of the password entered by the user.
    #2. I used a Listbox widget to allow the user to select multiple character types for their password.
    #3. I used a function to get the selected character types from the Listbox widget.
    #4. I used a function to generate the password using the length and character types selected by the user.
    #5. I used a function to copy the generated password to the clipboard.
    #6 . I restricted the user from entering a length that is not a number or a length that is not between 4 and 12 characters.


from tkinter import *
from tkinter import Message
import random
import string

root=Tk();

#widgets are added here
root.title("Random Password Generator");
root.geometry("400x300")
root.configure(bg="#f0f0f0")

def validate_length(size):

    if size == "": 
        return True;
    elif not size.isdigit():
        message_label.config(text="Please enter a number.", fg="purple");
        return False;
    else:

        if int(size) >= 4 and int(size) <= 12:
            message_label.config(text="Valid length", fg="green");
            return True;
        else:
            message_label.config(text="The length of the password should be between 4 and 12 characters.", fg="red");
            return False;
   

input1=Label(root, text="Enter the length of your password:", bg="#f0f0f0");
input2=Label(root, text="Choose your character types:");

input1.grid(row=0, padx=10, pady=10);
input2.grid(row=1);

#Register the function with the tkinter window manager
validate_length_command= root.register(validate_length);

e1=Entry(root, validate="key", validatecommand=(validate_length_command,"%P")); #input box that will validate the length

#place the input boxes next to the questions asked above
e1.grid(row=0, column=1, padx=10, pady=10);

message_label=Label(root, text="", fg="lightgrey", font=("Arial", 10, "italic"), bg="#f0f0f0");
message_label.grid(row=0, column=2, padx=10, pady=10);

characterSet=["Uppercase", "Lowercase", "Numbers", "Symbols"];
char_list=Listbox(root, selectmode=MULTIPLE,width=
             18, height=4, bg="grey");
for set in characterSet:
    char_list.insert(END, set);
char_list.grid(row=1, column=1, padx=10, pady=10);


def set_selected():
    selected= [char_list.get(i) for i in char_list.curselection()];
    print("The character types selected are : " ,selected);

    if(selected==[]): #if the user does not select any character type, then the default will be all the characters.
        selected=characterSet;
    return selected;


def randomPassword():

    #i want to get() the length of the password.
    #i want to collect the characters that the user wants in their passowrd
    length=e1.get();
    password_char_set= set_selected();
    
    char_set={
        "Uppercase": string.ascii_uppercase,
        "Lowercase": string.ascii_lowercase,
        "Numbers": string.digits,
        "Symbols": string.punctuation
        
    }

    pass_chars=[]; # alist of all characters to randomly select from to form the password

    for charType in password_char_set:
        for char in char_set[charType]:
            pass_chars.append(char);
    

    password="";
    for i in range(int(length)):
        password+= random.choice(pass_chars);

    print("The password is: ",password);
    
    #display the password in a label
    password_label=Label(root, text="Your password is: "+password, font=("Arial", 12), bg="#f0f0f0");
    password_label.grid(row=3, columnspan=3, padx=10, pady=10)

    return password;

    

    
# once i click on the button generate, i need to get() all the entries and form a password with them
myButton= Button(root, text="Generate", command= randomPassword, bg="#4CAF50", fg="grey" );
myButton.grid(row=2, column=1, pady=10)


def copy():

    mot_de_pass=randomPassword();
    root.clipboard_clear();
    root.clipboard_append(mot_de_pass);

    print("Password copied to clipboard");
    # Message.showinfo("Success", "Password copied to clipboard")

copy_button= Button(root, text="Copy to Clipboard", command= copy, bg="#008CBA", fg="grey");
copy_button.grid(row=2, column=2, pady=10)
    
root.mainloop(); #an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
















#the Listbox widget along with the selectmode attribute allows multiple items to be selected .
#the function set_selected() is triggered when the button is clicked on. This will retrieve all the selected items from the List .

#Real-time validation of the length of the password field:
   #The <validate> option is used to specify when the validation should occur.
   # When you set up the <validatecommand> option for the Entry widget, you need to provide a tuple where the first element is the registered function (as a string) 
      #....and the second element is the argument to pass to the function. 
    #.....In this case, '%P' is the argument that represents the current value of the Entry widget.
