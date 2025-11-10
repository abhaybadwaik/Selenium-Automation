from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.calculator.net/bmr-calculator.html")
driver.maximize_window()

time.sleep(5)
age=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input')
ht=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[3]/div[2]/form/table[3]/tbody/tr[1]/td[2]/input")
wt=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[2]/form/table[3]/tbody/tr[2]/td[2]/input')
res=driver.find_element(By.XPATH,'//input[@type="submit" and @name="x"]')

# time.sleep(10)
age.clear()
age.send_keys(str(25))
ht.clear()
ht.send_keys(str(168))
wt.clear()
wt.send_keys(str(54))
res.click()
op=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[1]')
pt=op.text
print(pt)
driver.quit()