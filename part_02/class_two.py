# letter grade programme
# Marks	Grade
# 80–100	A+
# 70–79	A
# 60–69	B
# 50–59	C
# 40–49	D
# 0–39	F





marks=int(input("Enter Your Mark: "))

if(marks>=80 and marks<=100):
    print("A+")
elif(marks>=70 and marks<=79):
    print("A")
elif(marks>=60 and marks<=69):
    print("B")
elif(marks>=50 and marks<=59):
    print("C")
elif(marks>=40 and marks<=49):
    print("D")
elif(marks>=0 and marks<=39):
    print("F")
else:
    print("Marks is not a valid number")