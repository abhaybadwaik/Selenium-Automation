from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the first website
driver.get("https://www.geeksforgeeks.org/")
print("Opened:", driver.title)
time.sleep(2)

# Navigate to another website using to()
driver.get("https://www.python.org/")
print("Opened:", driver.title)
time.sleep(2)

# Go back to the previous page
driver.back()
print("Back to:", driver.title)
time.sleep(2)

# Go forward to the next page
driver.forward()
print("Forward to:", driver.title)
time.sleep(2)

# Refresh the current page
driver.refresh()
print("Page refreshed:", driver.title)
time.sleep(2)

# Close the browser
driver.quit()
