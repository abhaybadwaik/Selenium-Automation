from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    search_box = driver.find_element(By.NAME, "q")
    print(search_box.get_attribute("non_existent_attribute"))  # Attribute does not exist
except NoSuchAttributeException as e:
    print("Exception: No such attribute!", e)

driver.quit()
