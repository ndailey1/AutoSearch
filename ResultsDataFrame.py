#Pandas dataframe created from extracting data table through website html using beautifulsoup. 
#Using this to define criteria for capturing the right data.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser

# Make a GET request
url = "https://connecticut-townclerks-records.com/LandRecords/protected/SrchBookPage.aspx"
response = requests.get(url)

# Check GET request
if response.status_code == 200:
    #print('true')

    # HTML scrape
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())






    # Pull table from HTML - why is this not working?
    table = soup.find('table', {'id': 'ctl00_cphMain_lrrgResults_cgvResults'})




# Create list to store table rows
    table_rows = []

    # Repeat for each row on the table
    for row in table.find_all('tr'):
        # Pull the cells in the current row
        cells = row.find_all(['th', 'td'])

        # Create a list to store the data in the current row
        row_data = []

        # Repeat for each cell in the current row
        for cell in cells:
            # Pull the data from the current cell
            data = cell.text.strip()

            # Add to the list for the current row
            row_data.append(data)

        # Add the list for the current row to the list of rows
        table_rows.append(row_data)

    # Make pandas dataframe from the list of rows
    df = pd.DataFrame(table_rows[1:], columns=table_rows[0])

#FINDING SPECIFIC DATA IN THE DATAFRAME

    # Set index of dataframe to the state column
    df = df.set_index('Kind')

    #Find specific values in dataframe
    value = df.loc['Release', 'Book/Page'] #access cell by row label and column name

    #Define specific value needed
    value_series = pd.Series(value, index=['Release'])

    #Save specific values to excel file
    value_series.to_excel('testsheet.xlsx', index=False)


    #Open excel sheet - THIS IS NOT WORKING
    try:
        webbrowser.open('testsheet.xlsx')
    except Exception as e:
        print("Error opening the file:", e)


else:
    print("FAILED")
