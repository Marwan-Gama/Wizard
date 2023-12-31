from colorama import Fore, Style
from tabulate import tabulate


def display_summary(details):
    summary_table = [
        [Fore.CYAN + Style.BRIGHT + "Phase 1", Fore.CYAN + Style.BRIGHT + "Phase 2",
         Fore.CYAN + Style.BRIGHT + "Phase 3"],
        [f"{Fore.YELLOW}Full Name{Style.RESET_ALL} - {details['Name']}",
         f"{Fore.YELLOW}City{Style.RESET_ALL} - {details['City']}",
         f"{Fore.YELLOW}Social Media{Style.RESET_ALL} - {details['Social Media']}"],
        [f"{Fore.YELLOW}Email{Style.RESET_ALL} - {details['Email']}",
         f"{Fore.YELLOW}Street{Style.RESET_ALL} - {details['Street']}",
         f"{Fore.YELLOW}Hobbies{Style.RESET_ALL} - {', '.join(details['Hobbies']) if details['Hobbies'] else '-'}"],
        [f"{Fore.YELLOW}Birth Date{Style.RESET_ALL} - {details['birth_date']}",
         f"{Fore.YELLOW}Number{Style.RESET_ALL} - {details['Number'] if details['Number'] else '-'}",
         ""]
    ]

    print("\n" + Fore.CYAN + "Summary:" + Style.RESET_ALL)
    print(tabulate(summary_table, headers="firstrow", tablefmt="pretty"))
    print("\n" + Fore.MAGENTA + Style.BRIGHT + "Thank you for registering!" + Style.RESET_ALL)



def show_phase(num_phase,details):
    phase_functions = {
        1: lambda: print_items(1,details, 0, 3),
        2: lambda: print_items(2,details, 3, 6),
        3: lambda: print_items(3,details, 6, 8)
    }
    phase_functions.get(num_phase, lambda: print("Invalid phase number"))()


def print_items(num_phase,details, start, end):
    print(f'{Fore.GREEN}Phase {num_phase} items:\n')
    for key, value in list(details.items())[start:end]:
        print(f'{Fore.BLUE}{key}:{Fore.GREEN} {value}{Style.RESET_ALL}')
