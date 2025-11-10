from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

try:
    hidden_text = driver.find_element(By.ID, "myDIV")  # Hidden div
    hidden_text.click()  # Trying to click a hidden element
except ElementNotVisibleException:
    print("Element is not visible!")

time.sleep(3)
driver.quit()
