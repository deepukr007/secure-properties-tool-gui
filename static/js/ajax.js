

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

  $("#stringForm").submit(function (event) {
    var value = $("#value").val();
    var key = $("#key").val();
    var algorithm = $("input[name='stringAlgo']:checked").val();
    var mode = $("input[name='stringMode']:checked").val();
    var OptionValue = $("#option :selected").val();


    var url = OptionValue;
    $.post(url,
      {
        value,
        key,
        algorithm,
        mode
      },
      function (data) {
        $('#outputString').text(data);
      });
    $("#output").addClass("output__on");
    event.preventDefault();


  })
  // $("#fileForm").submit(function (event) {

  //   var OptionValue = $("#option :selected").val();
  //   var fileName = $("#File").val();
  //   var fileKey = $("#keyFile").val();
  //   var algo = $("input[name='file']:checked").val();
  //   var mode = $("input[name='fileMode']:checked").val();

  //   console.log(OptionValue);
  //   console.log(fileName);
  //   console.log(fileKey);
  //   console.log(algo);
  //   console.log(mode);



  //   $("#output").addClass("output__on");
  //   event.preventDefault();


  // })



});