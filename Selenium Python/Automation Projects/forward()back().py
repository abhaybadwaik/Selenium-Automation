# importing the modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# using chrome driver
driver = webdriver.Chrome()

# taking first url
driver.get("https://www.geeksforgeeks.org/")
# getting title
print(driver.title)

# taking 2nd url
driver.get("https://www.youtube.com/")
# getting the title
print(driver.title)

# given time open url
time.sleep(2)
#
# WebDriver Navigational Commands backward
driver.back()
# given time open url
time.sleep(2)
# if back then given previous title
print(driver.title)

# WebDriver Navigational Commands backward
driver.forward()
# given time open url
time.sleep(2)
# if goto forward then given next title
print(driver.title)
driver.refresh()
driver.close()






# # importing the modules
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.udemy.com/?utm_source=aff-campaign&utm_medium=udemyads&LSNPUBID=OzpaRYwFVr0&ranMID=47901&ranEAID=OzpaRYwFVr0&ranSiteID=OzpaRYwFVr0-yzBZn49xqfM6N4lo5RU6Og&gad_source=1&gclid=CjwKCAiA2cu9BhBhEiwAft6IxFkYhXTZUy_wnr1CC0UBOto7T7tcCdDbCoP96VLYPjukHSWq6or4PBoCMUYQAvD_BwE")
# driver.maximize_window()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# time.sleep(3)
# driver.close()