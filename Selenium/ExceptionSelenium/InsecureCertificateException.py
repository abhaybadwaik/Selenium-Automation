from selenium import webdriver
from selenium.common.exceptions import InsecureCertificateException

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")  # To bypass SSL errors

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://expired.badssl.com/")  # A test site with an expired SSL certificate
except InsecureCertificateException:
    print("Insecure certificate detected!")

driver.quit()
