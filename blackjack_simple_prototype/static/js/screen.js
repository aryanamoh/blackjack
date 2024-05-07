let interaction = "n";
let action = "";
let dealtCardClass = "";
let dealResult = {};
let dealerID = "";
var count = 0;
let counter = 0;
var cardSetCount = 0;
var screenStates = []; // Array to store current screen states
var initialScreenStates = []; // Array to store initial screen states

$(document).ready(function() {
    
    dealer = lesson.media_array;
    set_action();
    set_table(0, 0);
    dealResult = dealCards(dealer);
    dealtCardClass = dealResult.cardSetClass;
    dealerID = dealResult.uniqueId;
    playerSplit = dealResult.playerSplit;

    // Back button kicks back to module selection
    $("#back_button").click(function () {

      window.location.href = '/learn';
      // rewind(); // Restore previous screen state
      // Existing code...

    });
    
  $("#next_button").click(function() {
      
      next_screen_change();
      dealer = lesson.media_array;
      
      module_interactions = lesson.lesson_interaction;
      interaction = lesson.interaction.toLowerCase();
      console.log(module_interactions)
      console.log(interaction)
      console.log(dealtCardClass);
      
     
      
      if (module_interactions[0] == "Discard") {
         
          discardCards(dealtCardClass);
      }
      if (module_interactions[0] == "RemoveHit") {
          let hitCard = $("#hit" + count);
          hitCard.css("transition", "transform 1s ease-in-out");
          hitCard.css("transform", "translate(800px, 20px)");
          
      }

      if (module_interactions[0] == "Deal" || module_interactions[1] == "Deal") {
          
          dealResult = dealCards(dealer);
          dealtCardClass = dealResult.cardSetClass;
          dealerID = dealResult.uniqueId
          playerSplit = dealResult.playerSplit;
      }
      if (module_interactions[0] == "Reveal" || module_interactions[1] == "Reveal") {
          
          let dealerCard = $("#" + dealerID);
          
          dealerCard.css("opacity", 0);
          if (module_interactions[0] == "Reveal") {
              setTimeout(() => {
                  dealerCard.attr("src", dealer[4]);
                  dealerCard.css("opacity", 1);
              }, 10);
          }
          else {
              setTimeout(() => {
                  dealerCard.attr("src", dealer[6]);
                  dealerCard.css("opacity", 1);
              }, 10);
          }
      }
      if (module_interactions[0] == "DealerHit") {
          count++;
          var $image = $("<img>", { "class": "cards " + dealtCardClass, "id": "hit" + count, "src": dealer[4] });
          $("#learn-table").append($image);
          setTimeout(function () {
              let hitCard = $("#hit" + count);
              hitCard.css("transition", "transform 1s ease-in-out");
              hitCard.css("transform", "translate(600px, 20px)");
          }, 100);
      }
      if (module_interactions[0] == "SplitHit") {
          console.log("HERE!")
          count++;
          var $image = $("<img>", { "class": "cards " + dealtCardClass, "id": "hit" + count, "src": dealer[4] });
          var $image2 = $("<img>", { "class": "cards " + dealtCardClass, "id": "splithit" + count, "src": dealer[5] });
          $("#learn-table").append($image);
          $("#learn-table").append($image2);
          setTimeout(function () {
              let hitCard = $("#hit" + count);
              let splitHitCard = $("#splithit" + count);
              hitCard.css("transition", "transform 1s ease-in-out");
              hitCard.css("transform", "translate(500px, 400px)");
              splitHitCard.css("transition", "transform 1s ease-in-out");
              splitHitCard.css("transform", "translate(720px, 400px)");
          }, 100);
      }
      if (module_interactions[0] == "Hit") {
          $("#next_button").hide();
      }
      if (module_interactions[0] == "Stand") {
          $("#next_button").hide();
      }
      if (module_interactions[0] == "Double") {
          $("#next_button").hide();
      }
  
      if (module_interactions[0] == "Split" || module_interactions[2] == "Split") {
        $("#next_button").hide();
      }
      
      
  });

  $(document).keydown(function(event) {
    if (event.key === 'h' || event.key === 't' || event.key === 's' || event.key === 'd') {
      console.log(event.key);
      handle_key_down(event.key);
    }
  });
});


