
#NAME: ANNE DEBORA NIYONKURU

#APPROACH:
    #1. Because people come from different environments and  therefore might use different units for different measurements, 
            #.........I  provided a way to convert the units to the standard units that the BMI formula uses (kg and meters).
    #2. I used a dictionary to store the categories of BMI and their corresponding ranges.
    #3. I used a function to calculate the BMI and display the result in a label.
    #4. I used a button to calculate the BMI.
    #5. I used a button to convert the weight to kilograms if it is not already in kilograms.
    #6. I used a button to convert the height to meters if it is not already in meters.
    #7. I used a label to display the heading of the application.
    #8. I used labels to display the input fields.
    #9. I used entry fields to get the input from the user.


from tkinter import *
import sqlite3



root=Tk();

root.title("BMI Calculator");
root.configure(background='light green');
root.geometry("500x300");

#styles
font_style = ("Helvetica", 12)
padding = 10
button_style = {"background": "#4CAF50", "foreground": "black", "font": font_style}
entry_style = {"background": "white", "foreground": "black", "font": font_style}
result_label_style = {"background": "#2196F3", "foreground": "white", "font": font_style}


heading = Label(root, text="BMI Calculator", bg="light green", font=font_style)
heading.grid(row=0, column=1, columnspan=4, padx=padding, pady=padding)

weight=Label(root, text="Enter your weight:", font=font_style);
weight_unit=Label(root, text="Unit (lbs or kg):", font=font_style);
height=Label(root, text="Enter your height:", font=font_style);
height_unit=Label(root, text="Unit(centimeters, meters or feet and inches):", font=font_style);

# heading.grid(row=0, column=1);
weight.grid(row=1, column=0, padx=padding, pady=padding)
weight_unit.grid(row=1, column=2, padx=padding, pady=padding)
height.grid(row=2, column=0, padx=padding, pady=padding)
height_unit.grid(row=2, column=2, padx=padding, pady=padding)

weight_entry=Entry(root, validate="key", font=font_style);
weight_unit_entry=Entry(root, validate="key", font=font_style);
height_entry=Entry(root, validate="key", font=font_style);
height_unit_entry=Entry(root, validate="key", font=font_style);

weight_entry.grid(row=1, column=1, padx=padding, pady=padding)
weight_unit_entry.grid(row=1, column=3, padx=padding, pady=padding)
height_entry.grid(row=2, column=1, padx=padding, pady=padding)
height_unit_entry.grid(row=2, column=3, padx=padding, pady=padding)

def convert_to_kg():
    get_weight=float(weight_entry.get());
    get_unit=weight_unit_entry.get();
    if get_unit=="lbs" or get_unit=="Lbs" or get_unit=="pounds" or get_unit=="Pounds":
        weight_entry.delete(0, END); # remove the previous entry from the input box
        weight_entry.insert(0, get_weight*0.453592);
        weight_unit_entry.delete(0, END);
        weight_unit_entry.insert(0, "Kg");
    else: #if the weight is already in kilograms, we do nothing
        pass

toKg_button=Button(root, text="Click to convert to Kg if your weight is not in kilograms.", command=convert_to_kg, **button_style);
toKg_button.grid(row=1, column=4, padx=padding, pady=padding);

def convert_to_meters():
    get_height=float(height_entry.get());
    get_unit=height_unit_entry.get();

    if get_unit=="centimeters" or get_unit=="cm":
        height_entry.delete(0, END);
        height_entry.insert(0, get_height*0.01);
    
        height_unit_entry.delete(0, END);
        height_unit_entry.insert(0, "meters");
    

    elif get_unit=="feet and inches":

        #separate the height into a whole number and a fractional part so that the conversion to meters is done.
        parts = str(get_height).split('.') #we split the number into parts when we encounter a '.' .

        whole_number = int(parts[0]) if len(parts) > 0 else 0
        fractional_part = int(parts[1]) if len(parts) > 1 else 0 #if there is a decimal point in the entered height , then the length of parts is 2 . The first element will be a whole number and the second will be a fractional part.

        #convert to foot: 1foot=12inches
        foot_fractional=fractional_part//12;
        total_foot=whole_number+foot_fractional; #add the whole number and the fractional part to get the total foot

        #convert feet to meters: 1ft=0.3048m
        foot_to_meters=total_foot*0.3048;

        # Update the height entry with the total meters
        height_entry.delete(0, END)
        height_entry.insert(0, str(foot_to_meters))
        height_unit_entry.delete(0, END)
        height_unit_entry.insert(0, "meters")

    else:
        pass

toMeters_button=Button(root, text="Click to convert to meters if your height isn't in one.", command=convert_to_meters, **button_style);
toMeters_button.grid(row=2, column=4, padx=padding, pady=padding);

#calculate BMI
def find_BMI():

    get_weight=float(weight_entry.get());
    get_height=float(height_entry.get());

    BMI= get_weight/(get_height)**2;
    
    categories={
        "Underweight": BMI<18.5,
        "Normal": 18.5<=BMI<=24.9,
        "Overweight": 25<=BMI<=29.9,
        "Obese": BMI>=30
    }

    if(categories["Underweight"]):
        result_label=Label(root, text="Your BMI is {:.2f} and you are Underweight".format(BMI), **result_label_style);
        # print("Your BMI is {:.2f} and you are Underweight".format(BMI));
    elif(categories["Normal"]):
        result_label=Label(root, text="Your BMI is {:.2f} and you are Normal".format(BMI), **result_label_style);

        # print("Your BMI is {:.2f} and you are Normal".format(BMI));
    elif(categories["Overweight"]):
        result_label=Label(root, text="Your BMI is {:.2f} and you are Overweight".format(BMI), **result_label_style);

        # print("Your BMI is {:.2f} and you are Overweight".format(BMI));
    elif(categories["Obese"]):
        result_label=Label(root, text="Your BMI is {:.2f} and you are Obese".format(BMI), **result_label_style);

        # print("Your BMI is {:.2f} and you are Obese".format(BMI));

    result_label.grid(row=4, column=0, columnspan=4, padx=padding, pady=padding)
    # insert_user(weight,weight_unit, height,height_unit, BMI);
    
myButton = Button(root, text="Calculate", command=find_BMI, **button_style);
myButton.grid(row=3, column=3, padx=padding, pady=padding);


# cose_button= Button(root, text="Close", command= close);
# cose_button.grid(row=3, column=3);







root.mainloop();

































#connect to the database
# conn=sqlite3.connect('BMI.db');
# cursor= conn.cursor(); #create a cursor object to interact with the database. A cursor object is used to traverse the records from the result set.

# #Create a table
# cursor.execute("""CREATE TABLE IF NOT EXISTS BMI(
#     weight REAL,
#     weight_unit TEXT,
#     height REAL,
#     height_unit TEXT,
#     BMI REAL
# )""");
# print("Table created successfully");

# #insert into the table
# def insert_user (weight,weight_unit, height,height_unit, BMI):
#     cursor.execute("INSERT INTO BMI VALUES(?,?,?,?,?)", (weight,weight_unit, height, height_unit, BMI) );
#     conn.commit();
#     print("Record inserted successfully");

# def update_user (weight,weight_unit, height,height_unit, BMI):
#     cursor.execute("UPDATE BMI SET weight=?, height=?, BMI=?", (weight,weight_unit, height, height_unit, BMI));
#     conn.commit();
#     print("Record updated successfully");

# def close():
#     conn.close();
#     print("Connection closed successfully");