import json

# Charger les informations des produits depuis le fichier JSON
with open("product_info.json", "r", encoding="utf-8") as json_file:
    product_info_list = json.load(json_file)

# Filtrer les produits en stock
products_in_stock = [product for product in product_info_list if ("En stock" in product["Disponibilité"])  \
                     or("Sur commande" in product["Disponibilité"]) ]

# Trier les produits par prix croissant
sorted_products = sorted(products_in_stock, key=lambda x: float(x["Prix"]))

# Remplacer la valeur de "Disponibilité" par "En stock"
for product in sorted_products:
    product["Disponibilité"] = "En stock"
    
# Enregistrer les produits triés dans un nouveau fichier JSON
output_file = "products.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(sorted_products, json_file, ensure_ascii=False, indent=4)

print(f"Les produits en stock triés par prix croissant ont été enregistrés dans {output_file}.")

