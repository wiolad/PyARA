from django import forms
from .models import Question
from .models import Answear

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','source','author','subject','answear']
