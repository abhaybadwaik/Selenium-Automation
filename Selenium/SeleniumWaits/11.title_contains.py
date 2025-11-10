import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

try:

    driver.get("https://botsdna.com")
    driver.maximize_window()
    time.sleep(4)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains("botsDNA"))
    print("Title is Matched")

except TimeoutException:
    print("Title is not Matched.")

finally:
    driver.close()
    driver.quit()