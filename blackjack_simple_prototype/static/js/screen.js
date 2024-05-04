let interaction = "h";
let action = "";
$(document).ready(function() {

  set_action();
  set_table(0, 0);

  $("#next_button").click(function() {
    next_screen_change();
  });

  $(document).keydown(function(event) {
    if (event.key === 'h' || event.key === 't' || event.key === 's' || event.key === 's') {
      console.log(event.key);
      handle_key_down(event.key);
    }
  });
});


function handle_key_down(key) {
  if (interaction != key) {
    $("#popup").fadeIn();
    $("#popup_text").text("Try again! We want to " + action + " here.");
  } else {
    next_screen_change();
  }
}

function set_action() {
  if (interaction == 'h') {
    action = "hit";
  } else if (interaction == 't') {
    action = "split";
  } else if (interaction == 's') {
    action = "stand";
  } else if (interaction == 'd') {
    action = "double";
  } else {
    action = "continue";
  }
}

function set_table(new_lesson, new_screen) {
  // Reset table
  // $("#learn-table").empty();

  // $("#learn-table").append(`<img class="deck-card" src="/../static/assets/images/back.png" alt="Card Deck"></img>`);
  // $('#left-table-text').append(`<p>${text}</p>`);

  // Set text
  // TODO: middle text/text array
  // Reset table
  clear_table();
  // Set text 

  lesson = scr[new_lesson][new_screen];
  spotlight = lesson.spotlight;
  dealer = lesson.media_array[0];
  player = lesson.media_array[1];
  text = lesson.text;
  next_screen = lesson.next_screen;
  $('#left-table-text').append(`<p>${text[0]}</p>`);
  $('#mid-table-text').append(`<p>${text[1]}</p>`);
  $('#bottom-table-text').append(`<p>${text[2]}</p>`);

  // Display dealer cards
  for (let i = 0; i < dealer.length; i++) {
    let class_name = "card-" + (i + 1);
    let url = dealer[i];
    $("#learn-table").append(`<img class=${class_name} src=${url}></img>`);
  }

  // Display player cards
  for (let i = 0; i < player.length; i++) {
    // index of player starts at 5 
    let class_name = "";
    if (player.length > 3 && i > 1) {
      class_name = "card-split-" + (i + 5);
    } else {
      class_name = "card-" + (i + 5);
    }

    let url = player[i];
    $("#learn-table").append(`<img class=${class_name} src=${url} alt="Playing Card"></img>`);
  }

  // Enable interactions
  if (interaction == 'N') {
    $("next_button").show()
  }
  else {
    $("next_button").hide()
  }
}

function clear_table() {
  $('img').remove();
  $("#learn-table").append(`<img class="deck-card" src="/../static/assets/images/back.png" alt="Card Deck"></img>`);
  $('#left-table-text').empty();
  $('#mid-table-text').empty();
  $('#bottom-table-text').empty();
}



function prev_screen_change() {
  let prev_mod = prev_screen[0] + 1;
  let prev_lesson = prev_screen[1] + 1;
  let prev_sheet = prev_screen[2] + 1;

  if (prev_mod < next_screen[0] + 1) {
    if (false && prev_mod == 1) {
      window.location.href = '/lesson_complete/1';
    } else if (false && prev_mod == 2) {
      window.location.href = '/lesson_complete/2';
    } else if (prev_mod == 0) {
      window.location.href = '/learn';
    }
  } else {
    set_table(prev_lesson - 1, prev_sheet - 1);
  }
}


function next_screen_change() {
  // Check if next screen is new module
  let next_mod = next_screen[0] + 1;
  let next_lesson = next_screen[1] + 1;
  let next_sheet = next_screen[2] + 1;

  if (next_sheet == 1 && next_lesson == 1) {
    if (next_mod == 2) {
      window.location.href = '/lesson_complete/1';
    } else if (next_mod == 3) {
      window.location.href = '/lesson_complete/2';
    }
  } else {
    set_table(next_lesson - 1, next_sheet - 1);
  }
}

$(".close").click(function() {
  $("#popup").fadeOut();
});
