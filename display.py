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

