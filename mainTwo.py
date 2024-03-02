#ask for the user their wieght in kilogroms
#ask  the user for their height in meters
#BMI= wegith/height(m)^2.
#categories are :underweight,normal, Overweight and obese.

#APPROACH:
    #1. I used the input() function to ask the user for their weight and height.
    #2. I used the float() function to convert the user's input to a floating point number.
    #3. I presented factors in parantheses to the user just in case they had a different measurement of weight and height
    #4. I used the if-elif-else statement to categorize the user's BMI into the four categories.
    #5. I used the format() function to format the BMI to two decimal places.
    #6. I used the print() function to display the user's BMI and category to the user.
    #7. I used a dictionary to store the categories and their conditions.




weight= float(input("Enter your weight in kilograms (1 lbs= 2.20462kg): "));
height= float (input("Enter your height in meters (1 foot = 30.48centimeters) and (1 centimeter= 0.01 meter): "));

BMI= weight/(height)**2;
print(BMI);

categories={
    "Underweight": BMI<18.5,
    "Normal": 18.5<=BMI<=24.9,
    "Overweight": 25<=BMI<=29.9,
    "Obese": BMI>=30
}

if(categories["Underweight"]):
    print("Your BMI is {:.2f} and you are Underweight".format(BMI));
elif(categories["Normal"]):
    print("Your BMI is {:.2f} and you are Normal".format(BMI));
elif(categories["Overweight"]):
    print("Your BMI is {:.2f} and you are Overweight".format(BMI));
elif(categories["Obese"]):
    print("Your BMI is {:.2f} and you are Obese".format(BMI));













# #separate the height into a whole number and a fractional part so that the conversion to meters is done.
        # whole_number=""
        # fractional_part=""
        # strHeight=height_entry.get();
        # for i in range(len(strHeight)):
        #     if strHeight[i]==".":
        #         #using string slicing to separate the whole number and the fractional part
        #         whole_number=strHeight[:i]; #everything before the decimal point
        #         fractional_part=strHeight[i:]; #everything after the decimal point
        #         break; #we break out the loop because we have found the decimal point

        # #convert the whole number to meters
        # whole_number=float(int(whole_number)*0.3048);
        # #convert the fractional part to meters
        # fractional_part=float(int(fractional_part)*0.0254);
        # #the fractional part could be empty because some people do not have a fractional part in their height.
        # if(fractional_part==""):
        #     height_entry.delete(0, END);
        #     height_entry.insert(0, whole_number);
        # else:
        #     height_entry.delete(0, END);
        #     height_entry.insert(0, str(whole_number+fractional_part));
        #     height_unit_entry.delete(0, END);
        #     height_unit_entry.insert(0, "meters");