from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

# Importing the lessons and quiz questions
from lessons import lessons
from questions import quiz_questions

app = Flask(__name__)


########################
#        ROUTES        #
########################

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/lesson/<module_id>/<lesson_id>')
def lesson(module_id, lesson_id):

    lesson = lessons[module_id][lesson_id]
    return render_template('lesson.html', lesson = lesson)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/question/<module_id>/<quiz_id>')
def question(module_id, quiz_id):
    
    question = quiz_questions[module_id][quiz_id]
    return render_template('question.html', question = question)

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




if __name__ == '__main__':
   app.run(debug = True)


