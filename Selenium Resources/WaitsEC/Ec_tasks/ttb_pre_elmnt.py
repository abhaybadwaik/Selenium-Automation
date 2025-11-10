import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Edge()

# Open the website
driver.get("https://botsdna.com/server/")
time.sleep(5)
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    s = driver.find_element(By.TAG_NAME, 'h1')
    # obtain text
    t = s.text
    print(t)  # Wait for alert
except:
    print("No tag was found.")

driver.close()
driver.quit()
