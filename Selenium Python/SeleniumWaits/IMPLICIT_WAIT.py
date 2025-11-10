from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
s=driver.find_element(By.ID,'password')
a=s.text
print(s)
print(a)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
#
# # set implicit wait time
# driver.implicitly_wait(10)  # seconds
# driver.get("https://www.geeksforgeeks.org/")
#
# # get element after 10 seconds
# element = driver.find_element(By.LINK_TEXT,"DSA")
# element.click()


# # Import WebDriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Create WebDriver instance
# driver = webdriver.Chrome()
#
# # Set implicit wait time
# driver.implicitly_wait(10)  # seconds
#
# # Open a website (Example: Wikipedia)
# driver.get("https://www.wikipedia.org/")
#
# # Find an element by ID (Example: "searchInput" for the search box)
#
# myDynamicElement=driver.find_element(By.ID, "searchInput")
#
# print("Element found:", myDynamicElement)
#
# # Close the browser
# driver.quit()
