from selenium import webdriver
from selenium.common.exceptions import InvalidCookieDomainException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    cookie = {'name': 'test_cookie', 'value': '1234', 'domain': 'example.com'}
    driver.add_cookie(cookie)
except InvalidCookieDomainException as e:
    print("Exception: Invalid cookie domain!", e)

driver.quit()
