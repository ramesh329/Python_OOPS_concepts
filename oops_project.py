class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""welcome to chatbook !! how would you like to proceed? 
                            1. Press 1 to signup
                            2. press 2 to signin
                            3. Press 3 to wrtie a post
                            4. Press 4 to message a friend
                            5. Press anyother key to exit 
                            """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        
    def signup(self):
        email = input("enter your email here ->")
        pwd = input("setup you password here ->")
        self.username = email
        self.password = pwd
        print("successfully signed in")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your eamil/username here ->")
            pwd = input ("Enter you password here ->")
            if self.username == uname and self.password == pwd:
                print('you have signed in successfully!')
                self.loggedin == True
            else:
                print("please input correct credentials")
            print("\n")
            self.menu()        

    


         


obj = chatbook()          
       

