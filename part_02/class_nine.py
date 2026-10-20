# without zip function 
names = ["Abdur Rahim", "Abdul Karim", "Sakib"]
marks = [80, 90, 75]

print(names[0],marks[0])
print(names[1],marks[1])
print(names[2],marks[2])

# zip function
result=zip(names,marks)
print(list(result))