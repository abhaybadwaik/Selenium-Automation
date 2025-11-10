from selenium import webdriver
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    non_select_element = driver.find_element(By.NAME, "q")  # This is not a <select> element
    select = Select(non_select_element)  # Trying to use Select on a non-dropdown
except UnexpectedTagNameException as e:
    print("Exception: Unexpected tag name!", e)

driver.quit()
