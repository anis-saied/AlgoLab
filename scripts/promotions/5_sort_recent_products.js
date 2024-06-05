// pour executer ce fichier : 
// node sort_recent_products.js

const fs = require('fs');

// Charger les données du fichier JSON
fs.readFile('filtered_recent_products_data.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Erreur lors de la lecture du fichier :', err);
    return;
  }

  try {
    const products = JSON.parse(data);

    // Trier les produits par prix (du plus bas au plus élevé)
    products.sort((a, b) => {
      const priceA = parseFloat(a['Prix spécial'].replace(' DT', '').replace(',', ''));
      const priceB = parseFloat(b['Prix spécial'].replace(' DT', '').replace(',', ''));
      return priceA - priceB;
    });

    // Enregistrer les produits triés dans un nouveau fichier JSON
    const outputFilename = 'sorted_filtered_recent_products.json';
    fs.writeFile(outputFilename, JSON.stringify(products, null, 4), (err) => {
      if (err) {
        console.error('Erreur lors de l\'enregistrement du fichier trié :', err);
        return;
      }
      console.log(`Les produits ont été triés par prix et enregistrés dans '${outputFilename}'.`);
    });
  } catch (e) {
    console.error('Erreur lors de l\'analyse des données JSON :', e);
  }
});

