import requests
from bs4 import BeautifulSoup
import json

# Fonction pour extraire les informations d'un produit à partir de son URL
def extract_product_info(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraction du prix
    price_element = soup.find('span', itemprop='price')
    price = price_element['content'] if price_element else None

    # Extraction du nom
    name_element = soup.find('h1', class_='h1', itemprop='name')
    name = name_element.text if name_element else None

    # Extraction de la disponibilité
    availability_element = soup.find('div', id='stock_availability')
    availability = availability_element.text.strip() if availability_element else None

    # Extraction de la description
    description_element = soup.find('div', itemprop='description', class_='prodes')
    description = description_element.text.strip() if description_element else None
    
    # Extraction de l'URL de l'image du produit
    # Rechercher l'élément div avec la classe "product-cover"
    product_cover_element = soup.find('div', class_='product-cover')

    if product_cover_element:
        # Extraire l'URL de l'image à partir de la balise img
        image_element = product_cover_element.find('img', itemprop='image')
        image_url = image_element['src'] if image_element else None
    else:
        image_url = None


    product_info = {
    	"Image":image_url,
        "Prix": price,
        "Nom": name,
        "Disponibilité": availability,
        "Description": description
    }

    return product_info

if __name__ == "__main__":
    # Charger la liste des URLs depuis le fichier "products.json"
    with open("product_urls.json", "r", encoding="utf-8") as json_file:
        product_urls = json.load(json_file)

    # Liste pour stocker les informations des produits
    product_info_list = []

    # Parcourir les URLs et extraire les informations
    for product_url in product_urls:
        product_info = extract_product_info(product_url)
        if product_info:
            product_info_list.append(product_info)

    # Enregistrer les informations des produits dans un fichier JSON
    with open("product_info.json", "w", encoding="utf-8") as json_file:
        json.dump(product_info_list, json_file, ensure_ascii=False, indent=4)

