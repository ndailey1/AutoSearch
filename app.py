# IMPORTS

import csv
import time
from selenium import webdriver

# SET UP

with open("NewBritainData.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

# WEB AUTOMATION

#LOGIN PAGE

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://connecticut-townclerks-records.com/User/Login.aspx?bSesExp=True')

        time.sleep(1)

#INPUTTING LOGIN INFO - using "Sign-In As Guest" option for testing - below code is to sign into a profile.

        #username = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[1]/td[2]/input')
        #username.send_keys('chriscooper')

        #password = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[2]/td[2]/input')
        #password.send_keys('101Corporate')

        #time.sleep(1)

#CLICKING "LOGIN"
        #**change sign in xpath when not signing in as guest.

        sign_in_button = driver.find_element("xpath", '/html/body/form/div[4]/div[3]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[3]/td/input[2]')
        sign_in_button.click()

        #time.sleep(1)


#HOW TO GET TO NEW PAGE???

#Main menu - Needs to go to New Britain page.

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://connecticut-townclerks-records.com/User/protected/MessageCenter.aspx')

        time.sleep(1)

        new_britain_button = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[26]/a')
        new_britain_button.click()

        time.sleep(1)

#SEARCHER PAGE

        #volume = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div/center/div/table/tbody/tr[1]/td[3]/input')
        volume.sendkeys(line[5])

        #page = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div/center/div/table/tbody/tr[1]/td[5]/input')
        #page.sendkeys(line[6])



#LEFT - webdriver keeps shutting down before executing login click. How to add "if" and "then" commands? New script after the login is executed? New script for each page?
