// let current_lesson = lesson.text_array[0][0]
// let current_hands = lesson.media_array[0]
// let current_spotlight = lesson.text_array[0][1]

// $(document).ready(function(){

//     // Populate w/ initial content:
//     // First text blurb
//     displayText(current_lesson)

//     // First set of cards we want to display
//     displayCards(current_hands)

    

//     let pointer = 1

//     $("#next_button").click(function(){
//         if("{{lesson.next_lesson}}" == "end"){
//             window.location.href = "/lesson_complete/{{module_id}}"
//         }else{
//             window.location.href = "/lesson/{{module_id}}/{{lesson.next_lesson}}"
//         }
//     })
//     $("#back_button").click(function(){
//         if( ({{lesson.lesson_id}} - 1) < 1){
//             window.location.href = "/learn"
//         } else {
//             let previous_lesson_id = {{lesson.lesson_id}}  - 1
//             window.location.href = "/lesson/{{module_id}}/"+ previous_lesson_id
//         }
//     })
//     $("#next_lesson").click(function(){
        
//         // go through each index of the lesson.media_array & lesson.text_array
//         if(pointer < lesson.text_array.length){
            
//             // Text field is stored at index 0 
//             current_lesson = lesson.text_array[pointer][0]

//             // Location of spotlight is held at index 1

//             /*
//             TODO: need logic that maps player, dealer, 
//             text, player_dealer, player_sideways_dealer to corresponding
//             divs to highlight. Ie: if current_spotlight contains "player"
//             then highlight the specific div for the player's hands 

//             If you want we can get more specific, player_left or player_right,
//             let me know 

//             */
//             // stores the string with the divs that need to be highlighted
//             current_spotlight = lesson.text_array[pointer][1]

//             // grab the dealer & player's hands 
//             current_hands = lesson.media_array[pointer]
//             prev_hands = lesson.media_array[pointer-1]
            
//             displayCards(current_hands)

//             // update the lesson text html or text blurb 
//             displayText(current_lesson)               
    
//             // increment out pointer for the next time interaction is recorded 
//             pointer +=1 
//             console.log(current_lesson, current_hands, "Current_hands length: "+current_hands.length, "spotlight on: "+current_spotlight)
//         }else{
//             // TODO: 
//             // Highlight the next button when done displaying text & images 
//             $("#next_button").click();
//             console.log("no more text blurbs bub.")
//         }

//     })
// })