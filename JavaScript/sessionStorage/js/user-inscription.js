let user = {};
let form = {};

// Lancer l'initialisation dès que la page est chargée
window.addEventListener('DOMContentLoaded', init);

function init() {

  // Récupérer les éléments du formulaire
  form.firstName = document.getElementById("firstName");
  form.lastName = document.getElementById("lastName");
  form.city = document.getElementById("city");
  form.address = document.getElementById("address");

  // Remplir le formulaire si des données existent déjà
  fillForm();

  // Ajouter les écouteurs "blur" proprement avec une fonction réutilisable
  const fields = ["firstName", "lastName", "city", "address"];
  
  fields.forEach(filed => {
    if(form[filed]){
        form[filed].addEventListener("blur", function(){
            user[filed] = form[filed]?.value;
            sessionStorage.setItem('user', JSON.stringify(user));
        })
    }
  });
}

function fillForm() {
  const savedUser = sessionStorage.getItem("user");
  if (savedUser) {
    user = JSON.parse(savedUser);
    if (form.firstName && user.firstName) form.firstName.value = user.firstName;
    if (form.lastName && user.lastName) form.lastName.value = user.lastName;
    if (form.city && user.city) form.city.value = user.city;
    if (form.address && user.address) form.address.value = user.address;
  }
}
