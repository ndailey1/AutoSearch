Program using Python and Selenium with Chrome webdriver to automate land record searches on a website with the majority of CT town hall databases. A lot of features need to be added to perfect the program. Used Chromedriver for running. Script is a for loop that continues until an error occurs which means the data was not found. Using xpath to find elements on the page for inputing the search data into the fields that comes from a CSV file using a CSV reader. Each time the script loops it uses the next line on the CSV file. For data extraction, I used a CSS selector to find child elements on the page then takes the 3 elements that comes after the "REL" string. Once this data is found, it is pulled to a Pandas dataframe that saves the text to a new CSV file called "ReleaseData.csv" which sorts the data to easily be copied and pasted into excel. Lastly, the script will use xpath again to click into the file the data was extracted from and print the document.
