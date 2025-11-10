from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException

driver = webdriver.Chrome()
driver.quit()  # Closing the session

try:
    driver.get("https://www.google.com")  # Trying to interact after quitting
except InvalidSessionIdException as e:
    print("Exception: Invalid session ID!", e)
