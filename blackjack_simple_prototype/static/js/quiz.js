// Skeleton javascript functions from people website 
var displayNames = function(data){
    //empty old data
    $("#people_container").empty()

    //insert all new data
    $.each(data, function(i, datum){
        var new_name= $("<div>"+datum["name"]+"</div>")
        $("#people_container").append(new_name)
    })
}

var saveName = function(name){
    var data_to_save = {"name": name}         
    $.ajax({
        type: "POST",
        url: "add_name",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var all_data = result["data"]
            data = all_data
            displayNames(data)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function(){
    //when the page loads, display all the names
    //displayNames(data)                        
    
    $("#submit_button").click(function () {
        
        let answerIndex = $("input[name='answer']").index($("input[name='answer']:checked"));
        // Send the selected answer index to the server using AJAX
        $.ajax({
            type: "POST",
            url: "/answer",
            contentType: "application/json",
            data: JSON.stringify({ answerIndex: answerIndex, quizId: question.quiz_id }),
            success: function (response) {
                console.log(response);
                $("#quiz_next_button").show();
                // Optionally, you can redirect or display a message after submitting the answer
            },
            error: function (xhr, status, error) {
                console.error("Error submitting answer:", error);
            }
        });
    });

    $("#submit_name").click(function(){                
        var name = $("#new_name").val()
        saveName(name)

    })
})