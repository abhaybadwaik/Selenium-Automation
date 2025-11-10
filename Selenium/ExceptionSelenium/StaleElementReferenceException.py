from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    search_box = driver.find_element(By.NAME, "q")
    driver.refresh()  # Refreshing the page, making the element stale
    search_box.send_keys("Selenium")
except StaleElementReferenceException as e:
    print("Exception: Stale element reference!", e)

driver.quit()
