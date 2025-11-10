import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


driver = webdriver.Edge()

try:

    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width")
    driver.maximize_window()
    time.sleep(10)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
    print("In iframe: h1 tag is identified")
    driver.switch_to.default_content()

except TimeoutException:
    print("Error: Either iframe or h1 tag is not working.")

finally:
    driver.quit()
