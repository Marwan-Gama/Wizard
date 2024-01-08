from phase import Phase
from operator import itemgetter
import display

class Wizard:
    def __init__(self):
        self.details = {
            "Name": None,
            "Email": None,
            "Birth Date": None,
            "City": None,
            "Street": None,
            "Number": None,
            "Social Media": None,
            "Hobbies": None,
            "Happy": None,  
            "Skydiving": None, 
            "One Dollar": None

        }
        self.users = []
        self.phases = []


    def check_if_update(self,phase):
        if_update = input("Do you want to update something? Type 'Y' for Yes or 'N' for No: ")
        if if_update.upper() == 'Y':
            print("You chose to update something.")
            phase.update(self)
            display.show_phase(phase.num_phase, self.details)
        elif if_update.upper() == 'N':
            print("You chose not to update anything.")



    def create_phase(self,num_phase):
        print(f"You in Phase {num_phase}")
        phase = Phase(num_phase)
        phase.run_phase(self)
        display.show_phase(phase.num_phase, self.details)
        self.phases.append(phase)
        self.check_if_update(phase)
        if num_phase == 4: 
            self.users.append(self.details.copy())
            print("Details added to users list.")


    def prev_or_next(self,num_phase):
        while True:
            move = input(f"You in Phase {num_phase} ,Type (1) for Next  / (2) for Prev : ")
            if move == "1":
                if num_phase == 1:
                    num_phase += 1
                    self.create_phase(num_phase)
                if num_phase == 2:
                    num_phase += 1
                    self.create_phase(num_phase)
                if num_phase == 3:
                    self.create_phase(num_phase + 1)
                    return 'done'
            elif move == "2":
                if num_phase == 1:
                    print('You in Phase 1, You cant prev')
                    display.show_phase(num_phase , self.details)
                    self.check_if_update(self.phases[num_phase-1])
                elif num_phase == 2:
                    num_phase -= 1
                    print('You in Phase 1')
                    display.show_phase(num_phase, self.details)
                    self.check_if_update(self.phases[num_phase-1])
                elif num_phase == 3:
                    num_phase -= 1
                    print('You in Phase 2')
                    display.show_phase(num_phase , self.details)
                    self.check_if_update(self.phases[num_phase-1])
                elif num_phase == 4:
                   print('You in Phase 3')
                   display.show_phase(num_phase -1 , self.details)
                   self.check_if_update(self.phases[num_phase-2])
            else:
                print("Invalid choice. Please enter '1' to continue Next or '2' to Prev.")

    def display_history(self):
        print("| {:<20} | {:<15} | {:<15} | {:<10} |".format("Name", "City", "Social", "Is Happy"))
        print("-" * 70)
        for user_details in self.users:
            print("| {:<20} | {:<15} | {:<15} | {:<10} |".format(
                user_details["Name"] if user_details["Name"] else "",
                user_details["City"] if user_details["City"] else "",
                user_details["Social Media"] if user_details["Social Media"] else "",
                user_details["Happy"] if user_details["Happy"] else ""
            ))
        print("-" * 70)


    def start_wizard(self):
        print("Welcome to the Wizard!")
        while True:
            choice = input("Menu: 1) Start New 2) Continue 3) History: ")
            if choice == "1":
                self.create_phase(1)
                if_done = self.prev_or_next(1)
                if if_done == 'done':
                    display.display_summary(self.details)
                    if display.get_rest():
                        self.phases = []

            elif choice == "2":
                phase_number = int(input("Enter phase number: "))
                phase_numbers = [phase.num_phase for phase in self.phases]
                if phase_number in phase_numbers:
                    self.show_phase(phase_number, self.details)
                elif phase_number == len(self.phases) + 1:
                    self.create_phase(phase_number)
                else:
                    print("You can't access this phase yet. Please complete previous phases.")

            elif choice == "3":
                self.display_history()
                sub_choice = input("Sub-menu: 1) Sort by Name 2) Sort by City 3) Sort by Social 4) Sort by Is Happy 5) Back to Main Menu: ")
                if sub_choice == "1":
                    self.users.sort(key=lambda x: x.get("Name", ""))
                    self.display_history()
                elif sub_choice == "2":
                    self.users.sort(key=lambda x: x.get("City", ""))
                    self.display_history()
                elif sub_choice == "3":
                    self.users.sort(key=lambda x: x.get("Social Media", ""))
                    self.display_history()
                elif sub_choice == "4":
                    self.users.sort(key=lambda x: x.get("Happy", ""))
                    self.display_history()
                elif sub_choice == "5":
                    continue
                else:
                    print("Invalid choice in sub-menu!")


            else:
                print("Invalid choice!")
