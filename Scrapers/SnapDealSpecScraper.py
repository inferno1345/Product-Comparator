import requests
from bs4 import BeautifulSoup

url='https://www.snapdeal.com/product/fratelli-red-plastic-car-pack/657704369642#bcrumbLabelId:1320'
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
string_values=[]
spec_divs = content.find_all('div',class_='tab-container')
# Iterate over each div element
for spec_div in spec_divs:
    # Find all string values within the div
    strings = spec_div.stripped_strings
    # Append each string value to the list
    string_values.extend(strings)
# Print all string values
print(string_values)
