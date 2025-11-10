from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://webmail.eidiko-india.com/')
driver.maximize_window()
time.sleep(5)

#BY ID_PATH
email = driver.find_element(By.ID, "user")
email.send_keys('abhayshyamsundar.badwaik@eidiko-india.com')
time.sleep(3)

#BY USING NAME
password = driver.find_element(By.NAME,'pass')
password.send_keys('Badwaik@123')
time.sleep(3)

#
login = driver.find_element(By.XPATH, '//*[@id="login_submit"]')
login.click()
time.sleep(10)

logout = driver.find_element(By.XPATH, '//*[@id="rcmbtn106"]')
logout.click()
time.sleep(10)

driver.close()
driver.quit()
