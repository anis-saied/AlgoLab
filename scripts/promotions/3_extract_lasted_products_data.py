import requests
from bs4 import BeautifulSoup
import json

# Function to extract product data from a URL
def extract_product_data(url):
    #print(f"Extracting data from URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        product_info = {}

        # Extract product data from the HTML structure
        # Modify this part based on the structure of the target website
        product_info["URL"] = url
        product_info["Title"] = soup.find("title").text.strip()

        # Add more data extraction logic here
        price_div = soup.find("div", class_="product-info-price")

        if price_div:
            special_price = price_div.find("span", class_="price").text
            old_price_element = price_div.find("span", {"data-price-type": "oldPrice"})
            old_price = old_price_element.text if old_price_element else None
            discount_element = price_div.find("span", class_="discount-price")
            discount = discount_element.text if discount_element else None

            product_info["Prix spécial"] = special_price
            product_info["Ancien prix"] = old_price
            product_info["Réduction"] = discount

        stock_and_sku_div = soup.find("div", class_="product-info-stock-sku")
        overview_div = soup.find("div", class_="product attribute overview")
        image_div = soup.find("div", class_="carousel-inner")

        if stock_and_sku_div:
            availability = stock_and_sku_div.find("div", class_="stock").text
            reference = stock_and_sku_div.find("div", class_="value", itemprop="sku").text
        else:
            availability = reference = None

        if overview_div:
            description_element = overview_div.find("div", class_="value", itemprop="DescriptionURL")
            description = description_element["href"] if description_element else None
        else:
            description = None

        if image_div:
            image = image_div.find("img", itemprop="image")["src"]
        else:
            image = None

        product_info["Disponibilité"] = availability
        product_info["Référence"] = reference
        product_info["Description"] = description
        product_info["Image"] = image

        return product_info

    #print(f"Product with URL {url} does not have a valid price.")
    return None

# Function to process a list of product URLs
def process_urls(input_file, output_file):
    with open(input_file, "r") as input_json:
        input_data = json.load(input_json)
        output_data = []

        for url in input_data[:500]:
            product_data = extract_product_data(url)
            if product_data:
                output_data.append(product_data)

        with open(output_file, "w", encoding="utf-8") as output_json:
            json.dump(output_data, output_json, ensure_ascii=False, indent=4)
        print(f"Data extracted from {len(output_data)} URLs and saved to {output_file}")

if __name__ == "__main__":
    input_file = "recent_products_urls.json"  # Change this to your input file
    output_file = "recent_products_data.json"  # Change this to your output file
    process_urls(input_file, output_file)

