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

var saveName = function(name) {
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

var saveStartTime = function(formattedTime, pathname) {

  $.ajax({
    type: "POST",
    url: "/client",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({ formattedTime, pathname }),
    success: function(result) {
      // do something with the result of this ajax call
      console.log(result)
    },
    error: function(request, status, error) {
      // console.log("Error");
      // console.log(request)
      // console.log(status)
      // console.log(error)
    }
  });
}

// TODO: Change name of div to match Aryana UI 
var addPlayerCard = function(card) {
  $("#player_hand").append(
    '<div class="box left" id="player_right">' +
    '    <img class="lesson-img" src="' + card + '" alt="' + lesson.media_alt + '">' +
    '</div>'
  );
}

// TODO: Change name of div to match Aryana UI 
var addDealerCard = function(card) {

  $("#dealer_hand").append(
    '<div class="box left" id="dealer_right">' +
    '    <img class="lesson-img" src="' + card + '" alt="' + lesson.media_alt + '">' +
    '</div>'
  );
}

/*
PARAMS: current_lesson is just a string holding the text blurb
we have extracted from the array of text blurbs associted with each lesson
ACTION: wips the current div holding lesson text and inputs the current blurb
TODO: Change the name of the id if we are displaying the text in a different
div 
*/

var displayText = function(current_lesson) {
  $("#lesson_text").empty()
  $("#lesson_text").html(current_lesson)
}


/*
PARAMS: current_hands is an array of playing card image paths 
ACTION: wipes both the dealer & player's hands and displays the 
images currently associated with the text blurb being displayed 
TODO: Play with the order in which cards are displayed for more
interaction 

*/
var displayCards = function(dealer, player) {

  // clean out the div of previous cards 
  $("#dealer_hand").empty()
  $("#player_hand").empty()

  for (let i = 0; i < dealer.length; i++) {
    $("#dealer_hand").append(
      '<div class="box left" id="dealer_left">' +
      '    <img class="lesson-img" src="' + dealer[i] + '" alt="' + dealer[i] + '">' +
      '</div>'
    );
  }
  for (let i = 0; i < player.length; i++) {
    $("#player_hand").append(
      '<div class="box left" id="player_left">' +
      '    <img class="lesson-img" src="' + player[i] + '" alt="' + player[i] + '">' +
      '</div>'
    );
  }
  return;
  // add the current playing cards needed 

  // check if we only need 4 divs to hold the card images
  if (current_hands.length > 4) {

    // tells us where in the spotlight string these strings are found 
    let index_player = current_spotlight.indexOf("player");
    let index_dealer = current_spotlight.indexOf("dealer");

    // flags to prevent duplicate hitting
    let player_added = 0
    let dealer_added = 0

    // we need to add more divs to either the dealer's hand 
    // or player's hand: stored in current_spotlight
    // current_spotlight can equal:
    // player, dealer, player_dealer, player_sideways_dealer
    for (let i = 4; i < current_hands.length; i++) {

      let card = current_hands[i]
      // TODO: figure out logic for when we need to add a specific 
      // card to dealer and a card to player but they all together
      // in data model 

      // need to add cards to both dealer & player's hands
      if (index_player !== -1 & index_dealer !== -1) {

        // if player comes first in the spotlight string
        // and hasn't been added, then add its card
        if (index_player < index_dealer & player_added != 1) {

          console.log("Need to add player first: " + current_hands[i] + " " + current_spotlight + " player added?: " + player_added);
          addPlayerCard(card);
          player_added += 1;

        }

        // if dealer comes first, then add it to its div first
        else if (index_dealer < index_player && dealer_added !== 1) {
          console.log("dealer added, before +=1: " + dealer_added);
          addDealerCard(card);
          dealer_added += 1;
          console.log("Need to add dealer first: " + current_hands[i] + " " + current_spotlight + " dealer added?: " + dealer_added);

        }

        // if player comes first but dealer hasn't been added yet
        // add it after the player 
        else if (index_player < index_dealer & player_added == 1) {
          console.log("Need to add dealer after player: " + current_hands[i] + " " + current_spotlight + " player added?: " + player_added)
          addDealerCard(card)
          dealer_added += 1;

        }

        // if dealers comes first but player hasn't been added yet
        // add it after the dealer 
        else if (index_dealer < index_player & dealer_added == 1) {
          console.log("Need to add player after dealer: " + current_hands[i] + " " + current_spotlight + " dealer added?: " + dealer_added)
          addPlayerCard(card)
          player_added += 1;

        }


      } else {

        // if only adding a player card
        if (index_player !== -1) {
          console.log("Need to add a solo player div for card: " + current_hands[i])

          // add the card to the player's hand 
          // $("#player_hand").append(
          //     '<div class="box left" id="player_right">' +
          //     '    <img class="lesson-img" src="' + current_hands[i] + '" alt="' + lesson.media_alt + '">' +
          //     '</div>'
          // );
          addPlayerCard(current_hands[i])
        }

        // if only adding a dealer 
        else if (index_dealer !== -1) {
          console.log("Need to add a solo dealer div for card: " + current_hands[i])

          // add the card to the dealer's hand 
          // $("#dealer_hand").append(
          //     '<div class="box left" id="dealer_right">' +
          //     '    <img class="lesson-img" src="' + current_hands[i] + '" alt="' + lesson.media_alt + '">' +
          //     '</div>'
          // );
          addDealerCard(current_hands[i])
        }

      }

    }

  }
}



$(document).ready(function() {

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
