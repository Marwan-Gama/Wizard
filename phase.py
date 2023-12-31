from wizard import wizard
import re
class Phase:
    def __init__(self,number):
        self.num_phase=number

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


