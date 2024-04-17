from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/hello_world', methods=['POST'])
def hello_world():
    product1 = request.form['select1']
    product2 = request.form['select2']
    requirements = request.form['requirements']
    
    url1 = product1
    
    if url1:
        req = requests.get(url1)
        content = BeautifulSoup(req.content, 'html.parser')
        string_values = []
        
        if 'ebay' in url1:
            spec_divs = content.find_all('div', class_='ux-layout-section-evo ux-layout-section--features')
        elif 'snapdeal' in url1:
            spec_divs = content.find_all('div',class_='tab-container')
        else:
            print("Invalid URL:", url1)
            string_values = []
        
        for spec_div in spec_divs:
            strings = spec_div.stripped_strings
            string_values.extend(strings)   
        print(string_values)
    else:
        print("Invalid URL:", url1)
        string_values = []

    return render_template('scraped_info.html', string_values=string_values, url=url1)

@app.route('/')
def index():
    return render_template('front.html')

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
