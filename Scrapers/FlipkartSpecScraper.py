import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/seashot-m3-portable-bluetooth-mini-dynamic-metal-sound-google-alexa-siri-assistant-smart-speaker/p/itm5079154737453?pid=ACCGSE9YPKBRPHH6&marketplace=FLIPKART&spotlightTagId=BestsellerId_0pm%2F0o7&srno=b_1_1&fm=organic&ppt=browse&ppn=browse'

req = requests.get(url)
content = BeautifulSoup(req.content, 'html.parser')

string_values = []
spec_divs = content.find_all('div', class_='_1UhVsV _3AsE0T')

for spec_div in spec_divs:
    strings = spec_div.stripped_strings
    string_values.extend(strings)

if len(string_values) == 0:
    spec_divs = content.find_all('div', class_='_3TOw5k')
    for spec_div in spec_divs:
        strings = spec_div.stripped_strings
        string_values.extend(strings)

print(string_values)

# Pass the URL to the Flask app
#response = requests.post('http://127.0.0.1:5000/hello_world', data={'url': url})
#print(response.text)
