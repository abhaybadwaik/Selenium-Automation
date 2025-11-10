import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://botsdna.com/server/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    element = driver.find_element(By.ID, "CreateServer")
    time.sleep(6)
    wait.until(EC.visibility_of(element))
    print("Element Identified")
except TimeoutException:
    print("Element is not Identified.")

finally:
    driver.close()
    driver.quit()