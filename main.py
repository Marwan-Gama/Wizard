#
import SplashScreen
from wizard import Wizard
from phase import Phase

def main():
    SplashScreen.mainloop()
    wizard = Wizard()
    wizard.start_wizard()
  
  
if __name__ == "__main__":
    main()


