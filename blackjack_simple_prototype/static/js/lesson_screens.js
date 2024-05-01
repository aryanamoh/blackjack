// let interaction = 'N';

// $(document).ready(function(){
//     $("#learn-table").empty();

//     $("#next_button").click(function(){
//         window.location.href = '/lesson/1/1/';
//     });

//     $(document).keydown(function(event) {
//         if (event.key === 'H') {
//             // Handle the key down event for H key
//             // Your code here
//         } else if (event.key === 'T') {
//             // Handle the key down event for T key
//             // Your code here
//         } else if (event.key === 'S') {
//             // Handle the key down event for S key
//             // Your code here
//         } else if (event.key === 'D') {
//             // Handle the key down event for D key
//             // Your code here
//         }
//     });
// });
    // let scr = {{screen|tojson}};
    // let spotlight = screen.spotlight;
    // let dealer = lesson.media_array[0];
    // let player = lesson.media_array[1];
    // let text = lesson.text_array;
 
    // <img class="card-1" src="{{ url_for('static', filename = 'assets/images/8Diamond.png') }}">
    // <img class="card-2" src="{{ url_for('static', filename = 'assets/images/8Diamond.png') }}"`</img>
 
    // wipe all contents on screeen to avoid overlapping w/ prev screen 
    // 

    // $("learn-table").append(`<img class="deck-card" src="/static/assets/image/back.png"></img>`);

    // $('.left-table-text').append(`<p>${text}</p>`);
 
    // for (let i = 0; i < dealer.length; i++) {
    //     let class_name = "card-" + (i + 1);
    //     let url = dealer[i];
    //     $("learn-table").append(`<img class=${class_name} src=${url}></img>`);
    // }

    // for (let i = 0; i < player.length; i++) {
    //     // index of player starts at 5 
    //     let class_name = "card-" + (i + 5);
    //     let url = dealer[i];
    //     $("learn-table").append(`<img class=${class_name} src=${url}></img>`);
    // }



// function next_screen() {
//     // Check if next screen is new module
//     let next_mod = next_screen[0] + 1;
//     let next_lesson = next_screen[1] + 1;
//     let next_sheet = next_screen[2] + 1;
   
//     if (next_sheet == 0) {
//         if (next_mod == 2) {
//             window.location.href = '/lesson_complete/1'
//         } else {
//             window.location.href = '/lesson_complete/2'
//         }
//     } else {

//     }
// }

// function set_table() {
//     // Reset table
//     $("learn-table").empty();
//     $("learn-table").append(`<img class="deck-card" src="../assets/images/back.png" alt="Card Deck"></img>`);

//     // Set text
//     // TODO: middle text/text array
//     $('.left-table-text').append(`<p>${text}</p>`);

//     // Display dealer cards
//     for (let i = 0; i < dealer.length; i++) {
//         let class_name = "card-" + (i + 1);
//         let url = dealer[i];
//         $("learn-table").append(`<img class=${class_name} src=${url}></img>`);
//     }

//     // Display player cards
//     for (let i = 0; i < player.length; i++) {
//         // index of player starts at 5 
//         let class_name = ""
//         if (player.length > 3 && i>1) {
//             class_name = "card-split-" + (i + 5);
//         } else {
//             class_name = "card-" + (i + 5);
//         }

//         let url = dealer[i];
//         $("learn-table").append(`<img class=${class_name} src=${url} alt="Playing Card"></img>`);
//     }

//     // Enable interactions
//     if (interaction == 'N') {
//         $("next_button").show()
//     }
//     else {
//         $("next_button").hide()
//     }
// }