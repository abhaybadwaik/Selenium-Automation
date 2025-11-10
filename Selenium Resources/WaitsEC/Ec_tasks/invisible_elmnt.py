import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
    driver.get("https://botsdna.com/server/")
    driver.maximize_window()
    time.sleep(10)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.invisibility_of_element_located((By.ID, "serverIP")))
    print("Element Identified")

except TimeoutException:
    print("Element is not identified or not clickable within the timeout.")

finally:
    driver.quit()
