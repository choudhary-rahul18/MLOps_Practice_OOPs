class Chatbook:

    __user_id = 1

    def __init__(self):
        self.id = Chatbook.__user_id
        Chatbook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    
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
            self.my_post()
        elif user_input == 4:
            self.sendmsg()
        else:
            exit()

    @staticmethod
    def get_id():           # getter
        return Chatbook.__user_id
    
    @staticmethod
    def set_id(val):       # setter
        Chatbook.__user_id = val

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

    def my_post(self):
        if self.loggedin == False:
            print("You need to signin first to post something.\n")
        else:
            message = input("Enter your message here --> ")
            print(f"Following content has been posted -> {message}\n")
        self.menu()

    
    def sendmsg(self):
        if self.loggedin == False:
            print("You need to signin first to post something.\n")
        else:
            txt = input("Enter your message here --> ")
            friend = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {friend}\n")
        self.menu()


