// Skeleton javascript functions from people website 
// var displayNames = function(data){
//     //empty old data
//     $("#people_container").empty()

//     //insert all new data
//     $.each(data, function(i, datum){
//         var new_name= $("<div>"+datum["name"]+"</div>")
//         $("#people_container").append(new_name)
//     })
// }

var saveName = function(name){
    // var data_to_save = {"name": name}         
    // $.ajax({
    //     type: "POST",
    //     url: "add_name",                
    //     dataType : "json",
    //     contentType: "application/json; charset=utf-8",
    //     data : JSON.stringify(data_to_save),
    //     success: function(result){
    //         var all_data = result["data"]
    //         data = all_data
    //         displayNames(data)
    //     },
    //     error: function(request, status, error){
    //         console.log("Error");
    //         console.log(request)
    //         console.log(status)
    //         console.log(error)
    //     }
    // });
}

var saveStartTime = function(formattedTime, pathname){
    
    $.ajax({
        type: "POST",
        url: "/client",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify({formattedTime,pathname}),
        success: function(result){
            // do something with the result of this ajax call
            console.log(result)
        },
        error: function(request, status, error){
            // console.log("Error");
            // console.log(request)
            // console.log(status)
            // console.log(error)
        }
    });
}


$(document).ready(function(){

    // parse the start time into hours, minutes & seconds delimited by `:`
    let startTime = new Date();
    let hours = startTime.getHours().toString().padStart(2, '0');
    let minutes = startTime.getMinutes().toString().padStart(2, '0');
    let seconds = startTime.getSeconds().toString().padStart(2, '0');
    let formattedTime = `${hours}:${minutes}:${seconds}`;

    // send this information to our backend to be utilized later on
    saveStartTime(formattedTime, window.location.pathname);
    // Old skeleton code
    //when the page loads, display all the names
    // displayNames(data)                        

    // $("#submit_name").click(function(){                
    //     var name = $("#new_name").val()
    //     saveName(name)

    // })
})