from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://www.amazon.in/Acer-Predator-Processor-Windows-PHN16-71/dp/B0C3HTXBWP/ref=sr_1_3?crid=25ZSB640RCYW4&dib=eyJ2IjoiMSJ9.wLqXpDOv8tldGY6pAZpRGij2WNRJX2bfZynhuEPnzAXCQozC00CiS5eiMcwq9tUlB2LLPtUTYAq7BGLXRnicJZnvqH3D61sbyC9I5alxss6YUYFIHr4hVKnsPX4UiqKY8bPHBJ00pYCdqmibZHla05ioAAiOE_31vcb7iuot4_a20muViEDjIwTECHc20OW7aqZVZFCDsW6qEU_wLZQvP1_AKQDqk1FOwMrYyc_TwfWRxrLYOglxNlUmm90wmNXqb4ZI7QVWgfjTuZ-oKcdl7V3dkpu4LvthDSb8RVSdaJo.-7uV7j7EXHqzCdlwi4r7bZWo9vqDDy05ppLjnGWvMHo&dib_tag=se&keywords=predator&s=computers&sprefix=predator%2Ccomputers%2C250&sr=1-3&th=1'
path = '/Users/Tom/Documents/Programs/Product Comparator/Product-Comparator/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

# Wait for the element to be present
wait = WebDriverWait(driver, 10)
products = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-keyvalue prodDetTable"]')))

if not products:
    print("No info")

for product in products:
    print(product.text)  # Use .text to get the text content of the element

driver.quit()
