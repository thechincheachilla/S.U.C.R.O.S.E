from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

import random
import time  

def loadDriver():
    tries = 0
    while (tries < 5):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options)  
            driver.implicitly_wait(2)
            break
        except:
            tries+=1
    if tries >= 5:
        print("Internet connection failure")
        return None
    return driver
    

def login(driver):    
    try:
        # Credentials format: username,password
        credentials = open("Credentials.txt", "r").readline().split(",") 
        #credentials = open("E:\Credentials.txt", "r").readline().split(",") 
        user = credentials[0]
        for char in user:
            driver.find_element_by_id("ap_email").send_keys(char)
            time.sleep(random.uniform(0.02, 0.2))
        time.sleep(2)
        driver.find_element_by_id("continue").click()
        time.sleep(2)
        password = credentials[1]
        for char in password:
            driver.find_element_by_id("ap_password").send_keys(char)
            time.sleep(random.uniform(0.02, 0.2))
        time.sleep(2)
        driver.find_element_by_id("signInSubmit").click()
        time.sleep(2)
        return True
    except:
        print("Error logging in")
        return False


def loadList():
    purchaseFile = open("Items.txt", 'r')
    #purchaseFile = open("E:\Items.txt", 'r')
    purchaseList = []
    for line in purchaseFile:
        purchaseList.append(line)
    purchaseFile.close()
    return purchaseList 

def makePurchase(driver, purchase_list, BARBLED):
    tries = 0
    # Try to make a purchase a max of 5 times, if fails, terminate
    while(tries < 5):
        try:    
            # Purchase a random loaded item (check subscription status)
            time.sleep(2)
            driver.get(random.choice(purchase_list))  
            noSubscription = False
            try:
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[text()[contains(., 'One-time purchase:')]]").click()
            except:
                print("\tNo subscription for this item")
            try:
                time.sleep(0.5)
                driver.find_element_by_name("submit.add-to-cart").click()
                time.sleep(0.5)
                driver.find_element_by_id("hlb-ptc-btn-native").click()
                time.sleep(0.5)
                login(driver)
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@id='orderSummaryPrimaryActionBtn']/span/input").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='orderSummaryPrimaryActionBtn']/span/input").click()
                time.sleep(2)
                driver.find_element_by_name("placeYourOrder1").click()
                time.sleep(0.5)
                try:
                    driver.find_element_by_name("placeYourOrder1").click()
                except:
                    print("No second place order button")
                print("Purchase Successful in " + str(tries+1) + " try/tries")  
                time.sleep(0.5)
                break
            except:
                tries+=1
                #BARBLED.blink(0.5, 0.5, 4, False)
                print("Purchase failed: looping again, tries = " + str(tries))
                driver.close()
                driver = loadDriver()
                if driver == None:
                    tries = 5
                    print("Driver connection failed")
                    break
                time.sleep(0.5)
        except:
            print("Failed to load purchase link")

    # Alert user if all tries failed
    if tries >= 5:
        if driver != None:
            print("Purchase failure, tries exhausted")
            driver.close()
        return False
    driver.close()
    return True

