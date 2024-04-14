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
    displayNames(data)                        

    $("#submit_name").click(function(){                
        var name = $("#new_name").val()
        saveName(name)

    })
})