function handle_key_down(key) {
    console.log(interaction)
  if (interaction != 'n' && interaction != key) {
    $("#popup").fadeIn();
      $("#popup_text").text("Try again! We want to " + module_interactions[0] + " here.");

  }
    else if (key == 'h' && interaction == 'h') {
        count++;
        var $image = $("<img>", { "class": "cards " + dealtCardClass, "id": "hit" + count, "src": dealer[4] });
        $("#learn-table").append($image);
        
        setTimeout(function () {
            let hitCard = $("#hit" + count);
            hitCard.css("transition", "transform 1s ease-in-out");
            hitCard.css("transform", "translate(600px, 400px)");
        }, 100);
      
      
        $("#next_button").show();
  }
  else if (key == 'd' && interaction == 'd') {
      count++;
      var $image = $("<img>", { "class": "cards " + dealtCardClass, "id": "hit" + count, "src": dealer[4] });
      $("#learn-table").append($image);

      setTimeout(function () {
          let hitCard = $("#hit" + count);
          hitCard.css("transition", "transform 1s ease-in-out");
          hitCard.css("transform", "translate(450px, 300px) rotate(90deg)");
      }, 100);
     

      $("#next_button").show();
  }
    else if (key == 's' && interaction == 's') {
        interaction = 'n';
        let dealerCard = $("#" + dealerID);
        console.log("in reveal" + dealerID)
        dealerCard.css("opacity", 0);

        setTimeout(() => {
            dealerCard.attr("src", dealer[4]);
            dealerCard.css("opacity", 1);
        }, 10);
      next_screen_change();
  }
  else if (key == 't' && interaction == 't') {
      
     
      setTimeout(function () {
          let splitCard = $("#" + playerSplit);
          splitCard.css("transition", "transform 1s ease-in-out");
          splitCard.css("transform", "translate(620px, 400px)");
          
      }, 100);
      next_screen_change();
  }

  else {
      ;
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
  clear_table();
  
  lesson = scr[new_lesson][new_screen];
  spotlight = lesson.spotlight;
  prev_screen = lesson.prev_screen;

  // Set text 
  text = lesson.text;
  next_screen = lesson.next_screen;
  $('#left-table-text').append(`<p>${text[0]}</p>`);
  $('#mid-table-text').append(`<p>${text[1]}</p>`);
  $('#bottom-table-text').append(`<p>${text[2]}</p>`);
 
  // Enable interactions
  if (interaction == 'N') {
    $("next_button").show()
  }
  else {
    $("next_button").hide()
  }
}

function clear_table() {
  
  $("#learn-table").append(`<img class="deck-card" src="/../static/assets/images/back.png" alt="Card Deck"></img>`);
  $('#left-table-text').empty();
  $('#mid-table-text').empty();
  $('#bottom-table-text').empty();
}

function prev_screen_change() {
    // let prev_mod = prev_screen[0] + 1;
    // let prev_lesson = prev_screen[1] + 1;
    // let prev_sheet = prev_screen[2] + 1;

    // if (prev_mod < next_screen[0] + 1) {
    //     if (false && prev_mod == 1) {
    //         window.location.href = '/lesson_complete/1';
    //     } else if (false && prev_mod == 2) {
    //         window.location.href = '/lesson_complete/2';
    //     } else if (prev_mod == 0) {
    //         window.location.href = '/learn';
    //     }
    // } else {
    //     // This populates the text fields with the correct information from
    //     // prev screen
    //     set_table(prev_lesson - 1, prev_sheet - 1);
    // }

    // kicks back to the module selection page 
    window.location.href = '/learn';
}
function next_screen_change() {
  // Check if next screen is new module
  storeScreenState();  
  let next_mod = next_screen[0] + 1;
  let next_lesson = next_screen[1] + 1;
  let next_sheet = next_screen[2] + 1;
      
  $("#next_button").show();
    
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


function dealCards(dealer) {
    cardSetCount++;

    var cardSetClass = "card-set-" + cardSetCount;
    var uniqueId = "dealer" + cardSetCount;
    var upId = "dealerup" + cardSetCount;
    var $nextButton = $("#next_button");
    var playerSplit;
    $nextButton.prop("disabled", true);
    $.each(dealer, function (index, imageUrl) {
        var $image = $("<img>", { "class": "cards " + cardSetClass, "src": imageUrl });
        $("#learn-table").append($image);
        if (index === 1) {
            $image.attr("id", uniqueId);
        }
        if (index === 0 || index === 2) {
            playerSplit = "player-split" + counter
            counter++;
            $image.attr("id", playerSplit);
        }
        if (index === 3) {
            $image.attr("id", upId);
        }
        setTimeout(() => {
            const images = $("." + cardSetClass);
            images.each(function (index) {
                let newPositionX = 0;
                let newPositionY = 0;

                switch (index) {
                    case 0:
                        newPositionX = 400;
                        newPositionY = 400;
                        break;
                    case 1:
                      
                        newPositionX = 400;
                        newPositionY = 20;
                        break;
                    case 2:
                        newPositionX = 500;
                        newPositionY = 400;
                        break;
                    case 3:
                       
                        newPositionX = 500;
                        newPositionY = 20;
                        break;
                    default:
                        return; // If index is beyond the specified range, exit the function
                }

                setTimeout(() => {
                    $(this).css("transform", `translate(${newPositionX}px, ${newPositionY}px)`);
                }, index * 500); // Delay each card's animation by its index times 1000 milliseconds
            });
        }, 500); // Initial delay of 1000 milliseconds before starting the animation process
        
    });
    
    setTimeout(() => {
        $nextButton.prop("disabled", false);
    }, 2500);
    return { cardSetClass: cardSetClass, uniqueId: uniqueId,  playerSplit: playerSplit};
}

function discardCards(cardClass) {
    const images = $("." + cardClass);
   
    setTimeout(() => {
        images.each(function (index) {
            let newPositionX = 0;
            let newPositionY = 0;

            // Calculate new position based on index
            switch (index) {
                case 0:
                    newPositionX = -600;
                    newPositionY = 400;

                    break;
                case 1:
                    newPositionX = -600;
                    newPositionY = 20;
                    break;
                case 2:
                    newPositionX = -600;
                    newPositionY = 400;
                    break;
                case 3:
                    newPositionX = -600;
                    newPositionY = 20;
                    break;
                case 4:
                    newPositionX = -600;
                    newPositionY = 400;
                    break;
                case 5:
                    newPositionX = -600;
                    newPositionY = 20;
                    break;
                default:
                    return; // If index is beyond the specified range, exit the function
            }

            // Set new position using CSS transform with a delay
            setTimeout(() => {
                $(this).css("transform", `translate(${newPositionX}px, ${newPositionY}px)`);
            }, index * 0); // Delay each image translation by 1 second (adjust timing as needed)
        });
    }, 200); // Initial delay of 1 second before starting the translation process
}
function storeScreenState() {
    var currentState = {}; // Object to store current state
    $(".cards").each(function () {
        var id = $(this).attr("id");
        var offset = $(this).offset();
        currentState[id] = { left: offset.left, top: offset.top };
    });
    screenStates.push(currentState); // Store current state in the array
    // Store initial state if it's the first time
    if (initialScreenStates.length === 0) {
        initialScreenStates.push($.extend(true, {}, currentState)); // Deep copy of currentState
    }
}

function rewind() {
    if (screenStates.length > 0 && initialScreenStates.length > 0) {
        var initialState = initialScreenStates.pop(); // Get the initial state
        // Restore initial state
        $(".cards").each(function () {
            var id = $(this).attr("id");
            var position = initialState[id];
            if (position) {
                $(this).offset({ left: position.left, top: position.top });
            }
        });
        // Clear subsequent changes
        screenStates.length = 0;
    }
}

