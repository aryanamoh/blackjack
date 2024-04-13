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
        "quiz_question": "Some question in Blackjack?",
        "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/Blackjack-hand-signal-for-standing-1.jpg",
        "media_alt":"Quiz question 1 media alt text",
        "text": "Drop something in this template spot",
        "answer":"Dynamically hide this element until user answers",
        "next_question": "2",
        "client_response":""
        },
    "2":{
        "quiz_id": "2",
        "quiz_question": "2nd question for the Blackjack?",
        "media":"https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/blackjack-hand-signal-doubling-down-1.jpg",
        "media_alt":"Quiz question 2 media alt text",
        "text": "Some text portion of the template",
        "answer":"Dynamically hide this element until user answers",
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


