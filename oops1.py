
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



from oops_proj import Chatbook

user1 = Chatbook()
print(user1.id)

user2 = Chatbook()
user2.set_id(10)
print(user2.id)

user3= Chatbook()
print(user3.id)
# user2 = Chatbook()
# print(user2.id)