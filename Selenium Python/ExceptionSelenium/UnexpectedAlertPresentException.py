from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

try:
    driver.find_element("xpath", "//input[@id='alertexamples']").click()
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='someInput']").click()  # Trying to interact without handling alert
except UnexpectedAlertPresentException as e:
    print("Exception: Unexpected alert present!", e)

driver.quit()
