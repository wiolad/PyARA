from django.test import TestCase, RequestFactory

from .models import Question, User, Answer

from django.urls import reverse

# Test Views


class QuestionsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='jacob', email='jacob@gmail.com')
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


class AnswersViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='jacob', email='jacob@gmail.com')
        Question.objects.create(title='How to?', source='www.onet.pl', author=User.objects.first(), subject='GEN')
        number_of_answers = 3
        for answer_id in range(number_of_answers):
            Answer.objects.create(question=Question.objects.first(), answer=f'answer_{answer_id}',
                                  author=User.objects.first(), source=f'source_{answer_id}')

    def test_url_exists(self):
        response = self.client.get(reverse('answers-list', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('answers-list', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/answers.html')
