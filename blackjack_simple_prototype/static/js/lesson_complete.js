
$(document).ready(function() {

  if (next_module_id == "Quiz" || next_module_id == 3 || next_module_id == "3") {
    $("#next_module_button").empty().text("CONTINUE TO QUIZ");
  } else {
    $("#next_module_button").empty().text("MOVE TO MODULE " + next_module_id);
  }

  $("#next_module_button").click(function() {

    if (next_module_id == "Quiz" || next_module_id == 3 || next_module_id == "3") {
      window.location.href = "/quiz_start"
    } else {
      window.location.href = `/lesson/${next_module_id}`
    }
  })

  $("#return_home_button").click(function() {
    window.location.href = "/";
  })
})
