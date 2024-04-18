from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import csv
from farsi_tools import replace_ascii_digits_with_farsi
from farsi_tools import standardize_persian_text

url = 'https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true'

driver = webdriver.Chrome()
driver.get(url)

html_page = driver.page_source

limit = 20
soup = BeautifulSoup(html_page, 'html.parser')
items = soup.find_all('div', attrs={'class': 'flex w-full flex-col'})[:limit]
all_cars = []
for item in items:
    car = []
    name = item.find('div', attrs={'class': 'w-full truncate font-bold'}).text[5:]
    price = item.find('h3', attrs='heading-4 normal-case flex items-center').text
    performance = item.find('div', attrs={'class': 'flex items-center truncate text-xs'}).text
    all_cars.append(car)
    car.append(name)
    car.append(performance)
    car.append(price)
    # print(car)

# print(all_cars)
with open('all_cars.csv', 'a', newline='', ) as file:
    writer = csv.writer(file)
    for row in all_cars:
        writer.writerow(row)
