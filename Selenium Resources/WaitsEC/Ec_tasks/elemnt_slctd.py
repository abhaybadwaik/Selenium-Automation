from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


driver = webdriver.Edge()

try:
    driver.get("https://botsdna.com/PayPowerBill/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    search_school = wait.until(EC.presence_of_element_located((By.ID, "tCheck")))
    search_school.click()
    wait.until(EC.element_to_be_selected(search_school))
    print("Element is selected")

except TimeoutException:
    print("Element is not identified within the timeout.")

finally:
    driver.quit()
