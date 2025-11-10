from selenium import webdriver
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    action = ActionChains(driver)
    action.move_by_offset(99999, 99999).click().perform()  # Out-of-bounds move
except MoveTargetOutOfBoundsException as e:
    print("Exception: Move target out of bounds!", e)

driver.quit()
