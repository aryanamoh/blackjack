let interaction = "N";

$(document).ready(function(){
    set_table();

    $("#next_button").click(function(){
        next_screen_change();
    });

    $(document).keydown(function(event) {
        if (event.key === 'H') {
            // Handle the key down event for H key
            next_screen_change();
        } else if (event.key === 'T') {
            // Handle the key down event for T key
            next_screen_change();
        } else if (event.key === 'S') {
            // Handle the key down event for S key
            next_screen_change();
        } else if (event.key === 'D') {
            // Handle the key down event for D key
            next_screen_change();
        }
    });
});

function set_table() {
    // Reset table
    // $("#learn-table").empty();
    $("#learn-table").append(`<img class="deck-card" src="/../static/assets/images/back.png" alt="Card Deck"></img>`);

    // Set text
    // TODO: middle text/text array
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
        if (player.length > 3 && i>1) {
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

function next_screen_change() {
    // Check if next screen is new module
    let next_mod = next_screen[0] ;
    let next_lesson = next_screen[1] ;
    let next_sheet = next_screen[2] ;
   
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