from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

website = 'https://www.flipkart.com/lenovo-ideapad-gaming-3-amd-ryzen-7-octa-core-6800h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-i5arh7d4-laptop/p/itme459756cf8bf4?pid=COMGVQ2YEE7ZFBSW&marketplace=FLIPKART&q=laptop&srno=s_1_5&fm=productRecommendation%2Fsimilar&ppt=pp&ppn=pp&qH=312f91285e048e09'
path = '/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

try:
    # Wait for the element to be clickable
    button = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='QqFHMw _4FgsLt']")))
    button.click()

    # Wait for product information elements to be present
    products = WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="_3Fm-hO"]')))

    if not products:
        print("No info")
    else:
        for product in products:
            print(product.text)  # Use .text to get the text content of the element

except TimeoutException:
    print("Timed out waiting for elements to load.")

finally:
    driver.quit()
