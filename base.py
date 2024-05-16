from flask import Flask, render_template, request
import requests
import time
import atexit

from bs4 import BeautifulSoup

from openai import OpenAI

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

app = Flask(__name__)

client = OpenAI(api_key = 'sk-proj-P1Geb3FAub2ams0wnB11T3BlbkFJoKKaUmjYdXrlTHv2HzNr')

product1=""

def get_completion(prompt): 
    messages=[
        {"role": "system", "content": "You are a data analyzer who compares information and helps the average person to identify the pros and cons of a product while being as consistent as possible with readable format"},
        {"role": "user", "content": prompt}
        ]
    query = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
    return query.choices[0].message.content
    
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
    
path = '/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service)    
    
def selenium_app(url):
    if url:
        global driver
        driver.get(url)
        time.sleep(3)
        if 'amazon' in url:
            price = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-price-whole"]')))
            products = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-keyvalue prodDetTable"]')))
            final_price = price[4]
            
        elif 'flipkart' in url:
            price = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="Nx9bqj CxhGGd"]')))
            final_price = price[0]
            button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='QqFHMw _4FgsLt']")))
            button.click()
            products = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="_3Fm-hO"]')))
        
        elif 'jiomart' in url:
            price = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jm-heading-xs jm-ml-xxs"]')))
            final_price = price[0]
            button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-target='#pdp_tech_specifications']")))
            button.click()
            products = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="product-specifications-wrapper"]')))
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
        
    return string_values, final_price.text
    
@app.route('/price_comp', methods=['POST'])
def price():
    global driver
    url = product1
    print(url)
    driver.get(url)
    title = product_title = ""
    url_now1 = url_now2 = price1 = price2 = ""
    if 'flipkart' in url:
        title = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="VU-ZEz"]')))
        for titles in title:
            print(titles.text)
            product_title = titles.text 
            
        driver.get("https://www.amazon.in")
        input_element = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]') 
        input_element.send_keys(product_title + Keys.ENTER)
        time.sleep(2)
        url_now1 = driver.current_url
        print(url_now1)
        price = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-price-whole"]')))
        price1 = price[1].text
        
        driver.get("https://www.jiomart.com")
        input_element = driver.find_element(By.XPATH,'//*[@class="aa-Input search_input"]') 
        input_element.send_keys(product_title + Keys.ENTER)
        url_now2 = driver.current_url
        print(url_now2)
        price = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jm-heading-xxs jm-mb-xxs"]')))
        price2 = price[0].text
        
    return render_template('front3.html', url_now1=url_now1, price1=price1, url_now2=url_now2, price2=price2)
        

@app.route('/hello_world', methods=['POST'])
def hello_world():
    global product1
    product1 = request.form['select1']
    product2 = request.form['select2']
    requirements = request.form['requirements']
    
    if 'ebay' in product1 or 'snapdeal' in product1:
        raw1 = soup(product1)
        raw2 = soup(product2)
    else:
        raw1, price1 = selenium_app(product1)
        raw2, price2 = selenium_app(product2)
    
    test = "Could you simplify the following data and break into portions such as Name, Description, Specificaions and so on (avoid bold text): \n" + "".join(raw1)   
    info1 = get_completion(test)
 
    test = "Could you simplify the following data and break into portions such as Name, Description, Specificaions and so on (avoid bold text): \n" + "".join(raw2)
    info2 = get_completion(test)

    atexit.register(close_driver)
    return render_template('front2.html', info1=info1, info2=info2, price1=price1, price2=price2)

@app.route('/')
def index():
    return render_template('front.html')


def close_driver():
    global driver
    if driver:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
