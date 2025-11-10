import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://botsdna.com/locator/')
time.sleep(2)
driver.maximize_window()
el = driver.find_element(By.CLASS_NAME, 'ng-scope')
# el.click()
print(el)
time.sleep(10)

driver.close()
driver.quit()
