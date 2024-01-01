# Wizard Application
import re
class Wizard:
    def __init__(self):
        self.details = {
            "Name": None,
            "Email": None,
            "birth_date": None,
            "City": None,
            "Street": None,
            "Number": None,
            "Social Media": None,
            "Hobbies": None
        }
        self.completed_phases = []
    def start_wizard(self):
        print("Welcome to the Wizard!")
        while True:
            choice = input("Menu: 1) Start New 2) Continue: ")
            if choice == "1":
                self.run_phase_1()
            elif choice == "2":
                phase = int(input("Enter phase number: "))
                if phase in self.completed_phases:
                    self.show_phase(phase)
                else:
                    if phase==self.completed_phases[len(self.completed_phases)-1]+1:
                        self.run_phase(phase)
                    print("You can't access this phase yet. Please complete previous phases.")
            else:
                print("Invalid choice!")

    def get_user_name(self):
        while True:
            full_name = input("Enter your full name (minimum 2 characters each): ")
            if len(full_name.split()) == 2 and (len(name) >= 2 for name in full_name.split()):
                self.details["Name"]=full_name
                return full_name
            else:
                print("Invalid input. Please enter both first and last name.")
    def get_email(self):
        while True:
            email = input("Enter your email address: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.details["Email"]=email
                return email
            else:
                print("Invalid email address. Please enter a valid email.")
    def get_birth_date(self):
        while True:
            birth_date = input("Enter your birth date in format (dd/MM/yy): ")
            if len(birth_date.split('/'))==3:
                self.details["birth_date"]=birth_date
                return birth_date
            else:
                print("Invalid date format. Please enter a valid date.")

    def run_phase_1(self):
        print("Phase 1:\n----------------")
        full_name=self.get_user_name()
        birth_date=self.get_birth_date()
        email=self.get_email()
        self.completed_phases.append(1)

        x=input("next or previous !.")
        if x=="next":
            if 2 in self.completed_phases:
                self.show_phase(2)
            else:
                self.run_phase_2
        else:
            self.show_phase(1)
        return full_name, email, birth_date

    def show_phase(self,i):#i index for phase
        if i==1:
            print("full name",":",self.details["Name"]) 
            print("Email",":",self.details["Email"]) 
            print("Birth Date",":",self.details["birth_date"]) 

            x=input("for update input the number of kjwdwjdnwejkd ")
            if x==1 or x==2 or x==3:
                set(x)
            else:
                if 2 not in self.completed_phases:
                    self.run_phase_2()
                else:
                    self.show_phase(2)
        

    def run_phase(self, phase):
        if phase == 1:
            self.run_phase_1()
        elif phase == 2:
            pass # self.run_phase_2()
        elif phase == 3:
            pass # self.run_phase_3()



    def display(self):
        print("\nSummary:")
        for key, value in self.details.items():
            print(f"{key}: {value}")
        print("\n")

# wizard = Wizard()
# wizard.start_wizard()

