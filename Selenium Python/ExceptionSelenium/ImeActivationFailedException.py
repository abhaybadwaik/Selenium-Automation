from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    # Attempt to activate an IME engine (which will fail)
    try:
        driver.ime.activate_engine("Japanese")  # This will raise an error
        print("IME activated successfully.")
    except Exception as e:
        print("IME Activation Failed:", e)

    time.sleep(2)

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    driver.quit()
    print("Browser closed.")
