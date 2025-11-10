# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver=webdriver.Chrome()
# driver.get("https://demo.autokmationtesting.in/Alerts.html")
#
# driver.maximize_window()
# ele=driver.find_element(By.CSS_SELECTOR,"#OKTab>button")
# ele.click()
# WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()
# time.sleep(5)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Edge()

# Open the website
driver.get("https://rpademo.automationanywhere.com/itbricks_crm.php")
time.sleep(5)
driver.maximize_window()

# Click the button
el = driver.find_element(By.XPATH, "/html/body/form/center/table/tbody/tr[7]/td/input[1]")
el.click()
time.sleep(25)

# Check for alert first
try:
    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.alert_is_present())  # Wait for alert
    alert.accept()  # Accept the alert
    print("Alert was present and accepted.")
except:
    print("No alert was found.")

# Close the driver

driver.close()
driver.quit()