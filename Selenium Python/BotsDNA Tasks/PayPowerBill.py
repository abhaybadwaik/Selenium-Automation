import os
from tkinter.tix import Select
from zipfile import ZipFile
from bs4 import BeautifulSoup
from selenium import webdriver
from pypdf import PdfReader
import shutil
import re
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from openpyxl import load_workbook
import re
from datetime import datetime

from torch.fx.experimental.unification.multipledispatch.dispatcher import source

driver=webdriver.Chrome()
driver.get("https://botsdna.com/PayPowerBill/")
with ZipFile(f"/home/bandaru/Downloads/Payments.zip", "r") as unzip:
    unzip.extractall("/home/bandaru/Downloads/jeevan")
files=os.listdir("/home/bandaru/Downloads/jeevan/Payments")



for i in files:
    print(i )
    input_string = i
    number = re.search(r'\d+', input_string).group()
    print(number)
    reader = PdfReader(f'/home/bandaru/Downloads/jeevan/Payments/{i}')
    page = reader.pages[0]
    input_str = page.extract_text()
    amount_match = re.search(r'₹ (\d+)', input_str)
    name_match = re.search(r'₹ \d+ (\w+ \w+)', input_str)
    transaction_id_match = re.search(r'T\d+', input_str)
    timestamp_match = re.search(r'(\d{1,2}:\d{2} [APM]{2} on \d{2} \w{3} \d{4})', input_str)
    amount = amount_match.group(1) if amount_match else None
    name = name_match.group(1) if name_match else None
    transaction_id = transaction_id_match.group(0) if transaction_id_match else None
    timestamp_str = timestamp_match.group(1) if timestamp_match else None
    timestamp = datetime.strptime(timestamp_str, "%I:%M %p on %d %b %Y") if timestamp_str else None
    date = timestamp.day if timestamp else None
    month = timestamp.strftime('%B') if timestamp else None
    year = timestamp.year if timestamp else None
    hour = timestamp.hour if timestamp else None
    minute = timestamp.minute if timestamp else None
    am_pm = timestamp.strftime('%p') if timestamp else None
    payments=driver.find_element(By.CSS_SELECTOR,'button[class="dropbtn"][onclick="myFunction()"')
    if i.startswith("DAE"):
        payments.send_keys("DAE BILL PAYMENT")
    elif i.startswith("DN"):
        payments.send_keys("DEMAND NOTE BILL PAYMENT")
    else:
        payments.send_keys("ENERGY BILL PAYMENT")
    time.sleep(5)
    installment_number=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Installment Number"]')
    installment_number.send_keys(number)
    time.sleep(2)
    transaction_id1=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Transaction ID"]')
    transaction_id1.send_keys(transaction_id[1:])
    time.sleep(1)
    amount1=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Amount"]')
    amount1.send_keys(amount)
    time.sleep(1)
    if len(str(date))==1:
        date1=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[1]')
        date1.click()
        date1.send_keys(f'0+{date}')
    else:
        date1 = driver.find_element(By.XPATH,
                                    '/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[1]')
        date1.click()
        date1.send_keys(date)

    month1=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[2]')
    month1.click()
    month1.send_keys(month)
    year1=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[3]')
    year1.click()
    year1.send_keys(year)
    hour1=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[4]')
    hour1.click()
    hour1.send_keys(hour)
    min1=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[5]')
    min1.click()
    min1.send_keys(minute)
    am=driver.find_element(By.XPATH,'/html/body/center/center/div/div/div/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select[6]')
    am.click()
    am.send_keys(am_pm)
    name1=driver.find_element(By.CSS_SELECTOR,'select[class="Operator"]')
    name1.click()
    name1.send_keys(name)
    time.sleep(5)
    sum=driver.find_element(By.ID,'mathExp').get_attribute('value')
    c=sum.split()
    res=driver.find_element(By.CSS_SELECTOR,'input[id="mathResult"]')
    res.click()
    res.send_keys(int(c[0])+int(c[2]))
    box=driver.find_element(By.CSS_SELECTOR,'input[id="tCheck"]')
    box.click()
    submit=driver.find_element(By.CSS_SELECTOR,'input[id="bill"]').click()
    final = driver.find_element(By.XPATH, '//*[@id="TransNo"]')
    su=final.text
    print(su)
    time.sleep(2)
    driver.back()
    driver.refresh()
    if os.path.exists("/home/bandaru/Downloads/jeevan/Payments/completed"):
        pass
    else:
        os.mkdir("/home/bandaru/Downloads/jeevan/Payments/completed")

    if i.startswith("DAE"):
        shutil.move(rf"/home/bandaru/Downloads/jeevan/Payments/{i}", rf"/home/bandaru/Downloads/jeevan/Payments/Completed/{i[0:18] + '_' + su + '.pdf'}")
    elif i.startswith("DN") or i.startswith("EB"):
        shutil.move(rf"/home/bandaru/Downloads/jeevan/Payments/{i}", rf"/home/bandaru/Downloads/jeevan/Payments/Completed/{i[0:17] + '_' + su + '.pdf'}")

    # Rename the file using shutil.move()
    # shutil.move(source, dest)/



# for f in allfiles:
#     src_path = os.path.join(source, f)
#     dst_path = os.path.join(destination, f)
#     shutil.move(src_path, dst_path)



















