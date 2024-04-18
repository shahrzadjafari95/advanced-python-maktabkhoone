from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import csv

url = 'https://bama.ir/car'

driver = webdriver.Chrome()
driver.get(url)

html_page = driver.page_source

limit = 2000
soup = BeautifulSoup(html_page, 'html.parser')
items = soup.find_all('div', attrs={'class': 'bama-ad-holder'})[:limit]

