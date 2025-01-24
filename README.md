Program built with Python and Selenium running on Chromedriver to automate land record searches on a site with the majority of municipal databases. A lot of features need to be added to perfect the program. Script is a For loop that continues until an error occurs, which means the data it is trying to extract was not found. Used xpaths to find elements on the page and input data from a CSV file using a CSV reader. Each time the script loops it uses the next line on the CSV file. For data extraction, I used a CSS selector to find specific child elements on the page. Once this data is found, it is pulled to a Pandas dataframe that saves the text to a new CSV file called "ReleaseData.csv". The new CSV file will sort the data to easily be copied and pasted into Excel. 
