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

#INPUTTING LOGIN INFO - using "Sign-In As Guest" rather than signing in just for testing.

        #username = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[1]/td[2]/input')
        #username.send_keys('chriscooper')

        #password = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[2]/td[2]/input')
        #password.send_keys('101Corporate')

        #time.sleep(1)

#CLICKING "LOGIN"
    #**change xpath when not signing in as guest.

        sign_in_button = driver.find_element("xpath", '/html/body/form/div[4]/div[3]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[3]/td/input[2]')
        sign_in_button.click()

        #time.sleep(1)

#Needs to go to New Britain page, then search by vol/page


#SEARCHER PAGE

        #volume = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div/center/div/table/tbody/tr[1]/td[3]/input')
        #volume.sendkeys(line[5])

        #page = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div/center/div/table/tbody/tr[1]/td[5]/input')
        #page.sendkeys(line[6])


