import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the target URL
driver.get('https://botsdna.com/notaries/')
time.sleep(2)  # Wait for the page to load
driver.maximize_window()

# Locate the link using partial link text and click it
partial_link_text = 'AP-ADVOCATES'
el = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
el.click()

time.sleep(10)

driver.close()
driver.quit()
