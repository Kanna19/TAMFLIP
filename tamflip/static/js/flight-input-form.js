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

$( "button[id*='track']" ).on("click", function(){
    var button_id = $(this).attr('id');
    var num = button_id.substr(5);
    var input_id = ".hidden-input"+num;
    $(input_id).toggleClass("hidden-input");
});


var loadData = 10;
$(".moreButton").on("click",function(){
     for(var i = 1; i<=10; i++)
     {
        var n = (loadData+i).toString();
        if($(".hidden-box"+n).length == 0) {
          $(".moreButton").css('display','none');
          break;
        }
        $(".hidden-box"+n).removeClass("hidden-div");
        // $(".hidden-box"+n).css("background","red");
     }
     loadData = loadData+10;
});

// var $divs = $(".flight-box");

// $(".type42").on("click", function () {
//     var count = 0;
//     var alphabeticallyOrderedDivs = $divs.sort(function (a, b) {
//         return $(a).(".fbox1 .fbox3").text() > $(b).(".fbox1 .fbox3").text();
//         count = count + 1;
//     });
//     $("#track-details").html(alphabeticallyOrderedDivs);
//     alert{count};
// });

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

            // var text1 = $(a).find(".departTime").text();
            // var text2 = $(b).find(".departTime").text();
            //       console.log(text1)
            //       console.log(text2)
            // var num =  $(a).find(".departTime").text() > $(b).find(".departTime").text() ? 1: -1;
            //       console.log(num);
            //       return num;

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


$(".moreButton").on("click", function(){
  divArr = $(".flight-box")
  for (var i = numLoading; i < numLoading+10; i++) {
    $(divArr[i]).removeClass("hidden-div");
  }
  numLoading = numLoading + 10;
});
