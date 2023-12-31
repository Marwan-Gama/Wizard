from wizard import wizard
import re
class Phase:
    def __init__(self,number):
        self.num_phase=number
       
        self.validation_functions = {
        "Name": lambda x: len(x.split()) == 2 and all(len(name) >= 2 for name in x.split()),
        "Email": lambda x: len(x) > 0 and re.match(r"[^@]+@[^@]+\.[^@]+", x),
        "Birth Date": lambda x: len(x) > 0 and len(x.split('/')) == 3,
        "City": lambda x: len(x) > 0,
        "Street": lambda x: len(x) > 0,
        "Number": lambda x: x != 0 and x > 0,
        "Social Media": lambda x: re.compile(r'^(https?://)?(www\.)?(facebook|twitter|instagram|linkedin)\.com/.*$'),
        "Hobbies": lambda x: True  
        }
    

    def input_validation(self,string,func=0):
        while True:
            print(string)
            if func:
                input=input()
                if func(input):
                    return input
                else:
                    print("Invalid input. Please enter it again.")
            else:
                input=input()
                return input

            
    def run_phase(self,wizard):
        if self.num_phase==1:
            wizard.details["Name"]=self.input_validation('Enter your full name (minimum 2 characters each):\n',lambda x:len(x.split()) == 2 and (len(name) >= 2 for name in x.split()))
            wizard.details["Email"]=self.input_validation('Enter your email address:\n',lambda x:len(x)>0 and re.match(r"[^@]+@[^@]+\.[^@]+", x))
            wizard.details["birth_date"]=self.input_validation('Enter your birth date in format (dd/MM/yy):\n',lambda x:len(x)>0 and len(x.split('/'))==3)
        elif self.num_phase==2:
            wizard.details["City"]=self.input_validation('Enter your city\n',lambda x:len(x)>0)
            wizard.details["Street"]=self.input_validation('Enter your street\n',lambda x:len(x)>0)
            wizard.details["Number"]=self.input_validation('Enter your number\n',lambda x: x !=0 and x>0)
        else:
            wizard.details["Social Media"]=self.input_validation('Enter your social media (facebook, twitter, Instagram or linkedin)\n',lambda x:re.compile(r'^(https?://)?(www\.)?(facebook|twitter|instagram|linkedin)\.com/.*$'))
            wizard.details["Hobbies"]=self.input_validation('Enter your hobbies (Chess, Movies, Sport, Cars, Dolls)\n')

    def update(self,wizard):
        '''
        Update a field in the wizard's details based on user input.

        Args:wizard (Wizard): The wizard instance.

        Returns:None
        '''
        choice = input("What field do you want to change?")
        choice=choice.capitalize()

        # Check the current phase and update the corresponding fields
        if self.num_phase==1:
          self.update_phase_field(self, wizard, choice, ["Name","Email","birth_date"])
   
        if self.num_phase==2:
            self.update_phase_field(self, wizard, choice, ["City","Street","Number"])

        if self.num_phase==3:
            self.update_phase_field(self, wizard, choice, ["Social Media","Hobbies"])

    def update_phase_field(self, wizard, choice,phaze_attributes):
        '''Update a field in the wizard's details if it belongs to the specified phase.

        Args: wizard (Wizard): The wizard instance.
            choice (str): The field the user wants to update.
            phase_attributes (list): List of valid field names for the current phase.

        Returns:None
        '''
        if choice in phaze_attributes:
            wizard.details[choice] = self.input_validation(f'Enter your {choice}:\n', self.validation_functions[choice])
        else:
            print("Invalid field choice.")



    