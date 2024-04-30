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

   

  $("#back_button").click(function() {
      if (question.quiz_id >= 2) {
          var url = "/quiz/" + (parseInt(question.quiz_id) - 1);
          
          window.location.href = url;
      }
      else {
          window.location.href = "/quiz_start";
      }
      
  });

    $("#submit_button").click(function () {
        if ($("input[name='answer']:checked").length === 0) {
            // If no option is selected, display an error message
             $("#popup").fadeIn() 
            $("#popup_text").text("Please select an answer to continue.");
            return; // Exit the function to prevent further execution
        }
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
          if (response !== "Correct!") { $("#popup").fadeIn(); }
          else {
              $(".answerResult").css("display", "block");
          }
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

    var lockAnswersIfNeeded = function () {
        if (question.answersLocked) {
           
            $("input[type='radio']").attr("disabled", true);
            $("#submit_button").hide();
            $("#quiz_next_button").show();

            var clientResponse = question.client_response;
            console.log(clientResponse)
            // Find the index of the client response in questions.panswers
            var userResponseIndex = -1; // Initialize to -1 if not found
            $.each(question.panswers, function (index, answer) {
                if (answer === clientResponse) {
                    userResponseIndex = index;
                    return false; // Break out of the loop once found
                }
            });
            // Check the corresponding radio button
            $("input[name='answer']").eq(userResponseIndex).prop('checked', true);
        }
       
    };

    // Call the function to lock answers if needed upon page load
    lockAnswersIfNeeded();

  $("#submit_name").click(function() {
    var name = $("#new_name").val()
    saveName(name)

  })
})
