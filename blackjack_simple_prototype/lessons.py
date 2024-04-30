# Usage: lessons[<Module ID>][<Lesson ID>]


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
