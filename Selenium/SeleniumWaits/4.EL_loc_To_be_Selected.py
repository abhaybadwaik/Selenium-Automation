import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Edge()
# Open the website
driver.get("https://botsdna.com/PayPowerBill/")
time.sleep(5)
driver.maximize_window()

el=driver.find_element(By.ID,'tCheck')
el.click()

# Check for alert first
try:
    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.element_located_to_be_selected((By.ID, "tCheck")))
    print("check box selected.")
except:
    print("No checkbox in selection was found.")

# Close the driver
time.sleep(5)
driver.close()
driver.quit()