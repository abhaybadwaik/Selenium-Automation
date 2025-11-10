from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Wikipedia homepage
driver.get("https://www.wikipedia.org/")

# Wait for the search input box to be present in the DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)

print("Element is present in the DOM!")

# Close browser
driver.quit()
