`use strict`;
function stringClick() {
  document.getElementById("string").className = "card__string-on";
  document.getElementById("file").className = "card__file";
}

function fileClick() {
  document.getElementById("string").className = "card__string-off";
  document.getElementById("file").className = "card__file-on";
}

function submitClick() {
  document.getElementById("output").className = "output__on"
}

function copyText() {
  debugger;
  var copyValue = document.getElementById("outputString");

  document.getElementById("outputString").className = "output__string-on";

  var copyString = copyValue.value
  // copyValue.select();
  // copyString.select();
  copyValue.focus();
  // copyValue.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyString);
  console.log(copyString);
  // document.execCommand("copy");
}

var value = document.getElementById("value").value;
var stringKey = document.getElementById("key").value;
var file = document.getElementById("File").value;
var stringAlgo = document.getElementsByName("stringAlgo").value;
var stringMode = document.getElementsByName("stringMode").value;





