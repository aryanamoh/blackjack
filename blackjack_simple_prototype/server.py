from flask import Flask, render_template, Response, request, jsonify

# Importing the lessons and quiz questions
from lessons import lessons
from questions import quiz_questions

score = 0

app = Flask(__name__)
@app.errorhandler(404) 


########################
#        ROUTES        #
########################

def not_found(e): 
  return render_template("404.html") 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    global quiz_questions 
    global score
    tmp = score 
    score = 0
    total = int(len(quiz_questions))
    return render_template('results.html', score = tmp, total=total)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/quiz_start')
def quiz_start():
    return render_template('quiz_start.html')

@app.route('/lesson/<module_id>/<lesson_id>')
def lesson(module_id, lesson_id):

    lesson = lessons[module_id][lesson_id]
    return render_template('lesson.html', lesson = lesson, module_id = module_id, lesson_id = lesson_id)

@app.route('/lesson_complete/<module_id>')
def lesson_complete(module_id):
    
    lesson = lessons[module_id]
    return render_template('lesson_complete.html', module_id = module_id, lesson = lesson)


@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    question = quiz_questions[quiz_id]
    return render_template('quiz.html', question = question, index=quiz_id)

@app.route('/client', methods=['POST'])
def client():
    data = request.json
    # grab the current module and lesson to update client's start time
    formattedTime = data["formattedTime"]
    pathname = data["pathname"]
    # splits the string by the delimiter "/"
    pathname_parts = pathname.split("/")
    # grab the last two strings 
    module_id, lesson_id = pathname_parts[-2:]
    #update user's start time 
    lessons[module_id][lesson_id]["start_time"] = data["formattedTime"]
    
    # uncomment if you wish to see the updated time for each lesson
    # print(lessons[module_id][lesson_id]["start_time"])
    return lessons[module_id][lesson_id]

@app.route('/answer', methods=['POST'])
def answer():
    
   data = request.json
   answer_index = int(data.get('answerIndex'))
   quizID = data.get('quizId')
   if answer_index == quiz_questions[quizID]['answer']:
        result = "Correct!"
        global score 
        score += 1
   else:
        result = "Wrong, the correct answer was: " + quiz_questions[quizID]['panswers'][quiz_questions[quizID]['answer']]

   quiz_questions[quizID]['result'] = result
   quiz_questions[quizID]['client_response'] = quiz_questions[quizID]['panswers'][answer_index]
   
   return result




if __name__ == '__main__':
   app.run(debug = True)


