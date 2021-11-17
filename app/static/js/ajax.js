

$(document).ready(function () {


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
    event.stopImmediatePropagation(); //To prevent triggering the function twice
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