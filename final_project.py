from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import csv

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="11071399",
    database="truecar_all_cars"
)
cursor = mydb.cursor()

url = 'https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true&page='
for page in range(1, 10):  # use loop fpr get 10 first page of truecar.com
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
        brand = item.find('div', attrs={'class': 'w-full truncate font-bold'}).text[5:]  # get brand without USED
        car.append(brand)
        # get performance without mi
        performance = item.find('div', attrs={'class': 'flex items-center truncate text-xs'}).text[:-3]
        int_performance = int(performance.replace("k", ""))  # convert str performance to int and delete k in of it.
        car.append(int_performance)
        price = item.find('h3', attrs='heading-4 normal-case flex items-center').text[1:]  # get price without $
        int_price = int(price.replace(",", ""))  # convert  str price to int
        car.append(int_price)
        all_cars.append(car)
        sql = "INSERT INTO car_informations (brand, performance, price ) VALUES (%s, %s, %s)"
        val = (brand, price, performance)
        cursor.execute(sql, val)  # save all information into the database
        mydb.commit()

    with open('all_cars.csv', 'a', newline='', ) as file:  # save all cars that get into the csv file
        writer = csv.writer(file)
        for row in all_cars:
            writer.writerow(row)
mydb.close()


# use machine learning method for predicting name of car when user enter price and performance
x = []
y = []
with open('all_cars.csv', 'r') as csv_file:  # read from csv file
    data = csv.reader(csv_file)
    for line in data:
        x.append(line[1:])
        y.append(line[0])

clf = DecisionTreeClassifier()

clf = clf.fit(x, y)
# enter performance and price with format for example 23 43000
user_input = list(map(int, input('Please enter the performance price and you want:').split(' ')))
predictions = clf.predict([user_input])
print(predictions)
