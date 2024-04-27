# Usage: lessons[<Module ID>][<Lesson ID>]


def card_image(rank, suit):
    card_dir = "/static/assets/images/card_images/"
    return f"{card_dir}{str(rank)}_of_{suit}.png"

lesson1_text = [

]

lesson_media = [
    [
        [
            (7, "diamonds"),
            ("jack", "diamonds2"),
            ("king", "clubs2"),
            ("king", "clubs2")
        ],
        [
            (7, "diamonds"),
            ("jack", "diamonds2"),
            ("king", "clubs2"),
            ("king", "clubs2")
        ],
        [
            (7, "diamonds"),
            ("jack", "diamonds2"),
            ("king", "clubs2"),
            ("king", "clubs2")
        ],
        [
            (7, "diamonds"),
            ("jack", "diamonds2"),
            ("king", "clubs2"),
            ("king", "clubs2")
        ],
    ],
    [
        [
            (10, "diamonds"),
            (2, "hearts"),
            (3, "diamonds"),
            (4, "clubs")
        ],
        [
            (10, "diamonds"),
            (2, "hearts"),
            (3, "diamonds"),
            (4, "clubs")
        ],
        [
            ("jack", "diamonds"),
            ("queen", "hearts2"),
            ("king", "clubs2"),
            ("king", "spades2")
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("king", "spades2"),
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            (7, "diamonds"),
            ("king", "spades2"),
            ("ace", "clubs"),
        ],
        [
            (7, "diamonds"),
            ("king", "spades2"),
            ("ace", "clubs"),
        ],
    ],
    [
        
        [
            (4, "clubs.png").
            # ("jack", "card.png").
            (9, "spades.png").
            (2, "hearts.png"
        ],
        
        [
            (4, "clubs.png").
            # ("jack", "card.png").
            (9, "spades.png").
            (2, "hearts.png"
        ],
        
        [
            (4, "clubs.png").
            # (back, "card.png").
            (9, "spades.png").
            (2, "hearts.png"
        ],
        
        [
            (4, "clubs.png").
            # (back, "card.png").
            (9, "spades.png").
            (2, "hearts.png").
            (9, "spades.png"
        ],
        
        [
            (4, "clubs.png").
            # (back, "card.png").
            (9, "spades.png").
            (2, "hearts.png").
            (9, "spades.png"
        ],
        
        [
            (4, "clubs.png").
            ("jack", "card.png").
            (9, "spades.png").
            (2, "hearts.png").
            (9, "spades.png"
        ],
        
        [
            (4, "clubs.png").
            (10, "diamonds.png").
            (9, "spades.png").
            (2, "hearts.png").
            (9, "spades.png"
        ],
        
        [
            (4, "clubs.png").
            (10, "diamonds.png").
            (10, "diamonds.png").
            (9, "spades.png").
            (2, "hearts.png").
            (9, "spades.png"
        ],
        
        [
            (4, "clubs"),
            (10 , "diamonds"),
            (10 , "diamonds"),
            (9 , "spades"),
            (2 , "hearts"),
            (9 , "spades")
        ],
        
        [
            (4, "clubs"),
            (10, "diamonds"),
            (10, "diamonds"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades")
        ]
        
    ],

    [ 
        ["","","",""],
        
        [
            ("jack", "diamonds"),
            ("back", "card"),
            ("ace", "clubs"),
            ("ace", "clubs,png"),
        ],
        
        [
            ("jack", "diamonds"),
            ("back", "card"),
            ("ace", "clubs"),
            "",
            "",
            ("ace", "clubs,png")
        ],
        
        [
            ("jack", "diamonds"),
            ("back", "card"),
            ("ace", "clubs"),
            ("2", "hearts"),
            ("ace", "clubs"),
            ("jack", "diamonds")
        ],
        
        [
            ("jack", "diamonds"),
            ("7", "diamonds"),
            ("ace", "clubs"),
            ("2", "hearts"),
            ("8", "hearts"),
            ("ace", "clubs"),
            ("jack", "diamonds")
        ],
    ],

    [
        ["","","",""],
        
        [
            ("4", "clubs"),
            ("back", "card"),
            ("9", "spades"),
            ("2", "hearts"),
            ("jack", "diamonds2"),
        ],
        
        [
            ("4", "clubs"),
            ("8", "hearts"),
            ("king", "hearts2"),
            ("9", "spades"),
            ("2", "hearts"),
            ("jack", "diamonds2"),
        ]

    ],
    [
        [
            "","","",""
        ],
        
        [
            ("ace", "clubs"),
            ("back", "card"),
            ("jack", "diamonds"),
            ("4", "clubs")
        ],
        
        [
            ("ace", "clubs"),
            ("7", "diamonds"),
            ("jack", "diamonds"),
            ("4", "clubs"),
            ("7", "diamonds")
        ],
    ]
]

lessons = {  
    "1": {
        "1":{
            "lesson_id": "1",
            "title": "What is blackjack and how does a player win or lose?",
            "media":"/static/assets/images/card_images/ace_of_spades.png",
            "media_alt":"Lesson 1 media alt text",
            "text": "Goal of blackjack is to beat the dealer.....",
            "next_lesson": "2",
            "start_time":0,
            "text_array":["The object of blackjack is to beat the dealer",
                          "The player wants to get as close to 21 as possible without going over",
                          "When the dealer has a 17 or more, they can't draw another card",
                          "You have 20 so you win!"],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[0] ]
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?",
            "media":"/static/assets/images/card_images/2_of_clubs.png",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "3",
            "start_time":0,
            "text_array":["Let's learn the value of the cards.",
                          "Numbers add their face value.",
                          "Face cards are all worth 10.",
                          "Aces are worth 1 or 11.",
                          "This hand is 8 OR an 18",
                          "It is called a SOFT hand because you can choose the hand's value of 8 or 18",
                          "Asking for another card is called HITTING.",
                          "Hitting gave us a 10. Now we have 18.",
                          "This is called a HARD hand.",
                          "The King is 10.",
                          "The seven is 7.",
                          "The ace is 1.",
                          "1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values."],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[1] ]
        },
        "3":{
            "lesson_id": "3",
            "title": "Let's play a guided game!",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "You will like to hold onto your current hand",
            "next_lesson": "4",
            "start_time":0,
            "text_array":["Let's play a game! We'll tell you what to do.",
                          "The dealer always starts with a card face down",
                          "You have 11.",
                          "You should always draw a card on 11 or less because you can't go over 21.",
                          ["This is called Hitting","player_hit_button"],
                          ["Your new card gives you a total of 20. It would be hard to get 21 from here, so you want to Stand","stand_button"],
                          "Since you chose to stand, it is now the dealer's turn",
                          "The dealer reveals they had a 10.",
                          "The dealer is required to hit when their hand is under 17.",
                          "They draw another 10 for a total of 24. Since they have more than 21 they Bust!",
                          "Busting means your hand is more than 21 and you lose."],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[2]],
        },
        "4":{
            "lesson_id": "4",
            "title": "Splitting...what is it? ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ask the friendly dealer for another card to your hand",
            "next_lesson": "5",
            "start_time":0,
            "text_array":["There are a few more terms you should know. The first is called Splitting.",
                          ["Being dealt two identical cards aallows you to Split.","split_button"],
                          "Splitting allows you to split your hand into two hands.",
                          ["The dealer will give you a new card for each hand and you can choose to stay or hit for each.",
                            "player_hit_button","player_stand_button"],
                          "You have 21 for both hands and the dealer has 17 so you win twice!",],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[3]],
        },
        "5":{
            "lesson_id": "5",
            "title": "Learn how to Double",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Insure that you'll only use x of your bet",
            "next_lesson": "6",
            "start_time":0,
            "text_array":["Next you'll learn how to Double",
                          ["Before you've hit on a new hand, you're allowed to Double instead.","player_double_button"],
                          ["If your hand is larger than the dealer's or the dealer busts, you win double your bet!","dealer_hit"],
                          ""],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[4]],
        },
        "6":{
            "lesson_id": "6",
            "title": "Let's learn about Insurance! ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "No, not like the living legend",
            "next_lesson": "end",
            "start_time":0,
            "text_array":["The last thing you need to know is Insurance",
                          ["If the dealer shows an ace, you'll be offered Insurance. Don't Take It. EVER!","no_insurance_button"],
                          ['''Insurance is a house advantage. 
                           If you take it and they have 21, you won't lose your bet. 
                           But it's never worth it.''',"player_hit_button"],
                          ],
            "media_array" : [card_image(rank, suit) for rank, suit in lesson_media[5]],
        },
        
        "next_module_id": 2
    },
    
    "2": {
        "1":{
            "lesson_id": "1",
            "title": "What is basic strategy?",
            "media":"/static/assets/images/basic_strategy.png",
            "media_alt":"Lesson 1 media alt text",
            "text": "Try wrapping your head around this baby :)",
            "next_lesson": "2",
            "start_time":0
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?....",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "end",
            "start_time":0
        },
        "next_module_id": "Quiz"
    }
}
