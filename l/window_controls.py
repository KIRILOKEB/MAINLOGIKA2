from PySide6.QtCore import *
from PySide6.QtWidgets import *

from main_window import *
from menu_window import *

from questions_controller import *

q1 = Question(
    question="Скільки 5+5?",
    answer="9",
    wrong_answer1="10",
    wrong_asnwer2="20",
    wrong_answer3="45"
)

q2 = Question(
    question="Когда создали Among Us?",
    answer="вчора",
    wrong_answer1="2025",
    wrong_asnwer2="2077",
    wrong_answer3="завтра"
)

question_controller = QuestionController()
question_controller.add_answer(q1)
question_controller.add_answer(q2)

def show_questions():
    result_gbox.hide()
    answers_gbox.show()
    question_controller.show_question()
    
def show_results():
    result_gbox.show()
    answers_gbox.hide()
    
def check_answer():
    if give_answer_pbtn.text() == "Відповісти":
        show_results()
        give_answer_pbtn.setText("Наступне питання")
        
    elif give_answer_pbtn.text() == "Наступне питання":
        show_questions()
        give_answer_pbtn.setText("Відповісти")
    
def show_menu():
    window_menu.show()
    window_main.hide()
    
def show_main():
    window_main.show()
    window_menu.hide()
    
def connect_buttons():
    menu_pbtn.clicked.connect(show_menu)
    give_answer_pbtn.clicked.connect(check_answer)
    back_to_main_pbtn.clicked.connect(show_main)
    