from selenium import webdriver
from selenium.common.exceptions import UnableToSetCookieException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.add_cookie({"name": "test", "value": "1234", "domain": "example.com"})  # Invalid domain
except UnableToSetCookieException as e:
    print("Exception: Unable to set cookie!", e)

driver.quit()
