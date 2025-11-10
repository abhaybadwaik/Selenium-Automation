from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException

driver = webdriver.Chrome()

try:
    driver.get(12345)  # Invalid URL format
except InvalidArgumentException:
    print("Exception: Invalid argument!")

driver.quit()
