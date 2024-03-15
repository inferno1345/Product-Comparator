import requests
from bs4 import BeautifulSoup

url = 'https://www.croma.com/xiaomi-a-series-100-cm-40-inch-full-hd-led-smart-google-tv-with-dolby-audio-2023-model-/p/300448'

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
response = requests.post('http://127.0.0.1:5000/hello_world', data={'url': url})
print(response.text)
