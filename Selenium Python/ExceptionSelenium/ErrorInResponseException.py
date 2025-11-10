from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()

try:
    driver.get("https://httpstat.us/500")  # A test page that returns a server error
except WebDriverException:
    print("Server error occurred!")

driver.quit()
