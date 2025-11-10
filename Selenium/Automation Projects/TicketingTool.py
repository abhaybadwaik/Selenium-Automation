from openpyxl import load_workbook
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

driver=webdriver.Chrome()
driver.get("https://botsdna.com/IPTicketingTool/")
driver.maximize_window()
