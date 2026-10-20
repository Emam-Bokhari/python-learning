class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age 
        

class Info(Person):
    def __init__(self,first_name,last_name,age,post_code,address):
        super().__init__(first_name,last_name,age)
        self.post_code=post_code
        self.address=address
        

person_info=Info("Moshfiqur","Rahman",27,3460,"Brahmanbaria")


# inheritance types: single, multiple, multilevel, hierarchical, hybrid