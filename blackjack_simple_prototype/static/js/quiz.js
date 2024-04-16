// Skeleton javascript functions from people website 
var displayNames = function(data) {
  //empty old data
  $("#people_container").empty()

  //insert all new data
  $.each(data, function(i, datum) {
    var new_name = $("<div>" + datum["name"] + "</div>")
    $("#people_container").append(new_name)
  })
}

var saveName = function(name) {
  var data_to_save = { "name": name }
  $.ajax({
    type: "POST",
    url: "add_name",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      var all_data = result["data"]
      data = all_data
      displayNames(data)
    },
    error: function(request, status, error) {
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
    }
  });
}


$(document).ready(function() {
  //when the page loads, display all the names
  //displayNames(data)                        

  $("#submit_button").click(function() {
    $("input[type='radio']").attr("disabled", true);
    let answerIndex = $("input[name='answer']").index($("input[name='answer']:checked"));
    let leave = false;
    // Send the selected answer index to the server using AJAX
    $.ajax({
      type: "POST",
      url: "/answer",
      contentType: "application/json",
      data: JSON.stringify({ answerIndex: answerIndex, quizId: question.quiz_id }),
      success: function(response) {
        console.log(response);
        $("#quiz_next_button").show();
        $("#submit_button").hide();

        $("#popup_text").text(response);
        if (question.next_question == "end") {
          $(".progress-bar").css("width", "100%");
          $(".progress-bar").text("100%");
        }
        else {
          let currentWidth = $(".progress-bar").width();
          console.log(currentWidth)
          let newWidth = currentWidth + 111.594; // 10% increase

          $(".progress-bar").width(newWidth);
          let currentWidthText = parseInt($(".progress-bar").text());
          $(".progress-bar").text(currentWidthText + 10 + "%");
        }
        // Optionally, you can redirect or display a message after submitting the answer

      },
      error: function(xhr, status, error) {
        console.error("Error submitting answer:", error);
      }
    });

    $("#popup").fadeIn();
    if (leave) { window.location.href = "/results"; }
  });

  $(".close").click(function() {
    $("#popup").fadeOut();
  });

  if (question.next_question == "end") {
    $("#quiz_next_button").text("View Results")
  }
  $("#quiz_next_button").click(function() {
    if (question.next_question == "end") {
      window.location.href = "/results"
    } else {

      window.location.href = "/quiz/" + question.next_question
    }
  })


  $("#submit_name").click(function() {
    var name = $("#new_name").val()
    saveName(name)

  })
})
