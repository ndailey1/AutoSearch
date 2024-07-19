# RANDOM AND NECESSARY IMPORTS

import csv
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from urllib.parse import urlparse
from lxml.html import fromstring
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#SET UP - this will be the CSV file used to populate data into the search form, and the Pandas df that will extract the data to a new CSV.

df = pd.DataFrame(columns=["Volume", "Page", "Date Filed"])

with open("Data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

#WEB AUTOMATION

#LOGIN PAGE

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://recordhub.cottsystems.com/****TOWN****CT/Search/') #MAKE SURE TO CHANGE THIS LINK TO THE RIGHT TOWN

        time.sleep(1)


    #INPUTTING LOGIN INFO - below code is to sign into a profile. The loop needs to login each time it runs which needs to be fixed.

        email = driver.find_element("xpath", '//*[@id="UserName"]')
        email.send_keys('USERNAME')

        password = driver.find_element("xpath", '//*[@id="Password"]')
        password.send_keys('PASS!')

        time.sleep(1)

        login = driver.find_element("xpath", '//*[@id="submit"]')
        login.click()

        time.sleep(1)

 #Select the Book/Page search
        search_drop_down = driver.find_element("xpath", '//*[@id="btnSearchType"]')
        search_drop_down.click()

        time.sleep(1)

        book_page = driver.find_element("xpath", '//*[@id="Type"]/ul/li[4]/a')
        book_page.click()

        time.sleep(1)

# Running the search using line in Data.csv and bringing to results page

        volume = driver.find_element("xpath", '//*[@id="Book"]')
        volume.send_keys(line[0])

        page = driver.find_element("xpath", '//*[@id="Page"]')
        page.send_keys(line[1])

        time.sleep(1)

        search_button = driver.find_element("xpath", '//*[@id="search-btn"]')
        search_button.click()

        time.sleep(3)



# to be added:
# IF MULTIPLE RESULTS, SELECT THE CORRECT MORTGAGE BY ITS VOL/PG NUMBER
# IF NO RELATED DOCS, PRINT "NO MORTGAGE FOUND" ON CSV INSTEAD OF ERROR
# IF RELATED DOCS BUT NO RELEASE, PRINT "NO RELEASE FOUND" ON CSV INSTEAD OF ERROR






#Click into related documents of mortgage - this is only if there is 1 mortgage listed**:
        related_documents = driver.find_element("xpath", '//*[@id="search-results-table"]/tbody/tr[1]/td[3]/a[3]')
        related_documents.click()

        time.sleep(1)


# Check if the related document is a release and pull VOL,PG,DATE using CSS slector then extract into pd df:
        child_elements = driver.find_elements(By.CSS_SELECTOR, 'td[class="childData"]')
        for child_element in child_elements:
            date_filed_data = ''
            volume_data = ''
            page_data = ''

            if 'REL' in child_element.text:
              date_filed_data = child_element.text.split('Filed:')[1].split(' ')[1]
              volume_data = child_element.text.split('Volume:')[1].split(' ')[1]
              page_data = child_element.text.split('Page:')[1].split(' ')[1]

              data = {
                  "Date Filed": date_filed_data,
                  "Volume": volume_data,
                  "Page": page_data,
              }
              df.loc[len(df)] = data
              df = df[['Date Filed', 'Volume', 'Page']]
              df.to_csv('ReleaseData.csv', index=False)

              time.sleep(1)

#Click into release document image
        
        documents = driver.find_element(By.CSS_SELECTOR, 'td[class="odd childContainerRow"]').find_elements(By.TAG_NAME, 'tr')
        for document in documents:
            if 'REL' in document.text:
                document.find_element(By.CSS_SELECTOR, 'a[class="btn btn-srchtbl"]').click()

        time.sleep(3)

#AFTER DATE, VOLUME, AND PAGE ARE RECORDED, CONTINUE WITH ADDING DOC TO CART

#Click print
        print_click = driver.find_element("xpath", '//*[@id="toolbar"]/div[1]/print-toolbar/div/a')
        print_click.click()

        time.sleep(1)

#Click print all images
        all_images = driver.find_element("xpath", '//*[@id="toolbar"]/div[1]/print-toolbar/div/ul/li[3]/a')
        all_images.click()

        time.sleep(1)

#Click add to cart
        add_to_cart = driver.find_element("xpath", '//*[@id="AddToCart"]')
        add_to_cart.click()

        time.sleep(1)

        continue_shopping = driver.find_element("xpath", '//*[@id="continue"]')
        continue_shopping.click()

        time.sleep(1)

        #print('-----------Search Complete------------')

        #quit()
