from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="truecar"
)

brand = input('enter your desire machine:')

url = 'https://www.truecar.com/used-cars-for-sale/listings/'+brand

driver = webdriver.Chrome()
driver.get(url)

html_page = driver.page_source

limit = 20
soup = BeautifulSoup(html_page, 'html.parser')

items = soup.find_all('div', attrs={'class': 'flex w-full flex-col'})[:limit]
cursor = mydb.cursor()

for item in items:
    price = item.find('h3', attrs='heading-4 normal-case flex items-center').text
    performance = item.find('div', attrs='flex items-center truncate text-xs').text
    sql = "INSERT INTO car_informations (brand ,price, performance) VALUES (%s, %s, %s)"
    val = (brand, price, performance)
    cursor.execute(sql, val)
    mydb.commit()
    # print(price)
    # print(performance)

mydb.close()

