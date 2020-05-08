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
  if($(".errorDiv1").hasClass("hideDiv1") == false){
      $(".errorDiv1").addClass("hideDiv1");
  }
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

$( "button[id*='track']" ).on("click", function(){
    var button_id = $(this).attr('id');
    var num = button_id.substr(5);
    var input_id = ".hidden-input"+num;
    $(input_id).toggleClass("hidden-input");
});

$("#fromLoc").change(function(){
  if($(".errorDiv2").hasClass("hideDiv2") == false){
      $(".errorDiv2").addClass("hideDiv2");
  }
});

$("#toLoc").change(function(){
  if($(".errorDiv2").hasClass("hideDiv2") == false){
      $(".errorDiv2").addClass("hideDiv2");
  }
});

$(".button1").on("click", function(event){
  var date1 = $("#traDate").val();
  var date2 = $("#reDate").val();

  var fromLoc = $("#fromLoc").val();
  var toLoc = $("#toLoc").val();

  var trip = $("#type3").text();

  if(trip == "Round Trip"){
    if(date2 < date1 && fromLoc == toLoc){
      $(".errorDiv1").removeClass("hideDiv1");
      if(fromLoc != ""){
        $(".errorDiv2").removeClass("hideDiv2");
      }
      event.preventDefault();
    }

    else if (date2 < date1 && fromLoc != toLoc) {
      $(".errorDiv1").removeClass("hideDiv1");
      $(".errorDiv2").addClass("hideDiv2");
      event.preventDefault();
    }

    else if (fromLoc == toLoc && date2 >= date1) {
      if(fromLoc != ""){
        $(".errorDiv2").removeClass("hideDiv2");
      }
      $(".errorDiv1").addClass("hideDiv1");
      event.preventDefault();
    }

    else{
      $(".errorDiv1").addClass("hideDiv1");
      $(".errorDiv2").addClass("hideDiv2");
    }
  }
  else{
    if(fromLoc == toLoc){
      if(fromLoc != ""){
        $(".errorDiv2").removeClass("hideDiv2");
      }
      $(".errorDiv1").addClass("hideDiv1");
      event.preventDefault();
    }
    else{
      $(".errorDiv2").addClass("hideDiv2");
      $(".errorDiv1").addClass("hideDiv1");
    }
  }
});

var numLoading = 0;
$(".type41").on("click", function(){
  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          var x =  $(a).find(".price").text();
          var y =  $(b).find(".price").text();
          num1 = parseInt(x, 10);
          num2 = parseInt(y, 10);
          return num1 > num2 ? 1: -1;
      })
  $("#track-details").append(divArr);
  $(divArr).addClass("hidden-div");

  for (var i = 0; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
});


$(".type42").on("click", function(){
  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".fbox3").text() > $(b).find(".fbox3").text() ? 1: -1;
      })
  $("#track-details").append(divArr);
  $(divArr).addClass("hidden-div");
  for (var i = 0; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
});


$(".type43").on("click", function(){
  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".departTime").text() > $(b).find(".departTime").text() ? 1: -1;
      })
  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  for (var i = 0; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
});

var len = 0;
divArr = $(".flight-box")
len = divArr.length;

$(".type44").on("click", function(){
  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".arrivalTime").text() > $(b).find(".arrivalTime").text() ? 1: -1;
      })

  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  for (var i = 0; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
});

$(".type45").on("click", function(){
  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          var x =  $(a).find(".numOfStops").text();
          var y =  $(b).find(".numOfStops").text();
          num1 = parseInt(x, 10);
          num2 = parseInt(y, 10);
          return num1 > num2 ? 1: -1;
      })
  $("#track-details").append(divArr);
  $(divArr).addClass("hidden-div");

  for (var i = 0; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
});

$(".moreButton").on("click", function(){
  divArr = $(".flight-box")
  if(numLoading == 0){
    numLoading = 10;
  }
  for (var i = numLoading; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
  numLoading = numLoading + 10;
  if(numLoading >= len){
    $(".noResults1").removeClass("hideResult");
    $(".moreButton").addClass("hideResult");
  }
});

// var loadData = 10;
// $(".moreButton").on("click",function(){
//      for(var i = 1; i<=10; i++)
//      {
//         var n = (loadData+i).toString();
//         if($(".hidden-box"+n).length == 0) {
//           $(".moreButton").css('display','none');
//           break;
//         }
//         $(".hidden-box"+n).removeClass("hidden-div");
//      }
//      loadData = loadData+10;
// });



var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
 if(dd<10){
        dd='0'+dd
    }
    if(mm<10){
        mm='0'+mm
    }

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("traDate").setAttribute("min", today);
document.getElementById("reDate").setAttribute("min", today);
