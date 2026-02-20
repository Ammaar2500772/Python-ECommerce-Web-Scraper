import csv
import time
import requests
from bs4 import BeautifulSoup

All_Info = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for pg in range(1, 6):
    print(f"Scraping page {pg}...")
    url = f"https://books.toscrape.com/catalogue/page-{pg}.html"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error loading page {pg}: {e}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    Card = soup.find_all('article', class_='product_pod')

    for book in Card:
        txt = book.find('h3').find('a')
        title = txt['title']
        incomplete_url = txt['href']

        Complete_url = "https://books.toscrape.com/catalogue/" + incomplete_url

        price = book.find('p', class_='price_color').text

        All_Info.append({'Title': title, 'Price': price, 'Link': Complete_url})
    
    time.sleep(2)

print(f"Scraping complete. Saving {len(All_Info)} items to CSV...")

with open('master_bookstore.csv', 'w', newline='', encoding='utf-8-sig') as file:
    csv_headers = ['Title', 'Price', 'Link']
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(All_Info)

print("Data saved successfully to master_bookstore.csv!")