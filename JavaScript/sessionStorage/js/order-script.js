function init() {
  editOrder();
  const table = document.getElementById("order");

  table.addEventListener("focusout", (event) => {
    clearSelectedRows();
  });
}

function doSetItem() {
  var ref = document.getElementById("reference");
  var qte = document.getElementById("quantity");

  sessionStorage.setItem(ref.value, qte.value);

  ref.value = "";
  qte.value = "";

  editOrder();
}

function editOrder() {
  var key = "";
  var orderLines = "";
  for (let index = 0; index < sessionStorage.length; index++) {
    key = sessionStorage.key(index);
    let value = sessionStorage.getItem(key);
    orderLines += `<tr data-value = '${key}' onclick="editOrderLine('${key}')">
            <td>${key}</td>
            <td>${value}</td>
            <td>
              <span class="delete" onclick="deleteOrderLine('${key}')">&#x2717;</span>
              <span class="edit" onclick="editOrderLine('${key}')">&#x270E;</span>
            </td>
        </tr>`;
  }
  document.getElementsByTagName("tbody")[0].innerHTML = orderLines;
  if (sessionStorage.length == 0) toggleClearButton("hide");
}

function toggleClearButton(value) {
  const clearBtn = document.querySelector(
    "input[type='button'][value='clear']",
  );
  if (clearBtn)
    if (value == "hide") clearBtn.classList.add("hidden");
    else clearBtn.classList.remove("hidden");
}
function deleteOrderLine(key) {
  let response = confirm(
    `Voulez-vous supprimer le produit '${key}' de votre commande ?`,
  );

  if (response) {
    sessionStorage.removeItem(key);
    editOrder();
  }
}

function editOrderLine(key) {
  clearSelectedRows();
  let quantity = sessionStorage.getItem(key);
  document.getElementById("reference").value = key;
  document.getElementById("quantity").value = quantity;
  const row = document.querySelector(`tr[data-value='${key}']`);
  if (row) {
    row.classList.add("selected-row");
  }
}

function clearOrder() {
  sessionStorage.clear();
  editOrder();
}
/* utils funtions */
function clearSelectedRows() {
  const rows = document.querySelectorAll("tbody tr");
  if (rows && rows.length > 0) {
    rows.forEach((row) => row.classList.remove("selected-row"));
  }
}

function clearForm() {
  document.getElementById("reference").value = "";
  document.getElementById("quantity").value = "";
  clearSelectedRows();
}
