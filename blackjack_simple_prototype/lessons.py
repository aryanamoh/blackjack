# Usage: lessons[<Module ID>][<Lesson ID>][<Screen ID>]


def card_image(card):
    rank, suit = card
    card_dir = "/../static/assets/images/"
    
    # TODO: handle the case where we want to show no cards 
    if rank=="_" or suit=="_" or not rank or not suit:
        
        return f"{card_dir}back.png"
    
    else:
        
        if(suit[0] == "h"):
            suit = "Heart"
        if(suit[0] == "c"):
            suit = "Club"
        if(suit[0] == "d"):
            suit = "Diamond"
        if(suit[0] == "s"):
            suit = "Spade"
        
        if(type(rank) == int):
            return f"{card_dir}{str(rank)}{suit}.png"   
        else:
            return f"{card_dir}{str(rank[0]).capitalize()}{suit}.png"
    

lesson_media = [
    [
        [
            [
                [(7, "diamonds"), ("jack", "diamonds2")],
                [("king", "clubs2"), ("king", "clubs2")]
            ],
            [
                [(7, "diamonds"), ("jack", "diamonds2")],
                [("king", "clubs2"), ("king", "clubs2")]
            ],
            [
                [(7, "diamonds"), ("jack", "diamonds2")],
                [("king", "clubs2"), ("king", "clubs2")]
            ],
            [
                [(7, "diamonds"), ("jack", "diamonds2")],
                [("king", "clubs2"), ("king", "clubs2")]
            ],
        ],
        [
            [
                [(10, "diamonds"), (2, "hearts")],
                [(3, "diamonds"), (4, "clubs")]
            ],
            [
                [(10, "diamonds"), (2, "hearts")],
                [(3, "diamonds"), (4, "clubs")]
            ],
            [
                [("jack", "diamonds"), ("queen", "hearts2")],
                [("king", "clubs2"), ("king", "spades2")]
            ],
            [   
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds")],
            ],
            [
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds")],
            ],
            [
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds")],
            ],
            [
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds"), ("king", "spades2")],
            ],
            [
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds"), ("king", "spades2")],
            ],
            [
                [("",""), ("","")],
                [("ace", "clubs"), (7, "diamonds"), ("king", "spades2")],
            ],
            [
                [("",""), ("king", "spades2")],
                [("ace", "clubs"), (7, "diamonds")],
            ],
            [
                [(7, "diamonds"), ("king", "spades2")],
                [("ace", "clubs"), ("","")]
            ],
            [
                [("ace", "clubs"), (7, "diamonds")],
                [("",""), ("",""), ("king", "spades2")],
            ],
            [
                [("ace", "clubs"), (7, "diamonds")],
                [("",""), ("",""), ("king", "spades2")],
            ],
        ],
        [
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts")],
            ],
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("back", "card")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), (10, "diamonds")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), (10, "diamonds")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), (10, "diamonds")],
                [(9, "spades"), (2, "hearts"), (10, "diamonds"), (9, "spades")],
            ],
            [
                [(4, "clubs"), (10, "diamonds")],
                [(9, "spades"), (2, "hearts"), (10, "diamonds"), (9, "spades")],
            ]
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("",""), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("",""), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("ace", "clubs"), (2,"hearts"), ("ace", "clubs"), ("jack", "diamonds")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("ace", "clubs"), (2,"hearts"), (8, "hearts"), ("ace", "clubs"), ("jack", "diamonds")],
            ],
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("4", "clubs"), ("back", "card")],
                [("9", "spades"), ("2", "hearts")],
            ],
            [
                [("4", "clubs"), ("back", "card")],
                [("9", "spades"), ("2", "hearts"), ("jack", "diamonds2")],
            ],
            [
                [("4", "clubs"), ("back", "card")],
                [("9", "spades"), ("2", "hearts"), ("jack", "diamonds2"), ("king", "hearts2")],
            ]
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("ace", "clubs"), ("back", "card")],
                [("jack", "diamonds"), ("4", "clubs")]
            ],
            [
                [("ace", "clubs"), ("7", "diamonds")],
                [("jack", "diamonds"), ("4", "clubs"), ("7", "diamonds")]
            ],
        ]
    ],
    [
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("ace", "clubs"), ("back", "card")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("back", "card")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("back", "card")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("jack", "diamonds")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("jack", "diamonds")],
                [("2", "hearts"), ("jack", "diamonds"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("jack", "diamonds")],
                [("2", "hearts"), ("jack", "diamonds"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("back", "card")],
                [("2", "hearts"), ("jack", "diamonds")],
            ],
        ],
        [
            [
                [("7", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("6", "hearts")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts"), ("jack", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts"), ("jack", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("6", "hearts"), ("4", "clubs")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("jack", "diamonds"), ("6", "hearts"), ("4", "clubs")],
            ],
        ],
        [
            [
                [("7", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("6", "hearts"),],
            ],
            [
                [("7", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("6", "hearts"),],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts"), ("jack", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts"), ("jack", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("6", "hearts"), ("ace", "clubs")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("6", "hearts"), ("ace", "clubs")],
            ],
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
        ],
        [
            [
                [("7", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("6", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts"), ("jack", "diamonds")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("ace", "clubs"), ("6", "hearts")],
            ],
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("ace", "clubs"), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("7", "diamonds")],
                [("jack", "diamonds"), ("ace", "clubs"), ("jack", "diamonds"), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("8", "diamonds"), ("8", "diamonds")],
            ],
            [
                [("jack", "diamonds"), ("7", "diamonds")],
                [("jack", "diamonds"), ("8", "diamonds"), ("jack", "diamonds"), ("8", "diamonds")],
            ],
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("8", "hearts"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
            [
                [("jack", "diamonds"), ("back", "card")],
                [("8", "hearts"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
            [
                [("8", "hearts"), ("back", "card")],
                [("3", "diamonds"), ("7", "diamonds")],
            ],
            [
                [("8", "hearts"), ("jack", "diamonds")],
                [("7", "diamonds"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
        ]
    ]
]

lesson_spotlight= [
    [
        [
            2, 3, 2, 3
        ],
        [
            0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0
        ],
        [
            0, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2
        ],
        [
            0, 3, 3, 3, 3
        ],
        [
            0, 3, 3, 3
        ],
        [
            0, 3, 3
        ]
    ],
    [
        [
            0, 2, 3, 0, 0, 2, 3, 0
        ],
        [
            0, 2, 3, 3, 0, 3
        ],
        [
            3, 3, 3, 3, 3, 3, 3, 0 
        ],
        [
            3, 3, 0
        ],
        [
            0, 3, 3, 3, 3, 0
        ],
        [
            0, 3, 3, 3, 3, 3
        ],
    ]
]

lesson_text = [
    [
        [
            "The object of blackjack is to beat the dealer",
            "The player wants to get as close to 21 as possible without going over",
            "When the dealer has a 17 or more, they can't draw another card",
            "You have 20 so you win!",
        ],
        [
            "Let's learn the value of the cards.",
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
            "1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values."
        ],
        [
            "Let's play a game! We'll tell you what to do.",
            "The dealer always starts with a card face down",
            "You have 11.",
            "You should always draw a card on 11 or less because you can't go over 21.",
            "This is called Hitting",
            "Your new card gives you a total of 20. It would be hard to get 21 from here, so you want to Stand",
            "Standing means you're done and it's the next player's turn.",
            "Since you chose to stand, it is now the dealer's turn",
            "The dealer reveals they had a 10.",
            "The dealer is required to hit when their hand is under 17.",
            "They draw another 10 for a total of 24. Since they have more than 21 they Bust!",
            "Busting means your hand is more than 21 and you lose.",
        ],
        [
            "There are a few more terms you should know. The first is called Splitting.",
            "Being dealt two identical cards allows you to Split.",
            "Splitting allows you to split your hand into two hands.",
            "The dealer will give you a new card for each hand and you can choose to stay or hit for each.",
            "You have 21 for both hands and the dealer has 17 so you win twice!"
        ],
        [
            "Next you'll learn how to Double",
            "Before you've hit on a new hand, you're allowed to Double instead.",
            "The dealer will deal you one card sideways and you can't hit again.",
            "If your hand is larger than the dealer's or the dealer busts, you win double your bet!"
        ],
        [
            "The last thing you need to know is Insurance",
            "If the dealer shows an ace, you'll be offered Insurance. Don't Take It. EVER!",
            "Insurance is a house advantage. If you take it and they have 21, you won't lose your bet. But it's never worth it.",
        ]
    ],
    [
        [
            "In this module you’ll learn how to play 'basic strategy', It is a set of rules that gives you the best possible odds.",
            "Most moves you make depend entirely on the dealer’s 'upcard'. Here we see it is a 4.",
            "You have a 12.",
            "There are more 10’s then any other value card. So always assume the dealer’s hidden card is a ten and the next card dealt will be a 10.",
            "And it is!",
            "And it is again! Dealer busts!",
            "If you had had a 13, 14, 15 etc…the result would be the same",
            "So if the dealer’s upcard is a 2-6. Always stand on 12+",
        ],
        [
            "Let’s consider another scenario…",
            "Now the dealer is showing a 7. We assume his hidden card is a 10.",
            "You have a 16. You’ll lose if the dealer has a 10. So you take a chance and hit!",
            "You draw a 4. You win!",
            "So if the dealer’s upcard is a 7-A. Always hit on 16 or less.",
        ],
        [
            "Let's consider soft hands (hands with an ace)", 
            "Total: 7 or 17",
            "If we assume the next card is a 10. Then after we hit are hard hand will become the same as the higher value of our soft hand.",
            "Total: Hard 17.",
            "However, there is a also a chance you could pull a smaller card…",
            "Total: 11 or 21.",
            "So always hit on soft hands that have a high total of 17 or less.",
        ],
        [
            "What if you have a soft hand of 18 or higher?",
            "It's best to stay soft on any hand above 18?",
            "You win!",
        ],
        [
            "Let's talk about when to split.",
            "Do you recall what to do with two aces?",
            "Exactly Right! ALWAYS split aces on any hand. You win double your bet!",
            "Should you always split eights too?",
            "Yes! 16 (8+8) is the worst total you can have. Splitting gives you a chance to change your luck!",
            "So always split As and 8s!",
        ],
        [
            "The last thing you need to know is when to double",
            "11 is the best starting hand outside of blackjack (21)",
            "21! Blackjack! We doubled our bet!",
            "10 should always be doubled UNLESS the dealer shows a 10 or an 8",
            "20! We bet again. Double our bet!",
        ],
    ]
]

def list_of_cards(idx):
    lst = []
    for hand in lesson_media[idx]:
        inner_lst = []
        for rank, suit in hand:
                inner_lst.append(card_image((rank, suit)))
        lst.append([inner_lst[:2], inner_lst[2:]])
    return lst


titles = [
    [
        "What is blackjack and how does a player win or lose?",
        "What do the cards mean?",
        "Let's play a guided game!",
        "Splitting...what is it? ",
        "Learn how to Double",
        "Let's learn about Insurance! ",
    ],
    [
        "title needed" for _ in range(len(lesson_text[1]))
    ]
]

def filename_generator(hand):
    return list(map(lambda tple : tuple(card_image(x) for x in tple), hand))

lessons = [[
    [
        {
            "lesson_id" : lesson + 1,
            "title" : titles[module][lesson],
            "text" : lesson_text[module][lesson][screen],
            "spotlight" : lesson_spotlight[module][lesson][screen],
            "next_screen" : [(module + (0 if lesson + 1 < len(lesson_text[module]) else 1)), #% len(lesson_text)""",
                             (lesson + (0 if screen + 1 < len(lesson_screens) else 1)) % len(lesson_text[module]),
                             (screen + 1) % len(lesson_screens)],
            # "media_array" : lesson_media[module][lesson][screen],
            "media_array" : filename_generator(lesson_media[module][lesson][screen]),
            "start_time" : 0,
        } for screen in range(len(lesson_screens))
    ] for lesson, lesson_screens in enumerate(lesson_text[module])
] for module in range(len(lesson_text))]

# for module in lessons:
#      for lesson in module:
#           for screen in module:
#                 for s in screen:
#                      for k, v in s.items():
#                           print(k, v)

"""

lessons = {
    "1": {
        "1":{
            "lesson_id": "1",
            "title": "What is blackjack and how does a player win or lose?",
            "media":"/static/assets/images/card_images/ace_of_spades.png",
            "media_alt":"Lesson 1 media alt text",
            "text": "Goal of blackjack is to beat the dealer...",
            "next_lesson": "2",
            "start_time":0,
            "text_array":[
                          ["The object of blackjack is to beat the dealer","text"],
                          ["The player wants to get as close to 21 as possible without going over","player"],
                          ["When the dealer has a 17 or more, they can't draw another card","dealer"],
                          ["You have 20 so you win!","player"]],
            "media_array" : list_of_cards(0)
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?",
            "media":"/static/assets/images/card_images/2_of_clubs.png",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "3",
            "start_time":0,
            "text_array":[
                         ["Let's learn the value of the cards.","text"],
                          ["Numbers add their face value.","player_dealer_both"],
                          ["Face cards are all worth 10.","player_dealer_both"],
                          ["Aces are worth 1 or 11.","player"],
                          ["This hand is 8 OR an 18","player"],
                          ["It is called a SOFT hand because you can choose the hand's value of 8 or 18", "player"],
                          ["Asking for another card is called HITTING.","player"],
                          ["Hitting gave us a 10. Now we have 18.","player"],
                          ["This is called a HARD hand.","player"],
                          ["The King is 10.","dealer_player"],
                          ["The seven is 7.","dealer_player"],
                          ["The ace is 1.","dealer"],
                          ["1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values.","dealer"]
                          ],
            "media_array" : list_of_cards(1)
        
        },
        "3":{
            "lesson_id": "3",
            "title": "Let's play a guided game!",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "You will like to hold onto your current hand",
            "next_lesson": "4",
            "start_time":0,
            "text_array":[
                          ["Let's play a game! We'll tell you what to do.","text"],
                          ["The dealer always starts with a card face down","dealer"],
                          ["You have 11.","player"],
                          ["You should always draw a card on 11 or less because you can't go over 21.","player"],
                          ["This is called Hitting","player"],
                          ["Your new card gives you a total of 20. It would be hard to get 21 from here, so you want to Stand","player"],
                          ["Standing means you're done and it's the next player's turn.","player_dealer"],
                          ["Since you chose to stand, it is now the dealer's turn","player_dealer"],
                          ["The dealer reveals they had a 10.","player_dealer"],
                          ["The dealer is required to hit when their hand is under 17.","player_dealer"],
                          ["They draw another 10 for a total of 24. Since they have more than 21 they Bust!","dealer_player"],
                          ["Busting means your hand is more than 21 and you lose.","dealer_player"]
                        ],
            "media_array" : list_of_cards(2)
        },
        "4":{
            "lesson_id": "4",
            "title": "Splitting...what is it? ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ask the friendly dealer for another card to your hand",
            "next_lesson": "5",
            "start_time":0,
            "text_array":[
                          ["There are a few more terms you should know. The first is called Splitting.","text"],
                          ["Being dealt two identical cards allows you to Split.","player"],
                          ["Splitting allows you to split your hand into two hands.","player"],
                          ["The dealer will give you a new card for each hand and you can choose to stay or hit for each.","player"],
                          ["You have 21 for both hands and the dealer has 17 so you win twice!","player"]
                        ],
            "media_array" : list_of_cards(3)
        },
        "5":{
            "lesson_id": "5",
            "title": "Learn how to Double",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Insure that you'll only use x of your bet",
            "next_lesson": "6",
            "start_time":0,
            "text_array":[
                          ["Next you'll learn how to Double","text"],
                          ["Before you've hit on a new hand, you're allowed to Double instead.","player"],
                          ["The dealer will deal you one card sideways and you can't hit again.","player_sideways"],
                          ["If your hand is larger than the dealer's or the dealer busts, you win double your bet!","player_sideways_dealer"]
                          ],
            
            "media_array" : list_of_cards(4)
        },
        "6":{
            "lesson_id": "6",
            "title": "Let's learn about Insurance! ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "No, not like the living legend",
            "next_lesson": "end",
            "start_time":0,
            "text_array":[
                          ["The last thing you need to know is Insurance","dealer"],
                          ["If the dealer shows an ace, you'll be offered Insurance. Don't Take It. EVER!","dealer"],
                          ['''Insurance is a house advantage. 
                           If you take it and they have 21, you won't lose your bet. 
                           But it's never worth it.''',"player_dealer"],
                          ],
            "media_array" : list_of_cards(5)
        },
        
        "next_module_id": 2
    },
    
    "2": {
        
        "1":{
            "lesson_id": "1",
            "title": "What is blackjack and how does a player win or lose?",
            "media":"/static/assets/images/card_images/ace_of_spades.png",
            "media_alt":"Lesson 1 media alt text",
            "text": "Goal of blackjack is to beat the dealer.....",
            "next_lesson": "2",
            "start_time":0,
            "text_array":[
                          ["The object of blackjack is to beat the dealer","text"],
                          ["The player wants to get as close to 21 as possible without going over","player"],
                          ["When the dealer has a 17 or more, they can't draw another card","dealer"],
                          ["You have 20 so you win!","player"]],
            # "media_array" : [card_image(rank, suit) for rank, suit in list_of_cards(0)]
            "media_array" : list_of_cards(0)
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?",
            "media":"/static/assets/images/card_images/2_of_clubs.png",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "3",
            "start_time":0,
            "text_array":[
                         ["Let's learn the value of the cards.","text"],
                          ["Numbers add their face value.","player_dealer"],
                          ["Face cards are all worth 10.","player_dealer"],
                          ["Aces are worth 1 or 11.","player"],
                          ["This hand is 8 OR an 18","player"],
                          ["It is called a SOFT hand because you can choose the hand's value of 8 or 18","player"],
                          ["Asking for another card is called HITTING.","player"],
                          ["Hitting gave us a 10. Now we have 18.","player"],
                          ["This is called a HARD hand.","player"],
                          ["The King is 10.","dealer_player"],
                          ["The seven is 7.","dealer_player"],
                          ["The ace is 1.","dealer"],
                          ["1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values.","dealer"]
                          ],
            "media_array" : list_of_cards(1)
        },
        "next_module_id": "Quiz"
    }
}

"""


"""

def card_image(rank, suit):
    card_dir = "/static/assets/images/card_images/"
    
    # handle the case where we don't want to show the back of the cards
    # for an empty slot 
    if rank=="_" or suit=="_" or not rank or not suit:
        return f"{card_dir}back_of_card.png"
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
        [   ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("",""),
            ("",""),
            ("ace", "clubs"),
            (7, "diamonds"),
            ("king", "spades2"),
        ],
        [
            ("",""),
            ("king", "spades2"),
            ("ace", "clubs"),
            (7, "diamonds"),
        ],
        [
            (7, "diamonds"),
            ("king", "spades2"),
            ("ace", "clubs"),
            ("","")
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
            ("",""),
            ("",""),
            ("king", "spades2"),
        ],
        [
            ("ace", "clubs"),
            (7, "diamonds"),
            ("",""),
            ("",""),
            ("king", "spades2"),
        ],
    ],
    [
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
        ],
        
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
        ],
        
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
        ],
        
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
        ],
        
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        
        [
            (4, "clubs"),
            ("back", "card"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        [
            (4, "clubs"),
            (10, "diamonds"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        
        [
            (4, "clubs"),
            (10, "diamonds"),
            (9, "spades"),
            (2, "hearts"),
            (9, "spades"),
        ],
        
        [
            (4, "clubs"),
            (10, "diamonds"),
            (9, "spades"),
            (2, "hearts"),
            (10, "diamonds"),
            (9, "spades")
        ],
        [
            (4, "clubs"),
            (10, "diamonds"),
            (9, "spades"),
            (2, "hearts"),
            (10, "diamonds"),
            (9, "spades")
        ]
        
    ],
    [
        [("_","_"),("_","_"),("_","_"),("_","_")],
        [
            ("jack", "diamonds"),
            ("back", "card"),
            ("ace", "clubs"),
            ("ace", "clubs"),
        ],
        
        [
            ("jack", "diamonds"),
            ("back", "card"),
            ("ace", "clubs"),
            ("",""), ("",""),
            ("ace", "clubs")
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
        [("",""),("",""),("",""),("","")],
        
        [
            ("4", "clubs"),
            ("back", "card"),
            ("9", "spades"),
            ("2", "hearts"),
        ],
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
            ("9", "spades"),
            ("2", "hearts"),
            ("jack", "diamonds2"),
            ("king", "hearts2"),
        ]

    ],
    [
        [("",""),("",""),("",""),("","")],
 
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

def list_of_cards(idx):
    lst = []
    for hand in lesson_media[idx]:
        inner_lst = []
        for rank, suit in hand:
                inner_lst.append(card_image(rank, suit))
        lst.append(inner_lst)
    return lst


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
            "text_array":[
                          ["The object of blackjack is to beat the dealer","text"],
                          ["The player wants to get as close to 21 as possible without going over","player"],
                          ["When the dealer has a 17 or more, they can't draw another card","dealer"],
                          ["You have 20 so you win!","player"]],
            "media_array" : list_of_cards(0)
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?",
            "media":"/static/assets/images/card_images/2_of_clubs.png",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "3",
            "start_time":0,
            "text_array":[
                         ["Let's learn the value of the cards.","text"],
                          ["Numbers add their face value.","player_dealer_both"],
                          ["Face cards are all worth 10.","player_dealer_both"],
                          ["Aces are worth 1 or 11.","player"],
                          ["This hand is 8 OR an 18","player"],
                          ["It is called a SOFT hand because you can choose the hand's value of 8 or 18","player"],
                          ["Asking for another card is called HITTING.","player"],
                          ["Hitting gave us a 10. Now we have 18.","player"],
                          ["This is called a HARD hand.","player"],
                          ["The King is 10.","dealer_player"],
                          ["The seven is 7.","dealer_player"],
                          ["The ace is 1.","dealer"],
                          ["1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values.","dealer"]
                          ],
            "media_array" : list_of_cards(1)
        
        },
        "3":{
            "lesson_id": "3",
            "title": "Let's play a guided game!",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "You will like to hold onto your current hand",
            "next_lesson": "4",
            "start_time":0,
            "text_array":[
                          ["Let's play a game! We'll tell you what to do.","text"],
                          ["The dealer always starts with a card face down","dealer"],
                          ["You have 11.","player"],
                          ["You should always draw a card on 11 or less because you can't go over 21.","player"],
                          ["This is called Hitting","player"],
                          ["Your new card gives you a total of 20. It would be hard to get 21 from here, so you want to Stand","player"],
                          ["Standing means you're done and it's the next player's turn.","player_dealer"],
                          ["Since you chose to stand, it is now the dealer's turn","player_dealer"],
                          ["The dealer reveals they had a 10.","player_dealer"],
                          ["The dealer is required to hit when their hand is under 17.","player_dealer"],
                          ["They draw another 10 for a total of 24. Since they have more than 21 they Bust!","dealer_player"],
                          ["Busting means your hand is more than 21 and you lose.","dealer_player"]
                        ],
            "media_array" : list_of_cards(2)
        },
        "4":{
            "lesson_id": "4",
            "title": "Splitting...what is it? ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ask the friendly dealer for another card to your hand",
            "next_lesson": "5",
            "start_time":0,
            "text_array":[
                          ["There are a few more terms you should know. The first is called Splitting.","text"],
                          ["Being dealt two identical cards allows you to Split.","player"],
                          ["Splitting allows you to split your hand into two hands.","player"],
                          ["The dealer will give you a new card for each hand and you can choose to stay or hit for each.","player"],
                          ["You have 21 for both hands and the dealer has 17 so you win twice!","player"]
                        ],
            "media_array" : list_of_cards(3)
        },
        "5":{
            "lesson_id": "5",
            "title": "Learn how to Double",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "Insure that you'll only use x of your bet",
            "next_lesson": "6",
            "start_time":0,
            "text_array":[
                          ["Next you'll learn how to Double","text"],
                          ["Before you've hit on a new hand, you're allowed to Double instead.","player"],
                          ["The dealer will deal you one card sideways and you can't hit again.","player_sideways"],
                          ["If your hand is larger than the dealer's or the dealer busts, you win double your bet!","player_sideways_dealer"]
                          ],
            
            "media_array" : list_of_cards(4)
        },
        "6":{
            "lesson_id": "6",
            "title": "Let's learn about Insurance! ",
            "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-to-play-blackjack-card-values-min.jpg",
            "media_alt":"Lesson 2 media alt text",
            "text": "No, not like the living legend",
            "next_lesson": "end",
            "start_time":0,
            "text_array":[
                          ["The last thing you need to know is Insurance","dealer"],
                          ["If the dealer shows an ace, you'll be offered Insurance. Don't Take It. EVER!","dealer"],
                          ['''Insurance is a house advantage. 
                           If you take it and they have 21, you won't lose your bet. 
                           But it's never worth it.''',"player_dealer"],
                          ],
            "media_array" : list_of_cards(5)
        },
        
        "next_module_id": 2
    },
    
    "2": {
        
        "1":{
            "lesson_id": "1",
            "title": "What is blackjack and how does a player win or lose?",
            "media":"/static/assets/images/card_images/ace_of_spades.png",
            "media_alt":"Lesson 1 media alt text",
            "text": "Goal of blackjack is to beat the dealer.....",
            "next_lesson": "2",
            "start_time":0,
            "text_array":[
                          ["The object of blackjack is to beat the dealer","text"],
                          ["The player wants to get as close to 21 as possible without going over","player"],
                          ["When the dealer has a 17 or more, they can't draw another card","dealer"],
                          ["You have 20 so you win!","player"]],
            # "media_array" : [card_image(rank, suit) for rank, suit in list_of_cards(0)]
            "media_array" : list_of_cards(0)
        },
        "2":{
            "lesson_id": "2",
            "title": "What do the cards mean?",
            "media":"/static/assets/images/card_images/2_of_clubs.png",
            "media_alt":"Lesson 2 media alt text",
            "text": "Ace can be of value 1 or 11",
            "next_lesson": "3",
            "start_time":0,
            "text_array":[
                         ["Let's learn the value of the cards.","text"],
                          ["Numbers add their face value.","player_dealer"],
                          ["Face cards are all worth 10.","player_dealer"],
                          ["Aces are worth 1 or 11.","player"],
                          ["This hand is 8 OR an 18","player"],
                          ["It is called a SOFT hand because you can choose the hand's value of 8 or 18","player"],
                          ["Asking for another card is called HITTING.","player"],
                          ["Hitting gave us a 10. Now we have 18.","player"],
                          ["This is called a HARD hand.","player"],
                          ["The King is 10.","dealer_player"],
                          ["The seven is 7.","dealer_player"],
                          ["The ace is 1.","dealer"],
                          ["1 + 7 + 10 = 18. The hand is HARD because the ace can no longer have two values.","dealer"]
                          ],
            "media_array" : list_of_cards(1)
        },
        "next_module_id": "Quiz"
    }
}


"""

for mod in lessons:
    for les in mod:
        for scr in les:
            print(scr["next_screen"])
