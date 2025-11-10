from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.find_element("???", "test")  # Invalid selector type
except InvalidSelectorException as e:
    print("Exception: Invalid selector!", e)

driver.quit()
