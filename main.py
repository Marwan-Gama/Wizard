#
import SplashScreen
from wizard import Wizard

def main():
    SplashScreen.mainloop()
    wizard = Wizard()
    wizard.start_wizard()

if __name__ == "__main__":
    main()


