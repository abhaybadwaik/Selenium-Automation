# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()

# driver.get("https://botsdna.com/vitrualplots/")
# time.sleep(2)
# driver.maximize_window()
# el=driver.find_element(By.CSS_SELECTOR, "input[name='seller']")
# el.click()
# time.sleep(10)
# driver.close()
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://botsdna.com/vitrualplots/")
el=driver.find_elements(By.CSS_SELECTOR,'input[name="Buyer"]')
el1=driver.find_elements(By.CSS_SELECTOR,'input[name="seller"]')
print(len(el))
print(len(el1))
for i in el:
    i.click()
    time.sleep(1)
for j in el1:
    j.click()
    time.sleep(1)