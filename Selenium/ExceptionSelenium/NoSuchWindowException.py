from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.switch_to.window("invalid_window")  # Switching to a non-existent window
except NoSuchWindowException as e:
    print("Exception: No such window!", e)

driver.quit()
