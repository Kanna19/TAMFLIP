// $("body").on("click", function(){
  // $(this).css("background", "green");
// })


$(".type21").on("click", function(){
  $("#type2").text("Economy");
  $(".hiddenInput1").val("Economy");
});

$(".type22").on("click", function(){
  $("#type2").text("Premium Economy");
  $(".hiddenInput1").val("Premium Economy");
});

$(".type23").on("click", function(){
  $("#type2").text("Business");
  $(".hiddenInput1").val("Business");
});

$(".type24").on("click", function(){
  $("#type2").text("First Class");
  $(".hiddenInput1").val("First Class");
});

$(".type31").on("click", function(){
  $("#type3").text("Round Trip");
  $(".hiddenInput2").val("Round Trip");
  $("#returnDate").removeClass("info-21");
  $("#returnDate").addClass("info-22");
});

$(".type32").on("click", function(){
  $("#type3").text("One-way");
  $(".hiddenInput2").val("One way");
  $("#returnDate").addClass("info-21");
  $("#returnDate").removeClass("info-22");
});

$(".passenger").on("click", function(){
  var adlt = $(".adlt").val();
  var chld = $(".chld").val();
  var inft = $(".inft").val();
  var sum = parseInt(adlt, 10) + parseInt(chld, 10) + parseInt(inft, 10);

  $("#type1Num").text(sum);

  if(sum <= 1){
    $("#type1Txt").text("Passenger");
  }

  if(sum > 1){
    $("#type1Txt").text("Passengers");
  }
});

// $("#submit").on("click", function(){
//   $(".filter").removeClass("info-21");
// });
