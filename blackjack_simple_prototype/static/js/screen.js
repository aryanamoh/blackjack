let interaction = "h";
let action = "";
$(document).ready(function() {

  set_action();
  set_table();

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

function set_table() {
  // Reset table
  // $("#learn-table").empty();

  // $("#learn-table").append(`<img class="deck-card" src="/../static/assets/images/back.png" alt="Card Deck"></img>`);
  // $('#left-table-text').append(`<p>${text}</p>`);

  // Set text
  // TODO: middle text/text array
  // Reset table
  clear_table();
  // Set text
  $('#left-table-text').append(`<p>${text}</p>`);


  // Display dealer cards
  for (let i = 0; i < dealer.length; i++) {
    let class_name = "card-" + (i + 1);
    let url = dealer[i];
    $("#learn-table").append(`<img class=${class_name} src=${url}></img>`);
  }

  // Display player cards
  for (let i = 0; i < player.length; i++) {
    // index of player starts at 5 
    let class_name = ""
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
}

function next_screen_change() {
  // Check if next screen is new module
  let next_mod = next_screen[0] + 1;
  let next_lesson = next_screen[1] + 1;
  let next_sheet = next_screen[2] + 1;

  if (next_sheet == 0) {
    if (next_mod == 2) {
      window.location.href = '/lesson_complete/1';
    } else {
      window.location.href = '/lesson_complete/2';
    }
  } else {
    window.location.href = '/lesson/' + next_mod + '/' + next_lesson + '/' + next_sheet;
  }
}

$(".close").click(function() {
  $("#popup").fadeOut();
});
