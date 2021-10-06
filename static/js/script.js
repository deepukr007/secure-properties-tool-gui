`use strict`;
function optionValue() {
  var OptionValue = document.querySelector("#option").value;
  document.querySelector('#submit').textContent = OptionValue;
}


function stringClick() {
  document.getElementById("string").className = "card__string-on";
  document.getElementById("file").className = "card__file";
}

function fileClick() {
  document.getElementById("string").className = "card__string-off";
  document.getElementById("file").className = "card__file-on";
}


function copyText() {
  var copyValue = document.getElementById("outputString");
  var copyString = copyValue.innerHTML.trim();
  navigator.clipboard.writeText(copyString);
  document.getElementById("outputString").className = "output__string-on";
  setTimeout(remove, 800);
}

function remove() {
  document.getElementById("outputString").className = "output__string";
}



$(document).ready(function () {
  $(".card__input").focus(function () {
    $(this).css("box-shadow", "2px 2px 4px #666");
  })
  $(".card__input").blur(function () {
    $(this).css("box-shadow", "none");
  })

  $(".card__input").blur(function () {
    var text = $(this).val().length;
    if (text < 2) {
      $(this).css("box-shadow", "2px 2px 4px #811");
    }
    else {
      $(this).css("box-shadow", "2px 2px 4px #181");
    }

  })
});