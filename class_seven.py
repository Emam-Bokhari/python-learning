# function

def say_hello():
    print("Hello World!")
    
say_hello()

# parameters, arguments
def addition(x,y):
    print(x+y)
    
addition(5,10)

# returning function
def add(x,y):
    return x+y 


result =add(2,3)
print(result)


# default parameter
def full_name(first_name="Emam",last_name="Bokhari"):
    print(f"{first_name} {last_name}")
    

full_name()

# *args
def summation(*args):
    total=0
    
    for num in args:
        total+=num
    
    return total 


print(summation(1,2,3,4,5,10))

# *args with another parameter
def customer_info(customer_name,*products):
    print(customer_name,products)
    

customer_info("Moshfiqur Rahman","Pencil","Pen","Tablet","iPhone")

# **kwargs
def customer_info(customer_name,**products):
    print(customer_name,products)
    

customer_info("Moshfiqur Rahman",product_name="macbook",product_price=89000)


