import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://botsdna.com/PayPowerBill/")
time.sleep(5)
driver.maximize_window()
el=driver.find_element(By.ID, "mathExp")
print(el)
time.sleep(5)
driver.close()
driver.quit()
