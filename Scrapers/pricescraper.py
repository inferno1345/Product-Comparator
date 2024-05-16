from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 
import time

website = 'https://www.flipkart.com/clapcart-success-motivational-quotation-printed-mousepad-computer-pc-laptop/p/itm9c6d41cef453b?pid=ACCGG8MBF7RGZRZ7&lid=LSTACCGG8MBF7RGZRZ7C0KWQD&marketplace=FLIPKART&q=mouse+pad&store=6bo&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_icYpbBhSf0WRkxTfco7wlIA0px3N7q8AFnT4VdBzjPd8mZfAFXTIX6JhauGmy_k541PF0H8cZ3moxLvNhBXcpQ%3D%3D&ppt=sp&ppn=sp&ssid=hhqf9xv3gw0000001715698307044&qH=f51896446fa8792d'
path = 'C:/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

try:
    # Wait for the element to be clickable
    '''button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-target='#pdp_tech_specifications']")))
    button.click()

    # Wait for product information elements to be present
    products = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="product-specifications-wrapper"]')))

    if not products:
        print("No info")
    else:
        for product in products:
            print(product.text)  # Use .text to get the text content of the element'''
    tit=""
    title = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="VU-ZEz"]')))
    for titles in title:
        print(titles.text)
        tit=titles.text+"-"
    print(tit)
    #driver.quit()
    time.sleep(5)
    driver.get("https://www.amazon.in")
    input_element=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]') #id="twotabsearchtextbox"
    input_element.send_keys(tit + Keys.ENTER)
    time.sleep(5)
    url=driver.current_url
    price = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-price-whole"]')))
    print(price[1].text)
    print(url)
    time.sleep(10)
except TimeoutException:
    print("Timed out waiting for elements to load.")

finally:
    driver.quit()
