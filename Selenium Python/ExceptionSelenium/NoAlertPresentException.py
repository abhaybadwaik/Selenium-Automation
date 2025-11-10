from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.switch_to.alert.accept()  # No alert present
except NoAlertPresentException as e:
    print("Exception: No alert present!", e)

driver.quit()
