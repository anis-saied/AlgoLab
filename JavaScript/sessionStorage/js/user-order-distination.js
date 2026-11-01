let user = {};

function get_item(){
    user = JSON.parse(sessionStorage.getItem('user'));

    console.log(user);
    const firstNameElement = document.getElementById("firstName");
    if(firstNameElement)
        firstNameElement.innerHTML = user.firstName;

    const lastNameElement = document.getElementById("lastName");
    if(lastNameElement)
        lastNameElement.innerHTML = user.lastName;
   
    const address = document.getElementById("address");
    if(address)
        address.innerHTML = user.address;
   
    const city = document.getElementById("city");
    if(city)
        city.innerHTML = user.city;
}