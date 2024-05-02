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

actions = [
    [
        [

        ]
    ]
]

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
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts")],
            ],
            
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts")],
            ],
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("", "")],
                [(9, "spades"), (2, "hearts"), (9, "spades")],
            ],
            [
                [(4, "clubs"), ("", "")],
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
                [("jack", "diamonds"), ("", "")],
                [("ace", "clubs"), ("",""), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("", "")],
                [("ace", "clubs"), ("",""), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("", "")],
                [("ace", "clubs"), (2,"hearts"), ("ace", "clubs"), ("jack", "diamonds")],
            ],
            [
                [("jack", "diamonds"), ("", "")],
                [("ace", "clubs"), (2,"hearts"), (8, "hearts"), ("ace", "clubs")], #, ("jack", "diamonds")
            ],
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("4", "clubs"), ("", "")],
                [("9", "spades"), ("2", "hearts")],
            ],
            [
                [("4", "clubs"), ("", "")],
                [("9", "spades"), ("2", "hearts"), ("jack", "diamonds2")],
            ],
            [
                [("4", "clubs"), ("", "")],
                [("9", "spades"), ("2", "hearts"), ("jack", "diamonds2"), ("king", "hearts2")],
            ]
        ],
        [
            [
                [("", ""), ("", "")],
                [("", ""), ("", "")],
            ],
            [
                [("ace", "clubs"), ("", "")],
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
                [("ace", "clubs"), ("", "")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("", "")],
                [("2", "hearts"), ("jack", "diamonds")]
            ],
            [
                [("ace", "clubs"), ("", "")],
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
                [("ace", "clubs"), ("", "")],
                [("2", "hearts"), ("jack", "diamonds")],
            ],
        ],
        [
            [
                [("7", "diamonds"), ("", "")],
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
                [("7", "diamonds"), ("", "")],
                [("ace", "clubs"), ("6", "hearts"), ("4", "clubs")],
            ],
            [
                [("7", "diamonds"), ("jack", "diamonds")],
                [("jack", "diamonds"), ("6", "hearts"), ("4", "clubs")],
            ],
        ],
        [
            [
                [("7", "diamonds"), ("", "")],
                [("ace", "clubs"), ("6", "hearts"),],
            ],
            [
                [("7", "diamonds"), ("", "")],
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
                [("7", "diamonds"), ("", "")],
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
                [("jack", "diamonds"), ("", "")],
                [("ace", "clubs"), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("7", "diamonds")],
                [("jack", "diamonds"), ("ace", "clubs"), ("jack", "diamonds"), ("ace", "clubs")],
            ],
            [
                [("jack", "diamonds"), ("", "")],
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
                [("jack", "diamonds"), ("", "")],
                [("8", "hearts"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
            [
                [("jack", "diamonds"), ("", "")],
                [("8", "hearts"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
            [
                [("8", "hearts"), ("", "")],
                [("3", "diamonds"), ("7", "diamonds")],
            ],
            [
                [("8", "hearts"), ("jack", "diamonds")],
                [("7", "diamonds"), ("3", "diamonds"), ("jack", "diamonds")],
            ],
        ]
    ]
]

lesson_spotlight = [
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
        ],
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


lessons = [
   [ 
       [ 
        { 
            "lesson_id" : lesson + 1,
            "title" : titles[module][lesson],
            "text" : lesson_text[module][lesson][screen],
            "spotlight" : lesson_spotlight[module][lesson][screen],
            "next_screen" : [(module + (0 if ((screen + 1) < len(lesson_screens)) or (lesson + 1) < len(lesson_text[module]) else 1)), #% len(lesson_text)""",
                             (lesson + (0 if (screen + 1) < len(lesson_screens) else 1)) % len(lesson_text[module]),
                             (screen + 1) % len(lesson_screens)],
            # "media_array" : lesson_media[module][lesson][screen],
            "media_array" : filename_generator(lesson_media[module][lesson][screen]),
            "start_time" : 0,
            } for screen in range(len(lesson_screens))
            ] for lesson, lesson_screens in enumerate(lesson_text[module])
] for module in range(len(lesson_text))
]


# lessons = {
#     module : {
#         lesson : {
#             screen : {
#             "lesson_id" : lesson + 1,
#             "title" : titles[module][lesson],
#             "text" : lesson_text[module][lesson][screen],
#             "spotlight" : lesson_spotlight[module][lesson][screen],
#             "next_screen" : [(module + (0 if ((screen + 1) < len(lesson_screens)) or (lesson + 1) < len(lesson_text[module]) else 1)), #% len(lesson_text)""",
#                              (lesson + (0 if (screen + 1) < len(lesson_screens) else 1)) % len(lesson_text[module]),
#                              (screen + 1) % len(lesson_screens)],
#             # "media_array" : lesson_media[module][lesson][screen],
#             "media_array" : filename_generator(lesson_media[module][lesson][screen]),
#             "start_time" : 0,
#         } for screen in range(len(lesson_screens))
#         } for lesson, lesson_screens in enumerate(lesson_text[module])
#     } for module in range(len(lesson_text))
# }

import json
import pprint

print("lessons = [")

for module in lessons:
    print("\t[")
    for lesson in module:
        print('\t\t[')
        for screens in lesson:
            print("\t\t\t{")
            for k, v in screens.items():
                if isinstance(v, str):
                    print(f"\t\t\t\"{k}\" : \"{v}\",")
                else:
                    print(f"\t\t\t\"{k}\" : {v},")
            print("\t\t\t},")
        print('\t\t],')
    print("\t],")
print("]")
