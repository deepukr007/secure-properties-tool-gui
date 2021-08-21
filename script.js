`use strict`;



function stringClick() {
  debugger;
  document.getElementById("string").className = "card__string-on";
  document.getElementById("file").className = "card__file";
  document.getElementById("batch").className = "card__batch";


  // document.querySelector(".card__file").className = "card__file";
  // document.querySelector(".card__string").className = "card__string";
  // document.querySelector(".card__batch").className = "card__batch";
}

function fileClick() {
  document.getElementById("string").className = "card__string-off";
  document.getElementById("file").className = "card__file-on";
  document.getElementById("batch").className = "card__batch";
}

function batchClick() {
  document.getElementById("string").className = "card__string-off";
  document.getElementById("file").className = "card__file";
  document.getElementById("batch").className = "card__batch-on";


  // document.querySelector(".card__batch").classList.add = "card__batch-on";
  // document.querySelector(".card__batch").className = "card__batch-on";


  // document.querySelector(".card__file").classList.remove = "card__file";
  // document.querySelector(".card__file").classList.add = "off"
  // document.querySelector(".card__string").classList.remove = "card__string-off";
  // document.querySelector(".card__batch").className = "card__batch";
}


// const currentLocation = location.href;
// const menuItem = document.querySelectorAll(".card__heading--link");
// const menuLength = menuItem.length;
// console.log('menuLength');
// for (let i = 0; i < menuLength; i++) {
//   if (menuItemp[i].href == currentLocation) {
//     menuItem.className = "active";
//   }
// }