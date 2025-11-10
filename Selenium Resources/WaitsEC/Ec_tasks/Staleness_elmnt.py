from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
    driver.get("https://botsdna.com/VegetableBasket/")
    driver.maximize_window()
    el=driver.find_element(By.ID,'updateVeg')
    wait = WebDriverWait(driver, 15)
    wait.until(EC.staleness_of(el))
    print("Staleness")

except TimeoutException:
    print("staleness is not working.")

finally:
    driver.quit()
