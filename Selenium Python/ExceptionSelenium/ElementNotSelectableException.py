from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotSelectableException
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option_disabled")

driver.switch_to.frame("iframeResult")  # Switch to iframe where dropdown exists

try:
    disabled_option = driver.find_element(By.XPATH, "//option[@disabled]")  # Trying to select disabled option
    disabled_option.click()
except ElementNotSelectableException:
    print("Element is not selectable!")

time.sleep(3)
driver.quit()
