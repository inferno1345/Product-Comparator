
import requests
import pandas as pd
from bs4 import BeautifulSoup

url='' #ENTER PRODUCT LINK HERE
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
#print(content)
string_values=[]
spec_divs = content.find_all('div', class_='_1UhVsV _3AsE0T')

# Iterate over each div element
for spec_div in spec_divs:
    # Find all string values within the div
    strings = spec_div.stripped_strings
    # Append each string value to the list
    string_values.extend(strings)
if(len(string_values) ==0):
    spec_divs=content.find_all('div', class_='_3TOw5k')
    for spec_div in spec_divs:

        # Find all string values within the div
        strings = spec_div.stripped_strings

        # Append each string value to the list
        string_values.extend(strings)
    
# Print all string values
print(string_values)