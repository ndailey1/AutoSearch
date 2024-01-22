# IMPORTS

import csv
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import socket

# SET UP - using a CSV file created from excel sheet. Ideally would like to have the data pulled/returned directly to/from the excel sheet.

with open("NewBritainVolPage.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

# WEB AUTOMATION

# LOGIN PAGE

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://connecticut-townclerks-records.com/User/Login.aspx?bSesExp=True')

        time.sleep(3)

    # INPUTTING LOGIN INFO - using "Sign-In As Guest" option for testing - below code is to sign into a profile.

        #username = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[1]/td[2]/input')
        #username.send_keys('USERNAME')

        #password = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/span[1]/div/div[2]/table/tbody/tr[2]/td[2]/input')
        #password.send_keys('PASSWORD')

        #time.sleep(1)

    # Change sign in xpath when not signing in as guest.

        sign_in_button = driver.find_element("xpath", '//*[@id="ctl00_cphMain_blkLogin_btnGuestLogin"]')
            #**change sign in xpath when not signing in as guest.
        sign_in_button.click()

        time.sleep(3)

#Main menu - direct to town here


        new_britain_button = driver.find_element("xpath", '/html/body/form/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[26]/a')
        new_britain_button.click()

        time.sleep(2)

#To volume and page search
        vol_page_search = driver.find_element("xpath", '//*[@id="ctl00_NavMenuIdxRec_btnNav_IdxRec_BookPage"]')
        vol_page_search.click()

        time.sleep(2)

# Running the search with CSV data and bringing to results page

        volume = driver.find_element("xpath", '//*[@id="ctl00_cphMain_txtBookNumber"]')
        volume.send_keys(line[0])

        page = driver.find_element("xpath", '//*[@id="ctl00_cphMain_txtPageNumber"]')
        page.send_keys(line[2])

        time.sleep(1)

        search_button = driver.find_element("xpath", '//*[@id="ctl00_cphMain_btnSearch"]')
        search_button.click()

        time.sleep(5)

#Need to add conditions defining the correct release to:
    #Extract the correct Vol/Page into excel or csv
    #Click on the correct image link
        #Can the tr/td variables in the xpath change conditionally?

#Trying to make conditions - only if the page has the word "release". Need to figure out how to reference the new URL for the current page.

# Get the script's current URL


# Clicking into the image of the release
        release_image = driver.find_element("xpath", '//*[@id="ctl00_cphMain_lrrgResults_cgvResults"]/tbody/tr[2]/td[14]/a')
        release_image.click()

        time.sleep(5)

# Adding document to cart
        add_to_cart = driver.find_element("xpath", '//*[@id="ctl00_cphMain_lbAddDocToCart"]')
        add_to_cart.click()

        time.sleep(5)
