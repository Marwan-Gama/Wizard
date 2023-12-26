import re
def get_user_info():
    while True:
        full_name = input("Enter your full name (minimum 2 characters each): ")
        if len(full_name.split()) == 2 and (len(name) >= 2 for name in full_name.split()):
            break
        else:
            print("Invalid input. Please enter both first and last name.")
    while True:
        email = input("Enter your email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        else:
            print("Invalid email address. Please enter a valid email.")
    while True:
        birth_date = input("Enter your birth date in format (dd/MM/yy): ")
        if len(birth_date.split('/'))==3:
            break
        else:
            print("Invalid date format. Please enter a valid date.")

    return full_name, email, birth_date


print("Phase 1:\n----------------\
       Enter your details")
name, email, birth_date = get_user_info()
