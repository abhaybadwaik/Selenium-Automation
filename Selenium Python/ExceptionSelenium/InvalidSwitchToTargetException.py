from selenium import webdriver
from selenium.common.exceptions import InvalidSwitchToTargetException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.switch_to.window("invalid_window")  # Non-existent window
except InvalidSwitchToTargetException as e:
    print("Exception: Invalid switch to target!", e)

driver.quit()
