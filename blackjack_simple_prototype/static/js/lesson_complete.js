
$(document).ready(function(){

    if(Number.isInteger(lesson.next_module_id)){
        $("#next_module_button").empty().text("MOVE TO MODULE " + lesson.next_module_id);
    }
    else{
        $("#next_module_button").empty().text("START THE QUIZ");
    }

    $("#next_module_button").click(function(){
        if("{{lesson.next_module_id}}" == "Quiz"){
            window.location.href = "/quiz_start"
        }else{
            window.location.href = "/lesson/{{lesson.next_module_id}}/1"
        }
    })

    $("#return_home_button").click(function(){
        window.location.href = "/";
    })
})