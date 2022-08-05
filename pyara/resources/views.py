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
    if request.method == "GET":
        question_form = QuestionForm()
    else:
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            title = question_form.cleaned_data['title']
            source = question_form.cleaned_data['source']
            author = question_form.cleaned_data['author']
            subject = question_form.cleaned_data['subject']
            answear = question_form.cleaned_data['answear']
            question, _ = Question.objects.get_or_create(title=title, source=source, author=author, subject = subject, answear = answear)
        else:
            print("NOT VALID")

#        if registration_form.is_valid():
#            user_email = registration_form.cleaned_data['email']
#            participant, _ = Participant.objects.get_or_create(email=user_email)
#            selected_meetup.participants.add(participant)
#            return redirect('confirm-registration', meetup_slug=meetup_slug)

    return render(request, 'resources/questions.html',{
            'questions': selected_subject,
            'form': question_form,
            })

def single_question(request):
    return render(request, 'resources/single.html')
