import requests
from bs4 import BeautifulSoup

url='https://www.ebay.com/itm/314284067722?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20230823115209%26meid%3D11947d1035294301ba56277a0ede0db3%26pid%3D101800%26rk%3D1%26rkt%3D1%26itm%3D314284067722%26pmt%3D1%26noa%3D1%26pg%3D4375194%26algv%3DRecentlyViewedItemsV2SignedOut%26brand%3DRolex&_trksid=p4375194.c101800.m5481&_trkparms=parentrq%3Aff100c7218d0aaf6560ac879fffe7d8a%7Cpageci%3A7676f63b-d88d-11ee-b6b5-a6c5b8cf1404%7Ciid%3A1%7Cvlpname%3Avlp_homepage' #place URL here
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
string_values=[]
spec_divs = content.find_all('div',class_='ux-layout-section-evo ux-layout-section--features')
# Iterate over each div element
for spec_div in spec_divs:
    # Find all string values within the div
    strings = spec_div.stripped_strings
    # Append each string value to the list
    string_values.extend(strings)   
# Print all string values
print(string_values)