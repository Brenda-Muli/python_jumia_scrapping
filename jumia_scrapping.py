
import requests
from bs4 import BeautifulSoup
import csv

# Fetching the page that contains the Jumia Flash sales
response = requests.get('https://www.jumia.co.ke/flash-sales/')

#fetch and parse the page using beautiful soup
result = requests.get('https://www.jumia.co.ke/flash-sales/')
# ensure I obtain 200 ok response that the page is present
print(result.status_code)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(result.text, 'html.parser')

# Find section containing the flash sale deals
deals_section = soup.find_all('div', class_='-paxs row _no-g _4cl-3cm-shs')

# Create a list that will be used to store deal data
deals_data = []

# Extracting name, price, discounts and reviews
for deal in deals_section:
    items = deal.find_all('div', class_='info')

    for item in items:
        try:
            # Extract product name
            product_name_elements = item.find_all('h3', class_='name')
            product_name = product_name_elements[0].text.strip()

            # Extract product price
            product_price_elements = item.find_all('div', class_='prc')
            product_price = product_price_elements[0].text.strip()

            # Extract product discount (if any)
            product_discount_element = item.find('div', class_='bdg _dsct _sm')
            if product_discount_element:
                product_discount = product_discount_element.text.strip()
            else:
                product_discount = 'No discount'

            # Extract product review (if any)
            product_review_element = item.find('div', class_='rev')
            if product_review_element:
                product_review = product_review_element.text.strip()
            else:
                product_review = 'No reviews'

            # Storing the extracted data in the deals_data list created
            deals_data.append([product_name, product_price, product_discount, product_review])

        except AttributeError as e:
            print(f'Error extracting data: {e}')

print(deals_data)

# Write the extracted data to a CSV file
with open('deals.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Product Price', 'Product Discount', 'Product Review'])
    writer.writerows(deals_data)

print("Data has been written to deals.csv")