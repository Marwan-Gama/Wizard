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
            "Hobbies": None,
            "Happy": None,  
            "Skydiving": None, 
            "One Dolar": None

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




# wizard = Wizard()
# wizard.start_wizard()

