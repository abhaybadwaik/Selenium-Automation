from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    driver.find_element(By.ID, "non_existent_element")  # Element does not exist
except NoSuchElementException as e:
    print("Exception: No such element!", e)

driver.quit()
