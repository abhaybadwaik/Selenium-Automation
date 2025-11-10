import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get("https://rpademo.automationanywhere.com/itbricks_enroll.php")
driver.maximize_window()
time.sleep(10)
el = driver.find_element(By.XPATH, "/html/body/form/center/table")
table_html = el.get_attribute('outerHTML')
soup = BeautifulSoup(table_html, 'html.parser')
rows = soup.find_all('tr')
table = []
i = 1
row1 = []
for row in rows:
    columns = row.find_all(('td', 'th'))
    dat = [col.get_text(strip=True) for col in columns]
    if i == 1:
        row1 = dat
        i += 1
    else:
        row2 = {row1[j]: dat[j] for j in range(len(dat))}
        table.append(row2)
for each in table:
    print(each)
driver.quit()






#
# el = driver.find_element(By.TAG_NAME, "table")
# table_html = el.get_attribute('outerHTML')
# soup = BeautifulSoup(table_html, 'html.parser')
# rows = soup.find_all('tr')
# table = []
# i = 1
# row1 = []
# for row in rows:
#     columns = row.find_all(('td', 'th'))
#     dat = [col.get_text(strip=True) for col in columns]
#     if i == 1:
#         row1 = dat
#         i += 1
#     else:
#         row2 = {row1[j]: dat[j] for j in range(len(dat))}
#         table.append(row2)
# print(table)
# j=2
# for i in table:
#     sheet['H' + str(j)] = i['STATUS']
#     sheet['G' + str(j)] = i['PAN NUMBER']
#     j+=1
