from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
driver.maximize_window()
time.sleep(5)

email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]')
email.send_keys('badwaikabhay@gmail.com')
time.sleep(3)

continu = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[2]/span/span/input')
continu.click()
time.sleep(3)

password = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input')
password.send_keys('Abhay@123')
time.sleep(3)

signin = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input')
signin.click()
time.sleep(3)

search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div[2]/div/form/div[2]/div[1]/div/input')
search.send_keys('smartphones')
search.send_keys(Keys.ENTER)

time.sleep(3)

google = driver.find_element(By.XPATH, '//*[@id="p_123/370584"]/span/a/span')
google.click()
time.sleep(3)

gb = driver.find_element(By.XPATH, '//*[@id="p_n_feature_thirty-two_browse-bin/108501313011"]/span/a/span')
gb.click()
time.sleep(3)

battery = driver.find_element(By.XPATH, '//*[@id="p_n_feature_forty-three_browse-bin/120185112011"]/span/a/span')
battery.click()
time.sleep(3)

select=driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div[4]/div[1]/a')
select.click()
time.sleep(3)
signOut=driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[26]/a')
signOut.click()
time.sleep(10)

phonename=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div[4]/div[1]/div/h1/span[1]')
ok=phonename.text
print(ok)

driver.quit()