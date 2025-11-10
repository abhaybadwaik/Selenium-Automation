from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    driver.maximize_window()

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Type a query and press ENTER
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    # Wait until the old search box disappears (staleness)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.staleness_of(search_box))

    print("Staleness detected! The old search box is gone.")

except TimeoutException:
    print("Staleness condition not met.")

finally:
    # Close the browser
    driver.quit()
