
$(document).ready(function(){

    console.log(next_module_id);

    if(next_module_id == "Quiz"){
        $("#next_module_button").empty().text("CONTINUE");
    }else{
        $("#next_module_button").empty().text("MOVE TO MODULE " + next_module_id);
    }

    $("#next_module_button").click(function(){
        
        if(next_module_id == "Quiz"){
            window.location.href = "/quiz_start"
        }else{
            window.location.href = "/lesson/" + next_module_id + "/1"
        }
    })

    $("#return_home_button").click(function(){
        window.location.href = "/";
    })
})