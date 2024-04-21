from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import csv


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="11071399",
    database="truecar_all_cars"
)
cursor = mydb.cursor()

url = 'https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true&page='
for page in range(1, 10):
    url = 'https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true&page={}'.format(page)

    driver = webdriver.Chrome()
    driver.get(url)

    html_page = driver.page_source

    # limit = 5
    soup = BeautifulSoup(html_page, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'flex w-full flex-col'})

    all_cars = []
    for item in items:
        car = []
        brand = item.find('div', attrs={'class': 'w-full truncate font-bold'}).text[5:]
        car.append(brand)
        performance = item.find('div', attrs={'class': 'flex items-center truncate text-xs'}).text[:-3]
        int_performance = int(performance.replace("k", ""))
        car.append(int_performance)
        price = item.find('h3', attrs='heading-4 normal-case flex items-center').text[1:]
        int_price = int(price.replace(",", ""))
        car.append(int_price)
        all_cars.append(car)
        sql = "INSERT INTO car_informations (brand, performance, price ) VALUES (%s, %s, %s)"
        val = (brand, price, performance)
        cursor.execute(sql, val)
        mydb.commit()

    with open('all_cars.csv', 'a', newline='', ) as file:
        writer = csv.writer(file)
        for row in all_cars:
            writer.writerow(row)
mydb.close()

