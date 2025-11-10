import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://botsdna.com/VegetableBasket/")
time.sleep(5)
driver.maximize_window()

wbl=driver.find_element(By.ID,'vegCode')
time.sleep(5)
wbl.click()
wbl.send_keys("VEG5440")
time.sleep(3)

try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "vegCode"), "VEG5440"))
    print("text indentified")
except:
    print("No text indentified.")

driver.close()
driver.quit()