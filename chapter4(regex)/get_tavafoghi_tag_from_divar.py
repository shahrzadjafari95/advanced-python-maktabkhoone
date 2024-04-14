from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://divar.ir/s/tehran/rent-residential'

driver = webdriver.Chrome()
driver.get(url)

html_page = driver.page_source

soup = BeautifulSoup(html_page, 'html.parser')
# print(soup)
pattern = 'رهن کامل'
# extract all ads from divar with separate attrs={'class': 'kt-post-card__info'}
all_ads = soup.find_all('div', attrs={'class': 'kt-post-card__info'})
for ad in all_ads:  # loop in all ads
    # extract content of ads that contain attrs={'class': 'kt-post-card__description'}
    all_prices = ad.find_all('div', attrs={'class': 'kt-post-card__description'})
    for price in all_prices:  # loop in all price
        if price.string == pattern:
            # print(price)
            title = ad.find('h2', attrs='kt-post-card__title')
            print(title.text)


