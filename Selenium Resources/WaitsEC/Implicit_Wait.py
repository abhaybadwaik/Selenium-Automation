from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(0.10)


driver.get("https://www.tutorialspoint.com/about/about_careers.htm")

l = driver.find_element(By.LINK_TEXT,'FAQ')
print(driver.title)


driver.close()
driver.quit()

"""

Default Timeout for Implicit Wait is 0 seconds. 
Here the Selenium Command reports immediately if it cannot find an element. 
Default Timeout for Page Load is 300 seconds. 
Default Timeout for Script Timeout is 30 seconds.

"""