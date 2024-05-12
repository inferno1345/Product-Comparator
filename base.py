from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re

import google.generativeai as genai

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from CromaSpecScraper import def_name

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
    
def selenium_app(url):
    if url:
        path = '/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
        service = Service(executable_path=path)
        op = webdriver.ChromeOptions()
        op.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=op)
        driver.get(url)
        
        #wait = WebDriverWait(driver, 10)
        if 'amazon' in url:
            products = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-keyvalue prodDetTable"]')))
        elif 'flipkart' in url:
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='QqFHMw _4FgsLt']")))
            button.click()
            products = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="_3Fm-hO"]')))
        elif 'jiomart' in url:
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-target='#pdp_tech_specifications']")))
            button.click()
            products = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="product-specifications-wrapper"]')))
        else:
            print("Invalid URL:", url)
            string_values = []
            return string_values    
        
        string_values = []
        for spec_div in products:
            text = spec_div.text.strip()
            string_values.append(text)
    else:
        print("Invalid URL:", url)
        string_values = []
        
    driver.quit()
    return string_values
    

@app.route('/hello_world', methods=['POST'])
def hello_world():
    product1 = request.form['select1']
    product2 = request.form['select2']
    requirements = request.form['requirements']
    
    raw1 = selenium_app(product1)
    raw2 = selenium_app(product2)
    
    test = "Could you simplify the following data so that the average joe can make sense of it while being as concise and descriptive as possible: " + " ".join(raw1)
    
    info1 = model.generate_content(test)
    info = info1.text
    cleaned_info = info.replace("**", "").replace("*", "").strip()
    
    test = "Could you simplify the following data so that the average joe can make sense of it while being as concise and descriptive as possible: " + " ".join(raw2)
    info2 = model.generate_content(test)
    info2 = info2.text
    cleaned_info2 = info2.replace("**", "").replace("*", "").strip()


    # Pass markdown_info1 to the template
    return render_template('front2.html', info1=cleaned_info, info2=cleaned_info2)

@app.route('/')
def index():
    return render_template('front.html')


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
