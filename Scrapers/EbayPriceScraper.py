import requests
#import pandas as pd
from bs4 import BeautifulSoup

url='' #URL link for croma products
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
string_values=[]
spec_divs = content.find_all('div',class_='x-price-primary')
# Iterate over each div element
for spec_div in spec_divs:
    # Find all string values within the div
    strings = spec_div.stripped_strings
    # Append each string value to the list
    #random comment
    string_values.extend(strings)
# Print all string values
print(string_values)