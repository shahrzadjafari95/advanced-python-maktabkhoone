from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import csv

url = 'https://bama.ir/car'

driver = webdriver.Chrome()
driver.get(url)

html_page = driver.page_source

limit = 5
soup = BeautifulSoup(html_page, 'html.parser')
items = soup.find_all('div', attrs={'class': 'bama-ad-holder'})[:limit]

for item in items:
    name = item.find('p', attrs='bama-ad__title').text.strip()
    price = item.find('div', attrs='bama-ad__price-holder').text.strip()
    performance = (item.find('div', attrs={'class': 'bama-ad__detail-row'})).find('span', attrs='dir-ltr').text.strip()
    date = (item.find('div', attrs={'class': 'bama-ad__detail-row'})).find('span').text.strip()
    # with open('', 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(price)
    # print('name:', name)
    # print('price:', price)
    # print('performance:', performance)
    # print('date:', date)
    # print(100 * '*')
