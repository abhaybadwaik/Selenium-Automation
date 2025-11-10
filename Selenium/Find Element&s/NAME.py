import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get('https://botsdna.com/IPTicketingTool/PeopleFinder.html')
time.sleep(2)
driver.maximize_window()
el=driver.find_element(By.NAME,'search')
el.click()
el.send_keys('ABHAY')
time.sleep(10)
