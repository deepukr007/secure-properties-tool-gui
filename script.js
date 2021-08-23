`use strict`;
function stringClick() {
  document.getElementById("string").className = "card__string-on";
  document.getElementById("file").className = "card__file";
}

function fileClick() {
  document.getElementById("string").className = "card__string-off";
  document.getElementById("file").className = "card__file-on";
}

var value = document.getElementById("value").value;
var stringKey = document.getElementById("key").value;
var file = document.getElementById("File").value;





