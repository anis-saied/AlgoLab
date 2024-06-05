// pour executer ce fichier : 
// node filter_and_sort.js

const fs = require('fs');

// Lire le fichier JSON contenant les résultats précédents
fs.readFile('prices.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Erreur de lecture du fichier JSON:', err);
    return;
  }

  const results = JSON.parse(data);

  // Filtrer les produits disponibles, soldés et triés
  const filteredProducts = results.filter(product => {
    return (
      //product['Réduction'] !== null &&   // Vérifier s'il y a une réduction
      product['Disponibilité'] !== null &&  // Vérifier s'il y a une disponibilité
      //product['Disponibilité'].toLowerCase() !== 'en arrivage' // Exclure les produits "En arrivage"
    );
  });

  // Trier les produits soldés par réduction
  /*
  sfilteredProducts.sort((a, b) => {
    const discountA = parseFloat(a['Réduction'].replace('DT', '').replace(',', '').trim());
    const discountB = parseFloat(b['Réduction'].replace('DT', '').replace(',', '').trim());
    return discountB - discountA;
  });
  */

  // Enregistrer les produits soldés triés dans un autre fichier JSON
  filteredProducts.forEach(product => {
    // Ajouter l'image à chaque produit
    product['Image'] = product['Image'];
  });

  fs.writeFile('products.json', JSON.stringify(filteredProducts, null, 2), err => {
    if (err) {
      console.error('Erreur d\'écriture du fichier JSON :', err);
    } else {
      console.log('Les produits disponibles, soldés et triés ont été enregistrés dans "products.json".');
    }
  });
});

// Fonction pour extraire l'URL de l'image depuis l'URL de la page du produit
function getImageUrl(productUrl) {
  // Vous devez extraire l'URL de l'image à partir de la page du produit
  // Ici, vous pouvez ajouter votre code pour extraire l'URL de l'image en fonction de la structure de la page.
  // Retournez l'URL de l'image que vous avez extraite.
  return 'URL_DE_L_IMAGE';
}

