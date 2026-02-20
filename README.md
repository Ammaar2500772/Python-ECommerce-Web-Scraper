# Python E-Commerce Web Scraper
A robust Python web scraping script designed to extract product data (Titles, Prices, URLs) from paginated e-commerce websites and export the organized data into an Excel-ready CSV file.

## Features:
* **BeautifulSoup4 & Requests:** Efficient HTML parsing and data extraction.
* **Pagination Handling:** Automatically loops through multiple pages of a catalog.
* **Polite Scraping:** Implements User-Agent headers and time delays (`time.sleep`) to prevent server overloading and IP blocking.
* **UTF-8-SIG Encoding:** Ensures perfect formatting when the output CSV is opened in Microsoft Excel.
* **Error Handling:** Includes HTTP status code validation.
