import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Edge()

# Open the website
driver.get("https://botsdna.com/locator/")
time.sleep(5)
driver.maximize_window()


try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/center/table[3]')))
    print("Table indentified")
except:
    print("Table not indentified.")

driver.close()
driver.quit()
