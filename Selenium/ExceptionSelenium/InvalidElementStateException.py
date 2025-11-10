from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_input_disabled")

try:
    driver.switch_to.frame("iframeResult")
    input_field = driver.find_element(By.NAME, "fname")
    input_field.send_keys("Testing")  # Trying to type in a disabled field
except InvalidElementStateException as e:
    print("Exception: Element is in an invalid state!", e)

driver.quit()
