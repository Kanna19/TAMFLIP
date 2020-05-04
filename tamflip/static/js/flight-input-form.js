// $("body").on("click", function(){
  // $(this).css("background", "green");
// })


$(".type21").on("click", function(){
  $("#type2").text("Economy");
  $(".hiddenInput").val("Economy");
});

$(".type22").on("click", function(){
  $("#type2").text("Premium Economy");
  $(".hiddenInput").val("Premium Economy");
});

$(".type23").on("click", function(){
  $("#type2").text("Business");
  $(".hiddenInput").val("Business");
});

$(".type24").on("click", function(){
  $("#type2").text("First Class");
  $(".hiddenInput").val("First Class");
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
