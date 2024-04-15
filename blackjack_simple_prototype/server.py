from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

lessons = {  
    "1":{
        "lesson_id": "1",
        "title": "What is blackjack and how does a player win or lose?",
        "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/how-do-you-play-blackjack.jpg",
        "media_alt":"Lesson 1 media alt text",
        "text": "Goal of blackjack is to beat the dealer.....",
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
        }                                 
}

quiz_questions = {  
    "1":{
        "quiz_id": "1",
        "quiz_question": "What are the possible values of this hand?",
        "media":"https://decksandstacks.com/wp-content/uploads/2023/07/Example-of-a-soft-hand-in-Blackjack.png",
        "media_alt":"Quiz question 1 media alt text",
        "panswers": ["16 and 6", "15 and 6", "16 only", "15 only"],
        "answer": 0,
        "next_question": "2",
        "client_response":""
        },
    "2":{
        "quiz_id": "2",
        "quiz_question": "What is the term for playing two hands when you're dealt two of the same card?",
        "media":"https://www.playojo.com/blog/wp-content/uploads/2020/11/1-3-768x509.jpg",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Breaking", "Dividing", "Splitting", "Seperating"],
        "answer": 2,
        "next_question": "3",
        "client_response":""
        },
    "3":{
        "quiz_id": "3",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak"],
        "answer": 1,
        "next_question": "4",
        "client_response":""
        },
    "4":{
        "quiz_id": "4",
        "quiz_question": "What does a soft hand mean?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["A hand with no face cards", "A bad hand", "A hand with an ace", "A hand with two identical cards"],
        "answer": 2,
        "next_question": "5",
        "client_response":""
        },
    "5":{
        "quiz_id": "5",
        "quiz_question": "Should you surrender?",
        "media":"/static/assets/images/surrender.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["No, I should hit", "No, I should stand", "No, I should double", "Yes"],
        "answer": 3,
        "next_question": "6",
        "client_response":""
        },
    "6":{
        "quiz_id": "6",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak'"],
        "answer": 1,
        "next_question": "7",
        "client_response":""
        },
    "7":{
        "quiz_id": "7",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak'"],
        "answer": 1,
        "next_question": "8",
        "client_response":""
        },       
    "8":{
        "quiz_id": "8",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak'"],
        "answer": 1,
        "next_question": "end",
        "client_response":""
        },
    "9":{
        "quiz_id": "9",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak'"],
        "answer": 1,
        "next_question": "10",
        "client_response":""
        },
    "10":{
        "quiz_id": "10",
        "quiz_question": "When is it good to take insurance?",
        "media":"/static/assets/images/insurance.png",
        "media_alt":"Quiz question 2 media alt text",
        "panswers": ["Always take insurance", "Never take insurance", "Only if you have a bad hand", "When you're caught in a losing streak'"],
        "answer": 1,
        "next_question": "end",
        "client_response":""
        },          
}

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):

    lesson = lessons[lesson_id]
    return render_template('learn.html', lesson = lesson)

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    
    question = quiz_questions[quiz_id]
    return render_template('quiz.html', question = question)

@app.route('/answer', methods=['POST'])
def answer():
    
   data = request.json
   answer_index = int(data.get('answerIndex'))
   quizID = data.get('quizId')
   if answer_index == quiz_questions[quizID]['answer']:
        result = "Correct"
   else:
        result = "Wrong, the correct answer was: " + quiz_questions[quizID]['panswers'][quiz_questions[quizID]['answer']]

   quiz_questions[quizID]['result'] = result
   quiz_questions[quizID]['client_response'] = quiz_questions[quizID]['panswers'][answer_index]
   
   return result

# skeleton code used to build up to midterm page 
# current_id = 2
# data = [
#     {
#         "id": 1,
#         "name": "michael scott"
#     },
#     {
#         "id": 2,
#         "name": "jim halpert"
#     },
# ]



# @app.route('/')
# def hello_world():
#    return 'Hello World'

# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name) 

# @app.route('/people')
# def people(name=None):
#     return render_template('people.html', data=data)  


# @app.route('/add_name', methods=['GET', 'POST'])
# def add_name():
#     global data 
#     global current_id 

#     json_data = request.get_json()   
#     name = json_data["name"] 
    
#     # add new entry to array with 
#     # a new id and the name the user sent in JSON
#     current_id += 1
#     new_id = current_id 
#     new_name_entry = {
#         "name": name,
#         "id":  current_id
#     }
#     data.append(new_name_entry)

#     #send back the WHOLE array of data, so the client can redisplay it
#     return jsonify(data = data)


if __name__ == '__main__':
   app.run(debug = True)


