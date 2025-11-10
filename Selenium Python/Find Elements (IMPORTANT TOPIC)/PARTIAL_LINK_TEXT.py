import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://botsdna.com/notaries/')
time.sleep(2)
driver.maximize_window()

el = driver.find_element(By.PARTIAL_LINK_TEXT, 'AP-ADVOCATES')
el.click()

time.sleep(10)

# Close the browser
driver.close()
driver.quit()
