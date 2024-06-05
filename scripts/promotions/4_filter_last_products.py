import json

# Charger les données depuis le fichier "recent_products_data.json"
with open("recent_products_data.json", "r", encoding="utf-8") as input_file:
    product_data = json.load(input_file)

# Filtrer les produits soldés, disponibles, en stock et avec "Ancien prix" non nul
filtered_products = [product for product in product_data if
                    product.get("Prix spécial") and
                    product.get("Disponibilité") and
                    "en stock" in product.get("Disponibilité").lower() and
                    product.get("Ancien prix")]

# Enregistrer les produits filtrés dans un nouveau fichier JSON
output_file = "filtered_recent_products_data.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(filtered_products, json_file, ensure_ascii=False, indent=4)

print(f"Les produits soldés, disponibles, en stock et avec 'Ancien prix' non nul ont été filtrés et enregistrés dans '{output_file}'.")

