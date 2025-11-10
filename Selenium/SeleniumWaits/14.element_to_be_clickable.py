import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://botsdna.com/school/")
    driver.maximize_window()
    time.sleep(10)
    wait = WebDriverWait(driver, 5)
    search_school = wait.until(EC.element_to_be_clickable((By.ID, "SearchSchool")))
    search_school.click()
    print("Element is Clickable")

except TimeoutException:
    print("Element is not identified or not clickable within the timeout.")

finally:
    driver.quit()