from django.shortcuts import render
#from django.http import HttpResponse

from .models import Question, Answer

from .forms import QuestionForm
from .forms import AnswerForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'resources/index.html',{
    'questions':questions
    })
#    return HttpResponse('Welcome to PyARA - Python Amazing Resources App!')

def questions(request, question_subject):
    selected_subject = Question.objects.filter(subject=question_subject)
    selected_answers = Answer.objects.all()
    if request.method == "GET":
        question_form = QuestionForm()
    else:
        question_form = QuestionForm(request.POST)
#        AnswerFormSet = inlineformset_factory(Question, Answer, fields=('answer','date'))
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
    """
    Show question and answers
    """
    selected_answers = Answer.objects.filter(question=question_id)
    answer_form = AnswerForm()
    return render(request, 'resources/answers.html',{
            'answers': selected_answers,
            'form': answer_form,
            })


def single_question(request):
    return render(request, 'resources/single.html')
