
#ask the user for how long they want their password to be
#ask what the types of their characters they want in their password
#minimum length of password is 4characters.
#maximum length os password is 8characters.

#for the input string, only string values are allowed. 


import random
import string

length= int(input("Enter the length of the password:"));

while (length<4 or length>8):
    print("The length of the password should be between 4 and 8 characters.");
    length= int(input("Enter the length of the password:"));

up_Letters=input("Uppercase letters? (yes or no):");
while( up_Letters.isnumeric() ):
    print("Please enter a string value.");
    up_Letters=input("Uppercase letters? (yes or no): ");

low_Letters=input("Lowercase letters? (yes or no): ");
while( low_Letters.isnumeric() ):
    print("Please enter a string value .");
    low_Letters=input("Lowercase letters? (yes or no): ");

numbers=input("Numbers? (yes or no): "); 
while( numbers.isnumeric() ):
    print("Please enter a string value .");
    numbers=input("Numbers? (yes or no): ");

symbols=input("Symbols? (yes or no): ");
while( symbols.isnumeric() ):
    print("Please enter a string value .");
    symbols=input("Symbols? (yes or no): ");


digits= string.digits;
lettersUpper= string.ascii_uppercase; #uppercase letters
lettersLower= string.ascii_lowercase; #lowercase letters
symbol= string.punctuation; 

print(lettersUpper);

password= "";

#a list of all the characters that the user wants in their password.
allCharacters= []; #it will be a list of all the character types that the user wants in their password.

if (up_Letters=="yes"):
    allCharacters+=list(lettersUpper); #add the uppercase letters to the list of all characters
if (low_Letters=="yes"):
    allCharacters+=list(lettersLower);
    
if (numbers=="yes"):
    allCharacters+=list(digits);
if (symbols=="yes"):
    allCharacters+=list(symbol);
    
print(allCharacters);


#build the password

for i in range(length): #we will loop through the character list <length> times.
    
    password+=random.choice(allCharacters);

    
print("Your password is: ", password); 


























# if (up_Letters=="yes" and low_Letters=="yes" and numbers=="yes" and symbols=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersUpper);
#         password+=random.choice(lettersLower);
#         password+=str(random.choice(numbers));
#         password+=random.choice(symbols);
# elif (up_Letters=="yes" and low_Letters=="yes" and numbers=="yes"):
#     for i in range(length):

#         password+=random.choice(lettersUpper);
#         password+=random.choice(lettersLower);
#         password+=str(random.choice(numbers));
# elif (up_Letters=="yes" and low_Letters=="yes" and symbols=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersUpper);
#         password+=random.choice(lettersLower);
#         password+=random.choice(symbols);
# elif (up_Letters=="yes" and numbers=="yes" and symbols=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersUpper);
#         password+=str(random.choice(numbers));
#         password+=random.choice(symbols);
# elif (low_Letters=="yes" and numbers=="yes" and symbols=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersLower);
#         password+=str(random.choice(numbers));
#         password+=random.choice(symbols);
# elif (up_Letters=="yes" and low_Letters=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersUpper);
#         password+=random.choice(lettersLower);
# elif (up_Letters=="yes" and numbers=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersUpper);
#         password+=str(random.choice(numbers));
# elif (up_Letters=="yes" and symbols=="yes"):
#     for i in range(length):

#         password+=random.choice(lettersUpper);
#         password+=random.choice(symbols);
# elif (low_Letters=="yes" and numbers=="yes"):
#     for i in range(length):

#         password+=random.choice(lettersLower);
#         password+=str(random.choice(numbers));
# elif (low_Letters=="yes" and symbols=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersLower);
#         password+=random.choice(symbols);
# elif (numbers=="yes" and symbols=="yes"):
#     for i in range(length):

#         password+=str(random.choice(numbers));
#         password+=random.choice(symbols);
# elif (up_Letters=="yes"):
#     for i in range(length):

#         password+=random.choice(lettersUpper);
# elif (low_Letters=="yes"):
#     for i in range(length):
#         password+=random.choice(lettersLower);
# elif (numbers=="yes"):
#     for i in range(length):
#         password+=str(random.choice(numbers));
# elif (symbols=="yes"):
#     for i in range(length):
    
#         password+=random.choice(symbols);
# else:
#     print("You did not choose any type of characters for your password");

# print("Your password is: ", password);
    



