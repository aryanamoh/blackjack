from flask import Flask, redirect, url_for, render_template, Response, request, jsonify

# Importing the lessons and quiz questions
from lessons import lessons
from questions import quiz_questions

progress = "0%"
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
    for question_id, question_data in quiz_questions.items():
        if question_data['answersLocked'] == False:
            quiz_id = question_data['quiz_id']
            return redirect(url_for('quiz', quiz_id=quiz_id))
     
    score = 0
    for question_id, question_data in quiz_questions.items():
    
        client_response = question_data["client_response"]
        correct_answer = question_data["panswers"][question_data["answer"]]
    
    
        if client_response == correct_answer:
       
            score += 1
    total = int(len(quiz_questions))
    return render_template('results.html', score = score, total=total, questions = quiz_questions)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/go_to_quiz')
def go_to_quiz():
    goto = "0"
    for question_id, question_data in quiz_questions.items():
        if question_data['answersLocked'] == False:
            goto = question_data['quiz_id']
            break;
    return goto

@app.route('/learn_table')
def learn_table():
    return render_template('learn_table.html')

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
    for i in range(1, int(quiz_id)):
        i_str = str(i)
        if quiz_questions[i_str]['answersLocked'] == False:
            quiz_id = quiz_questions[i_str]['quiz_id']
            question = quiz_questions[quiz_id]
            return redirect(url_for('quiz', quiz_id=quiz_id))
            break;
    return render_template('quiz.html', question = question, index=quiz_id, progress=progress)

@app.route('/retake')
def retake():
    global progress
    quiz_id = "1"
    progress = "0%"
    question = quiz_questions[quiz_id]
    for question_id, question_data in quiz_questions.items():
        question_data['answersLocked'] = False
        question_data['client_response'] = ""

    return render_template('quiz.html', question = question, index=quiz_id, progress=progress)

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
   global progress
   data = request.json
   answer_index = int(data.get('answerIndex'))
   quizID = data.get('quizId')
   if answer_index == quiz_questions[quizID]['answer']:
        result = "Correct!"
        
   else:
        result = "Wrong, the correct answer was: " + quiz_questions[quizID]['panswers'][quiz_questions[quizID]['answer']]

   quiz_questions[quizID]['result'] = result
   quiz_questions[quizID]['answersLocked'] = True
   quiz_questions[quizID]['client_response'] = quiz_questions[quizID]['panswers'][answer_index]
   progress_value = int(progress[:-1])  # Remove the '%' sign and convert to integer
    # Increase progress by 10%
   progress_value += 10
    # Limit progress to 100%
   progress_value = min(progress_value, 100)
    # Convert progress back to string format
   progress = f"{progress_value}%"
   
   return result




if __name__ == '__main__':
   app.run(debug = True)


