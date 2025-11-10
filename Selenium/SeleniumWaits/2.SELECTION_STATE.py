# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome()
#
# driver.get("https://botsdna.com/server/")
# time.sleep(5)
# driver.maximize_window()
#
# el = driver.find_element(By.XPATH, "/html/body/center/font/table/tbody/tr[3]/td[2]/input[1]")
# el.click()
# time.sleep(5)
#
# # Check for alert first
# try:
#     wait = WebDriverWait(driver, 5)
#     alert = wait.until(EC.element_located_selection_state_to_be((By.ID,"hdd"),True))  # Wait for alert
#     print("element selected.")
# except:
#     print("No element in selection was found.")
#
# # Close the driver
# time.sleep(5)
# driver.close()
# driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://semantic-ui.com/modules/checkbox.html")
time.sleep(5)
driver.maximize_window()

el = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div/label")
el.click()
time.sleep(5)

# Check for alert first
try:
    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.element_located_selection_state_to_be((By.NAME, "example"), True))
    print("element selected.")
except:
    print("No element in selection was found.")

# Close the driver
time.sleep(5 )
driver.close()
driver.quit()










