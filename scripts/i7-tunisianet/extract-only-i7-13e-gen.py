import requests
from bs4 import BeautifulSoup
import json

# Lien vers le sitemap XML
sitemap_url = "https://www.tunisianet.com.tn/sitemap.xml"

# Mot-clé à rechercher dans l'URL
keyword = "i7-13e-gen"

# Liste pour stocker les URL des produits
product_urls = []

# Fonction pour extraire les liens des produits
def extract_product_links(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.text, 'xml')

    # Trouver tous les liens dans le sitemap XML
    for loc in soup.find_all('loc'):
        url = loc.text
        if keyword in url:
            product_urls.append(url)

if __name__ == "__main__":
    extract_product_links(sitemap_url)

    # Enregistrer les URL des produits dans un fichier JSON
    with open("product_urls.json", "w", encoding="utf-8") as json_file:
        json.dump(product_urls, json_file, ensure_ascii=False, indent=4)

