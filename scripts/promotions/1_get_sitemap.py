import requests

# URL du fichier sitemap à télécharger
sitemap_url = "https://www.mytek.tn/media/sitemap/sitemap.xml"

# Chemin local où vous souhaitez enregistrer le fichier
local_file_path = "sitemap.xml"

try:
    # Effectuez une requête GET pour télécharger le fichier
    response = requests.get(sitemap_url)

    # Vérifiez si la requête a réussi (code de statut HTTP 200)
    if response.status_code == 200:
        # Ouvrez un fichier local en mode écriture binaire
        with open(local_file_path, "wb") as local_file:
            # Écrivez le contenu du fichier téléchargé dans le fichier local
            local_file.write(response.content)
        
        print(f"Fichier '{local_file_path}' a été téléchargé et enregistré avec succès.")
    else:
        print(f"Échec de la requête HTTP. Statut de la réponse : {response.status_code}")

except requests.RequestException as e:
    print(f"Une erreur s'est produite lors de la requête : {e}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

