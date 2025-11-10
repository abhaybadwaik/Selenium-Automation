# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import ElementNotInteractableException
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
#
# # Open Wikipedia
# driver.get("https://www.wikipedia.org/")
# driver.maximize_window()
# time.sleep(2)
#
# try:
#     # Try to interact with a hidden search bar (Example: using the wrong locator)
#     search_box = driver.find_element(By.ID, "searchInput")
#
#     driver.execute_script("arguments[0].style.display='none';", search_box)
#
#     search_box.send_keys("Selenium WebDriver")
#
# except ElementNotInteractableException:
#     print("Error: The element is in the DOM but is not interactable (hidden or disabled).")
#
# # Close the browser
# driver.quit()

#DRIVER.EXECUTE>SCRIPT
# 1️⃣ Clicking an element using JavaScript
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://example.com")
#
# button = driver.find_element(By.ID, "submit")  # Find button
# driver.execute_script("arguments[0].click();", button)  # Click using JS
#
# driver.quit()

# 2️⃣ For Scrolling
# Scenario: Scroll to the footer of Wikipedia using scrollIntoView().

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")

# Find the footer element
footer = driver.find_element(By.ID, "footer")

# Scroll to the footer
driver.execute_script("arguments[0].scrollIntoView();", footer)
print("Scrolled to footer")

time.sleep(10)
driver.quit()