from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")  # Sample page with a button
driver.maximize_window()

driver.switch_to.frame("iframeResult")  # Switch to iframe where button exists

try:
    button = driver.find_element(By.XPATH, "//button[text()='Try it']")
    button.click()
    print("Button clicked successfully!")
except ElementClickInterceptedException:
    print("Click was intercepted by another element!")

time.sleep(3)
driver.quit()
