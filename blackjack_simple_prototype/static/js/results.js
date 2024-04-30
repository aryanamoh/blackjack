$(document).ready(function() {
  $("#home_button").click(function() {
      window.location.href = "/";


  });

    $("#retake_button").click(function () {
        // Send AJAX request to the retake path
        $.ajax({
            type: "GET",
            url: "/retake",
            success: function (response) {
                // Handle success response if needed
                window.location.href= "/quiz/1";
            },
            error: function (xhr, status, error) {
                // Handle error response if needed
                console.error("Error sending retake request:", error);
            }
        });
    });

});
