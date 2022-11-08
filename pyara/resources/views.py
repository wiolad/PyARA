from django.shortcuts import render

from .models import Question, Answer

from .forms import QuestionForm
from .forms import AnswerForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'resources/index.html',{
    'questions':questions
    })

def questions(request, question_subject):
    selected_subject = Question.objects.filter(subject=question_subject)
    selected_answers = Answer.objects.all()
    if request.method == "GET":
        question_form = QuestionForm()
    else:
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            title = question_form.cleaned_data['title']
            source = question_form.cleaned_data['source']
            author = question_form.cleaned_data['author']
            subject = question_form.cleaned_data['subject']
            question, _ = Question.objects.get_or_create(title=title, source=source, author=author, subject = subject)
        else:
            print("NOT VALID")

    return render(request, 'resources/questions.html',{
            'questions': selected_subject,
            'answers': selected_answers,
            'form': question_form,
            })


def answers(request, question_id):
    selected_answers = Answer.objects.filter(question=question_id)
    selected_question = Question.objects.get(id=question_id)
    if request.method == "GET":
        answer_form = AnswerForm(initial={'question': question_id})
    else:
        answer_form = AnswerForm(request.POST, initial={'question': question_id})
        if answer_form.is_valid():
            question = answer_form.cleaned_data['question']
            answer = answer_form.cleaned_data['answer']
            source = answer_form.cleaned_data['source']
            author = answer_form.cleaned_data['author']
            date = answer_form.cleaned_data['date']
            drawing = answer_form.cleaned_data['drawing']
            answer, _ = Answer.objects.get_or_create(question=question, answer=answer, source=source, author=author, date=date, drawing=drawing)
        else:
            print("NOT VALID")

            fields = ['question', 'answer', 'source', 'author', 'date', 'drawing']

    return render(request, 'resources/answers.html', {
            'answers': selected_answers,
            'question': selected_question,
            'form': answer_form,
            })


def single_question(request):
    return render(request, 'resources/single.html')
