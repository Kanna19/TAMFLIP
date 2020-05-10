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

$("#traDate").change(function(){
  if($(".errorDiv1").hasClass("hideDiv1") == false){
      $(".errorDiv1").addClass("hideDiv1");
  }
});

$("#reDate").change(function(){
  if($(".errorDiv1").hasClass("hideDiv1") == false){
      $(".errorDiv1").addClass("hideDiv1");
  }
});




$(".button1").on("click", function(event){
  var date1 = $("#traDate").val();
  var date2 = $("#reDate").val();

  var fromLoc = $("#fromLoc").val();
  var toLoc = $("#toLoc").val();

  var trip = $("#type3").text();

  // if(fromLoc == "" || toLoc == ""){
  //   $(".errorDiv3").removeClass("hideDiv3");
  //   event.preventDefault();
  // }
  //
  // if(date1 < today || date2 < today){
  //   $(".errorDiv4").removeClass("hideDiv4");
  //   event.preventDefault();
  // }

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

icon1 = $(".type41").find("i");
icon2 = $(".type42").find("i");
icon3 = $(".type43").find("i");
icon4 = $(".type44").find("i");
icon5 = $(".type45").find("i");
icon6 = $(".type46").find("i");
icon7 = $(".type47").find("i");


var numLoading = 0;
$(".type41").on("click", function(){
  icon1.addClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");

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

  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});


$(".type42").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.addClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");

  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".fbox3").text() > $(b).find(".fbox3").text() ? 1: -1;
      })
  $("#track-details").append(divArr);
  $(divArr).addClass("hidden-div");
  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});


$(".type43").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.addClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");

  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".departTime").text() > $(b).find(".departTime").text() ? 1: -1;
      })
  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});

var len = 0;
divArr = $(".flight-box")
len = divArr.length;

$(".type44").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.addClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");

  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".arrivalTime").text() > $(b).find(".arrivalTime").text() ? 1: -1;
      })

  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});

$(".type45").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.addClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");


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

  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});

$(".moreButton").on("click", function(){
  divArr = $(".flight-box")
  if(numLoading == 0){
    numLoading = 10;
  }

  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }

  numLoading = numLoading + 10;
    if(numLoading >= len){
    $(".noResults1").removeClass("hideResult");
    $(".moreButton").addClass("hideResult");
  }
});

$(".type46").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.addClass("fa fa-hand-o-left");
  icon7.removeClass("fa fa-hand-o-left");

  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".departTime").text() > $(b).find(".departTime").text() ? -1: 1;
      })

  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});

$(".type47").on("click", function(){
  icon1.removeClass("fa fa-hand-o-left");
  icon2.removeClass("fa fa-hand-o-left");
  icon3.removeClass("fa fa-hand-o-left");
  icon4.removeClass("fa fa-hand-o-left");
  icon5.removeClass("fa fa-hand-o-left");
  icon6.removeClass("fa fa-hand-o-left");
  icon7.addClass("fa fa-hand-o-left");

  divArr = $(".flight-box")
  divArr.sort(function(a, b) {
          return $(a).find(".arrivalTime").text() > $(b).find(".arrivalTime").text() ? -1: 1;
      })

  $(divArr).addClass("hidden-div");
  $("#track-details").append(divArr);
  var j=0;
  for (var i = 0; i < numLoading+10; ) {

    if(j >= divArr.length){
      break;
    }

    if(filterValue(j)){
      i++;
      $(divArr[j]).removeClass("hidden-div");
    }
    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;
  }
});

function filterValue(i){
    divArr = $(".flight-box");

    var x = $(".rangeInput1").val();
    var y = $(".rangeInput2").val();

    num1 = parseInt(x, 10);
    num2 = parseInt(y, 10);

    var val1 = parseInt($(divArr[i]).find(".price").text(), 10);
    var val2 = parseInt($(divArr[i]).find(".numOfStops").text(), 10);

    console.log("num1 = "+num1);
    console.log("num2 = "+num2);
    console.log("val1 = "+val1);
    console.log("val2 = "+val2);

    if(val1 > num1 || val2 > num2){
      return false;
    }
    return true;
}


$(".filterButton").on("click", function(){
  divArr = $(".flight-box");
  var l = divArr.length;

  var j = 0;

  if(numLoading == 0){
    numLoading = numLoading + 10;
  }

  for(var i=0; i<numLoading;){
    if(j >= divArr.length){
      if(i == 0){
        $(".noResults1").removeClass("hideResult");
        $(".moreButton").addClass("hideResult");
      }
      break;
    }

    if(filterValue(j)){
      $(divArr[j]).removeClass("hidden-div");
      i++;
    }

    else{
      $(divArr[j]).addClass("hidden-div");
    }
    j++;

    console.log("i = "+i);
    console.log("j = "+j);

  }
  if(j < divArr.length){
    $(".noResults1").addClass("hideResult");
    $(".moreButton").removeClass("hideResult");
  }
  if(numLoading == 10){
    numLoading = 0;
  }
});


// Render details without page reload, trial

$("input[id*='track-submit']").click(function(event){
    // Prevent redirection with AJAX for contact form
    var form = $('#track-details');
    var form_id = 'track-details';
    var url = form.prop('action');
    var type = form.prop('method');
    var formData = getContactFormData(form_id);

    $(this).closest('form').find("input[type=email], textarea").val("");

    // submit form via AJAX
    send_form(form, form_id, url, type, modular_ajax, formData);
});

function getContactFormData(form) {
    // creates a FormData object and adds chips text
    var formData = new FormData(document.getElementById(form));
    for (var [key, value] of formData.entries()) { console.log('formData', key, value);}
    return formData
}

// need to handle for errors
function send_form(form, form_id, url, type, inner_ajax, formData) {
    event.preventDefault();
    // inner AJAX call
    inner_ajax(url, type, formData);
}

function modular_ajax(url, type, formData) {
    // Most simple modular AJAX building block
    $.ajax({
        url: url,
        type: type,
        data: formData,
        processData: false,
        contentType: false,
        success: function ( data ){
           // response from Flask contains elements
              tracked_flight = data.tracked_flight;
              entry_there = data.entry_there;
        },
    }).done(function() {
      // Make changes only for non-empty response
        if(tracked_flight !='-1'){
          if(!($('#tracksu'+tracked_flight).hasClass("hidden-tick"))){
            $('#tracksu'+tracked_flight).addClass("hidden-tick");
          }
          if(!($('#tracksb'+tracked_flight).hasClass("hidden-tick"))){
            $('#tracksb'+tracked_flight).addClass("hidden-tick");
          }
          if(entry_there){
              $('#tracksu'+tracked_flight).removeClass("hidden-tick");
          }
          else{
              $('#tracksb'+tracked_flight).removeClass("hidden-tick");
          }
        }
    });
};

function updateRangeInput1(elem) {
    $(".rangeInput1").val($(elem).val());
}

function updateRangeInput2(elem) {
    $(".rangeInput2").val($(elem).val());
}
