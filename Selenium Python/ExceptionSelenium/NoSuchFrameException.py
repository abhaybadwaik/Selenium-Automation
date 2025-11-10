from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.switch_to.frame("non_existent_frame")  # Frame does not exist
except NoSuchFrameException as e:
    print("Exception: No such frame!", e)

driver.quit()
