from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

website = 'https://www.jiomart.com/p/electronics/op-nord-ce-3-lite-128-gb-8-gb-ram-chromatic-grey-mobile-phone/608711332'
path = '/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

try:
    # Wait for the element to be clickable
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-target='#pdp_tech_specifications']")))
    button.click()

    # Wait for product information elements to be present
    products = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="product-specifications-wrapper"]')))

    if not products:
        print("No info")
    else:
        for product in products:
            print(product.text)  # Use .text to get the text content of the element

except TimeoutException:
    print("Timed out waiting for elements to load.")

finally:
    driver.quit()
