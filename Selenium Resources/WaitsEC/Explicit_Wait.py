import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Edge()
#url launch
driver.get("https://botsdna.com/school/")
driver.maximize_window()

#expected condition for explicit wait
w = WebDriverWait(driver, 5)
w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
s = driver.find_element(By.TAG_NAME,'h1')
#obtain text
t = s.text
print(t)
time.sleep(6)
#driver quit
driver.close()
driver.quit()


"""
Creates a WebDriverWait object (w) associated with driver.
It sets a timeout of 5 seconds to wait for a specific condition.
.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
Selenium will repeatedly check for the <h1> tag for up to 5 seconds.
If the element appears before the timeout, the script continues.
If not, a TimeoutException is raised.

"""