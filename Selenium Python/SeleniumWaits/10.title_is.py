from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("https://www.botsdna.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    expected_title = "botsDNA"
    wait.until(EC.title_is(expected_title))
    print("Title is Matched")
except Exception as e:
    print("Title is not Matched. Error:", e)
finally:
    driver.close()
    driver.quit()

    #THIS IS CASE SENSITIVE OKAY