
class Employee:
    # special method/magic method/ dunder method - constructor
    def __init__(self):
        print("Started Executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data has been executed\n")

    def travel(self, destination):
        print("This function is called mannually")
        print(f"Employe is now travelling to {destination}")



# Create an object/instance of the class Employee
sam = Employee()

#printing the attributes
print(sam.id)
#calling a method
sam.travel("Mumbai")