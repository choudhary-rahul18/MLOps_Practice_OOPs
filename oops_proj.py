class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    
    def menu(self):
        user_input = int(input("Welcome to Chatbook!! How would you like to proceed?\n"\
                            "1. Press 1 to signup\n" \
                            "2. Press 2 to signin\n" \
                            "3. Press 3 to write a post\n" \
                            "4. Press 4 to message a friend\n" \
                            "5. Press any other key to exit \n"))
        
        if user_input == 1:
            self.signup()
        elif user_input ==2:
            self.signin()
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email here --> ")
        pwd = input("Setup your password here --> ")
        self.username = email
        self.password = pwd
        print("You have signup successfully !!\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please Signedup first by pressing 1 in the main menu\n")
        
        else:
            email = input("Enter your email here --> ")
            pwd = input("Setup your password here --> ")

            if self.username == email and self.password == pwd:
                print("Signin Suceesfully!!\n")
                self.loggedin = True
            else:
                print("Incorrect username or password\n")
        
        self.menu()


ram = Chatbook()
