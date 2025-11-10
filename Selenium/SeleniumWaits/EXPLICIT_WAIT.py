from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the website
driver.get('https://practicetestautomation.com/practice-test-login/')

# Wait for the element to be visible and clickable
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "submit"))
)

# Click the element
element.click()

driver.quit()
