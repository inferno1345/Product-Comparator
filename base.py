from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/hello_world', methods=['POST'])
def hello_world():
    product1 = request.form['select1']
    product2 = request.form['select2']
    requirements = request.form['requirements']
    
    url = product1
    
    if url:
        req = requests.get(url)
        content = BeautifulSoup(req.content, 'html.parser')
        string_values = []
        spec_divs = content.find_all('div', class_='ux-layout-section-evo ux-layout-section--features')
        for spec_div in spec_divs:
            strings = spec_div.stripped_strings
            string_values.extend(strings)   
        print(string_values)
    else:
        print("Invalid URL:", url)
        string_values = []

    return render_template('scraped_info.html', string_values=string_values, url=url)

@app.route('/')
def index():
    return render_template('front.html')

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
