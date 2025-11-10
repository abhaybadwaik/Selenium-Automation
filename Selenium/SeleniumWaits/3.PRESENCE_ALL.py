# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
#
# # Open the website
# driver.get("https://botsdna.com/locator/")
# time.sleep(5)
# driver.maximize_window()
#
# # Check for alert first
# try:
#     wait = WebDriverWait(driver, 5)
#     alert = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ng-scope")))
#     print("class name was present.")
# except:
#     print("No class name was found.")
#
# # Close the driver
# time.sleep(3)
# driver.close()
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.cricbuzz.com/")
time.sleep(5)
driver.maximize_window()

# Check for alert first
try:
    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cb-hm-text")))
    print("class name was present.")
except:
    print("No class name was found.")

# Close the driver
time.sleep(3)
driver.close()
driver.quit()