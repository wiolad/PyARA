from django.test import TestCase

from .models import Question, User

from django.urls import reverse


# Create your tests here.
class QuestionsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_questions = 10
        for question_id in range(number_of_questions):
            Question.objects.create(title=f"question{question_id}", slug=f"slug_{question_id}", author=User.objects.first(), subject="GEN")

    def test_url_exists(self):
        question_subject = 'GEN'
        response = self.client.get(reverse('questions-list', args=[question_subject]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        question_subject = 'GEN'
        response = self.client.get(reverse('questions-list', args=[question_subject]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/questions.html')

