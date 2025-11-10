# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://botsdna.com/notaries/")
# time.sleep(2)
# driver.maximize_window()
# el=driver.find_element(By.TAG_NAME, "input")
# el.send_keys("thank you")
# # print(el)
# time.sleep(2)
# driver.close()
# driver.quit()
#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.zomato.com/")
driver.maximize_window()
time.sleep(2)
s=driver.find_element(By.TAG_NAME,"h1")
print(s.text)
time.sleep(5)