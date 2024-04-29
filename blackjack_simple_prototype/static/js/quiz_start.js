$(document).ready(function () {
    // Function to handle button click event
    $("#startQuizButton").click(function () {
        // Perform AJAX call
        $.ajax({
            url: "/go_to_quiz",
            type: "GET",
            success: function (response) {
                // Parse the response
                var quizId = response;
                // Construct the URL
                if (quizId == "0") {
                    window.location.href = "/results"
                }
                else {
                    var url = "/quiz/" + quizId;
                    // Redirect the user
                    window.location.href = url;
                }
            }
        });
    });
});