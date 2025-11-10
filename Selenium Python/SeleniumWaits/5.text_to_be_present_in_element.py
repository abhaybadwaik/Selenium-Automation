import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://botsdna.com/jewelry/")

e=driver.find_element(By.TAG_NAME,"h4")
e.click()
# print(e.text)
try:
    w=WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h4"), "in"))
    print(w)
    print("text is present")
except:
    print("text is not present")
time.sleep(3)
driver.quit()