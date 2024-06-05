import requests
from bs4 import BeautifulSoup
import json
import csv

# Fonction pour extraire le prix d'une URL donnée
def extract_price(url, index, total):
    print(f"Traitement de l'URL {index}/{total}: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        price_div = soup.find("div", class_="product-info-price")
        stock_and_sku_div = soup.find("div", class_="product-info-stock-sku")
        overview_div = soup.find("div", class_="product attribute overview")
        image_div = soup.find("div", class_="carousel-inner")

        if price_div:
            special_price = price_div.find("span", class_="price").text
            old_price_element = price_div.find("span", {"data-price-type": "oldPrice"})
            old_price = old_price_element.text if old_price_element else None
            discount_element = price_div.find("span", class_="discount-price")
            discount = discount_element.text if discount_element else None
        else:
            special_price = old_price = discount = None

        if stock_and_sku_div:
            availability = stock_and_sku_div.find("div", class_="stock").text
            reference = stock_and_sku_div.find("div", class_="value", itemprop="sku").text
        else:
            availability = reference = None

        if overview_div:
            description = overview_div.find("div", class_="value", itemprop="description").text
        else:
            description = None

        if image_div:
            image = image_div.find("img", itemprop="image")["src"]
        else:
            image = None

        result = {
            "URL": url,
            "Prix spécial": special_price,
            "Ancien prix": old_price,
            "Réduction": discount,
            "Disponibilité": availability,
            "Référence": reference,
            "Description": description,
            "Image": image
        }
    else:
        result = {"URL": url, "Erreur": f"Échec de la requête HTTP. Statut de la réponse : {response.status_code}"}

    print(f"Terminé : {index}/{total}")
    return result


# Charger la liste d'URLs depuis le fichier CSV
url_list = []
with open("only-i7-13e-gen.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        url_list.extend(row)

total_urls = len(url_list)

# Extraire les prix de chaque URL et stocker les résultats dans une liste
results = []
for index, url in enumerate(url_list, start=1):
    result = extract_price(url, index, total_urls)
    results.append(result)

# Enregistrer les résultats dans un fichier JSON
with open("prices.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

print("Les résultats ont été enregistrés dans 'prices.json'.")

