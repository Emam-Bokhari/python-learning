# if,else,elif, inner if, ternary operator

# if,else

age=6

if(age<35):
    print("Eligible")
else:
    print("Not Eligible")


food_name="Mango"

user_input=input("Enter your food name here: ")

if(food_name==user_input):
    print("Correct")
else:
    print("InCorrect")

# elif

if(food_name==user_input):
    print("Correct")
elif(age>18 and age<45):
    print("Your are eligible")
else:
    print("You are not eligible")

# inner if
email = "user@gmail.com"
password = "123456"

if(email=="user@gmail.com"):
    print("Email is correct")
    
    if(password=="123456"):
        print("Password is correct")
    else:
        print("Password is incorrect")
else:
    print("Your e-mail is not exist's in our database")

# ternary operator
result="Adult" if age>=18 else "Children"
print(result)