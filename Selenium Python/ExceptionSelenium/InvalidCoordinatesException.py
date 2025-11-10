from selenium import webdriver
from selenium.common.exceptions import InvalidCoordinatesException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    action = ActionChains(driver)
    action.move_by_offset(99999, 99999).click().perform()  # Unrealistic coordinates
except Exception as e:  # Selenium removed this exception, so catching a general one
    print("Exception: Invalid coordinates!", e)

driver.quit()
