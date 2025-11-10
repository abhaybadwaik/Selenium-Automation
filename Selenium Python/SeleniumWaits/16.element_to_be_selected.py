from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open demo login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for the login button to be present in the DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "submit"))
)

print("Login button is present in the DOM!")

# Close browser
driver.quit()
