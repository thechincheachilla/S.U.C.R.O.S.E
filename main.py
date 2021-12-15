from methods  import loadDriver, loadList, makePurchase

from selenium import webdriver  

from gpiozero import Button
from gpiozero import LED

# Make sure correct interpreter is selected

# TODO: Allow credentials and link to be read from a usb
#       Design enclosure 

def main():
    bigAssRedButton = True # for testing for now
    #= Button(4) cannot work unless rpi is connected
    BARBLED = None #LED(17)
    # BARBLED.on()
    purchase_list = loadList()

    test = 0 # remove later
    while test < 1 and 1:
        # Might need to debug this if spamming the button breaks stuff
        if bigAssRedButton: #.isPressed():
            # bigAssRedButton.wait_for_release()
            driver = loadDriver()
            if (driver == None):
                pass
                #BARBLED.blink(0, 4, 1, False)
            else:
                if makePurchase(driver, purchase_list, BARBLED) == True:
                    pass
                    #BARBLED.blink(0.25, 0.25, 20, False)
                else:
                    #BARBLED.blink(0, 4, 1, False)
                    pass
            test+=1 # remove later

if __name__ == "__main__":
    main()
