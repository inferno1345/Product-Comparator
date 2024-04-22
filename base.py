import re
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re

import google.generativeai as genai

genai.configure(api_key='AIzaSyBikkmJTd7ie4cZPnPNEZ_ANLeBlENAGl4')
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

'''client = OpenAI(api_key = 'sk-proj-gyg3FAPF7h6Z2WctUoDzT3BlbkFJljs5VBS1erZDIcng4cXx')

def get_completion(prompt): 
    #print(prompt) 
    messages=[{"role": "system", "content": "You are a data analyzer who compares information and helps the average person to identify and pros and cons of a product."},
                  {"role": "user", "content": prompt}]
    query = client.chat.completions.create(
        model="davinci-002",
        messages = messages
        
    )
    return query.choices[0].message.content
    '''


def soup(url):
    if url:
        req = requests.get(url)
        content = BeautifulSoup(req.content, 'html.parser')
        string_values = []
        
        if 'ebay' in url:
            spec_divs = content.find_all('div', class_='ux-layout-section-evo ux-layout-section--features')
        elif 'snapdeal' in url:
            spec_divs = content.find_all('div',class_='tab-container')
        else:
            print("Invalid URL:", url)
            string_values = []
            return string_values
        
        for spec_div in spec_divs:
            strings = spec_div.stripped_strings
            string_values.extend(strings)   
        return string_values
    
    else:
        print("Invalid URL:", url)
        string_values = []
        return string_values
    
    

@app.route('/hello_world', methods=['POST'])
def hello_world():
    product1 = request.form['select1']
    product2 = request.form['select2']
    requirements = request.form['requirements']
    
    raw1 = soup(product1)
    raw2 = soup(product2)
    
    test = "Could you simplify the following data so that the average joe can make sense of it while being as concise and descriptive as possible: " + " ".join(raw1)
    
    info1 = model.generate_content(test)
    info = info1.text
    cleaned_info = info.replace("**", "").replace("*", "").strip()
    print(cleaned_info)
    
    test = "Could you simplify the following data so that the average joe can make sense of it while being as concise and descriptive as possible: " + " ".join(raw2)
    info2 = model.generate_content(test)
    info2 = info2.text
    cleaned_info2 = info2.replace("**", "").replace("*", "").strip()
    print(cleaned_info2)


    # Pass markdown_info1 to the template
    return render_template('front2.html', info1=cleaned_info, info2=cleaned_info2)

@app.route('/')
def index():
    return render_template('front.html')


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
