import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Initialize a DataFrame with additional columns for mortgage Volume and Page
df = pd.DataFrame(columns=["Volume", "Page", "Date Filed", "Mortgage Volume", "Mortgage Page"])

# Open the CSV file containing Volume and Page data for searching
with open("ExampleData.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate through each row in the CSV
    for line in csv_reader:
        # Launch a new Chrome browser instance
        driver = webdriver.Chrome()
        # Navigate to the RecordHub search page for Windsor Locks, CT
        driver.get('https://recordhub.cottsystems.com/WinchesterCT/Search/Records')
        time.sleep(1)  # Wait for page to load


#* LOGIN CREDENTIALS REQUIRED*

        email = driver.find_element("xpath", '//*[@id="UserName"]')
        email.send_keys('username')

        password = driver.find_element("xpath", '//*[@id="Password"]')
        password.send_keys('pass')


        time.sleep(1)  # Brief pause before submitting
        login = driver.find_element("xpath", '//*[@id="submit"]')
        login.click()
        time.sleep(1)  # Wait for login to process

        # Select "Book/Page" search option from dropdown
        search_drop_down = driver.find_element("xpath", '//*[@id="btnSearchType"]')
        search_drop_down.click()
        time.sleep(1)

        book_page = driver.find_element("xpath", '//*[@id="Type"]/ul/li[4]/a')
        book_page.click()
        time.sleep(1)

        # Input Volume and Page from CSV into search fields
        volume = driver.find_element("xpath", '//*[@id="Book"]')
        volume.send_keys(line[0])  # Volume from CSV column 0
        mortgage_volume = line[0]  # Store mortgage Volume

        page = driver.find_element("xpath", '//*[@id="Page"]')
        page.send_keys(line[1])    # Page from CSV column 1
        mortgage_page = line[1]    # Store mortgage Page

        time.sleep(1)
        search_button = driver.find_element("xpath", '//*[@id="search-btn"]')
        search_button.click()
        time.sleep(3)  # Wait for search results to load

        # Check for release documents and extract data
        release_found = False  # Flag to track if a release is found
        try:
            # Click into related documents (assumes single mortgage result)
            related_documents = driver.find_element("xpath", '//*[@id="search-results-table"]/tbody/tr[1]/td[3]/a[3]')
            related_documents.click()
            time.sleep(1)

            # Look for release documents in related documents
            child_elements = driver.find_elements(By.CSS_SELECTOR, 'td[class="childData"]')
            for child_element in child_elements:
                if 'REL' in child_element.text:  # Check if it's a release document
                    release_found = True
                    # Extract Date Filed, Volume, and Page from text
                    date_filed_data = child_element.text.split('Filed:')[1].split(' ')[1]
                    volume_data = child_element.text.split('Volume:')[1].split(' ')[1]
                    page_data = child_element.text.split('Page:')[1].split(' ')[1]

                    # Store extracted data in DataFrame, including mortgage Volume/Page
                    data = {
                        "Date Filed": date_filed_data,
                        "Volume": volume_data,
                        "Page": page_data,
                        "Mortgage Volume": mortgage_volume,
                        "Mortgage Page": mortgage_page,
                    }
                    df.loc[len(df)] = data
                    df.to_csv('ReleaseData.csv', index=False)  # Save to CSV
                    time.sleep(1)

                    # Click into the release document
                    documents = driver.find_element(By.CSS_SELECTOR, 'td[class="odd childContainerRow"]').find_elements(By.TAG_NAME, 'tr')
                    for document in documents:
                        if 'REL' in document.text:
                            document.find_element(By.CSS_SELECTOR, 'a[class="btn btn-srchtbl"]').click()
                            time.sleep(3)  # Wait for document to load

                    # Add document to cart for printing
                    print_click = driver.find_element("xpath", '//*[@id="toolbar"]/div[1]/print-toolbar/div/a')
                    print_click.click()
                    time.sleep(1)

                    all_images = driver.find_element("xpath", '//*[@id="toolbar"]/div[1]/print-toolbar/div/ul/li[3]/a')
                    all_images.click()
                    time.sleep(1)

                    add_to_cart = driver.find_element("xpath", '//*[@id="AddToCart"]')
                    add_to_cart.click()
                    time.sleep(1)

                    continue_shopping = driver.find_element("xpath", '//*[@id="continue"]')
                    continue_shopping.click()
                    time.sleep(1)

                    #print("\u001b[32m----------------------Search Complete!-----------------------\u001b[0m")

        except Exception as e:
            # If any error occurs (e.g., no results, element not found), log "No Release"
            print(f"Error for Volume: {mortgage_volume}, Page: {mortgage_page} - {str(e)}")
            data = {
                "Date Filed": "No Release",
                "Volume": "N/A",
                "Page": "N/A",
                "Mortgage Volume": mortgage_volume,
                "Mortgage Page": mortgage_page,
            }
            df.loc[len(df)] = data
            df.to_csv('ReleaseData.csv', index=False)  # Save to CSV

        # If no release was found in the try block, log it (in case error wasn't the issue)
        if not release_found:
            print(f"No release found for Volume: {mortgage_volume}, Page: {mortgage_page}")
            data = {
                "Date Filed": "No Release",
                "Volume": "N/A",
                "Page": "N/A",
                "Mortgage Volume": mortgage_volume,
                "Mortgage Page": mortgage_page,
            }
            # Only append if not already added in the except block
            if len(df) == 0 or df.iloc[-1]["Date Filed"] != "No Release":
                df.loc[len(df)] = data
                df.to_csv('ReleaseData.csv', index=False)

        # Close the browser after processing this row
        driver.quit()
