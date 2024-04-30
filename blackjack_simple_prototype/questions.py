# Usage: lessons[<Module ID>][<Question ID>]

quiz_questions = {  
        "1":{
            "quiz_id": "1",
            "quiz_question": "What are the possible values of this hand?",
           'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/JSpade.png'
            ],
            'card_images_player': [
            '/../static/assets/images/AHeart.png',
            '/../static/assets/images/5Club.png'
            ],
            "panswers": ["16 and 6", "15 and 6", "16 only", "15 only"],
            "answer": 0,
            "next_question": "2",
            "client_response":"",
            "progress": "0%",
            "answersLocked": False
        },
        "2":{
            "quiz_id": "2",
            "quiz_question": "What should you do in this situation?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/KHeart.png'
            ],
            'card_images_player': [
            '/../static/assets/images/8Spade.png',
            '/../static/assets/images/8Diamond.png'
            ],
            "panswers": ["Stand", "Double", "Split", "Hit"],
            "answer": 2,
            "next_question": "3",
            "client_response":"",
            "progress": "10%",
            "answersLocked": False
        },
        "3":{
            "quiz_id": "3",
            "quiz_question": "Should you take insurance?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/AClub.png'
            ],
            'card_images_player': [
            '/../static/assets/images/6Heart.png',
            '/../static/assets/images/10Spade.png'
            ],
            "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak"],
            "answer": 1,
            "next_question": "4",
           "client_response":"",
            "progress": "20%",
            "answersLocked": False
        },
        "4":{
            "quiz_id": "4",
            "quiz_question": "What type of hand do you have?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/6Spade.png'
            ],
            'card_images_player': [
            '/../static/assets/images/ADiamond.png',
            '/../static/assets/images/2Heart.png'
            ],
            "panswers": ["A hand with no face cards", "A bad hand", "A soft hand", "A hard hand"],
            "answer": 2,
            "next_question": "5",
            "client_response":"",
            "progress": "30%",
            "answersLocked": False
        },
        "5":{
            "quiz_id": "5",
            "quiz_question": "What's your best move according to basic strategy?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/5Club.png'
            ],
            'card_images_player': [
            '/../static/assets/images/8Spade.png',
            '/../static/assets/images/3Heart.png'
            ],
            "panswers": ["Hit", "Stand", "Take Insurance", "Double"],
            "answer": 3,
            "next_question": "6",
            "client_response":"",
            "progress": "40%",
            "answersLocked": False
        },
        "6":{
            "quiz_id": "6",
            "quiz_question": "Dealer is showing a 6. What should you do?",
           'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/6Heart.png'
            ],
            'card_images_player': [
            '/../static/assets/images/2Heart.png',
            '/../static/assets/images/QDiamond.png'
            ],
            "panswers": ["Stand", "Hit", "Double", "Split"],
            "answer": 0,
            "next_question": "7",
            "client_response":"",
            "progress": "50%",
            "answersLocked": False
        },
        "7":{
            "quiz_id": "7",
            "quiz_question": "Dealer is showing a 10. What should you do?",
           'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/10Diamond.png'
            ],
            'card_images_player': [
            '/../static/assets/images/9Heart.png',
            '/../static/assets/images/7Club.png'
            ],
            "panswers": ["Stand", "Hit", "Double", "Split"],
            "answer": 1,
            "next_question": "8",
            "client_response":"",
            "progress": "60%",
            "answersLocked": False
        },
        "8":{
            "quiz_id": "8",
            "quiz_question": "Dealer is showing an Ace. What should you do?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/ADiamond.png'
            ],
            'card_images_player': [
            '/../static/assets/images/7Club.png',
            '/../static/assets/images/7Heart.png'
            ],
            "panswers": ["Stand", "Hit", "Split", "Take insurance"],
            "answer": 1,
            "next_question": "9",
            "client_response":"",
            "progress": "70%",
            "answersLocked": False
        },
        "9":{
            "quiz_id": "9",
            "quiz_question": "Dealer is showing a 4. What should you do?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/4Spade.png'
            ],
            'card_images_player': [
            '/../static/assets/images/5Heart.png',
            '/../static/assets/images/5Diamond.png'
            ],
            "panswers": ["Stand", "Hit", "Double", "Split"],
            "answer": 2,
            "next_question": "10",
            "client_response":"",
            "progress": "80%",
            "answersLocked": False
        },
        "10":{
            "quiz_id": "10",
            "quiz_question": "Dealer is showing a 8. What should you do?",
            'card_images_dealer': [
            '/../static/assets/images/back.png',
            '/../static/assets/images/8Heart.png'
            ],
            'card_images_player': [
            '/../static/assets/images/QClub.png',
            '/../static/assets/images/7Diamond.png'
            ],
            "panswers": ["Stand", "Hit", "Double", "Pray"],
            "answer": 0,
            "next_question": "end",
            "client_response":"",
            "progress": "90%",
            "answersLocked": False
        }    
    }
