import requests
#import pandas as pd
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

url='https://www.flipkart.com/alan-jones-solid-men-polo-neck-grey-t-shirt/p/itm52fee18ca2cc3?pid=TSHGQTPEFPWGTMHU&lid=LSTTSHGQTPEFPWGTMHUJNNUEY&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_1&otracker=browse&fm=organic&iid=en_htDFOhPfx8p8nA8Cx8PCEFU9qVaCo-Y8xSwsISbplqL8I5IW5abA5AuD3dLW6G_qF4tysSg1Vxof2E3ErrVxUA%3D%3D&ppt=browse&ppn=browse&ssid=v5ml08obgg0000001710482632702' #URL link for croma products
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
string_values=[]
spec_divs = content.find_all('div',class_='_30jeq3 _16Jk6d')
# Iterate over each div element
for spec_div in spec_divs:
    # Find all string values within the div
    strings = spec_div.stripped_strings
    # Append each string value to the list
    #random comment
    string_values.extend(strings)
# Print all string values
#print(string_values)
try:
    print(string_values)
except UnicodeEncodeError:
    print(string_values.encode('ascii', 'ignore').decode('ascii'))