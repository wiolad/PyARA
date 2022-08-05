from django.shortcuts import render
#from django.http import HttpResponse

from .models import Question

from .forms import QuestionForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'resources/index.html',{
    'questions':questions
    })
#    return HttpResponse('Welcome to PyARA - Python Amazing Resources App!')

def questions(request, question_subject):
    selected_subject = Question.objects.filter(subject=question_subject)
    question_form = QuestionForm()
    return render(request, 'resources/questions.html',{
            'questions': selected_subject,
            'form': question_form,
            })

def single_question(request):
    return render(request, 'resources/single.html')
