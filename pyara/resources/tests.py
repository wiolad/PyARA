from django.test import TestCase, RequestFactory

from .models import Question, User, Answer

from django.urls import reverse


# Test Views
class IndexViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get(reverse('index-view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/index.html')


class QuestionsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='jacob', email='jacob@gmail.com')
        number_of_questions = 10
        for question_id in range(number_of_questions):
            Question.objects.create(title=f"question{question_id}", slug=f"slug_{question_id}",
                                    author=User.objects.first(), subject="GEN")

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


# Test Models
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 3
        for user_id in range(number_of_users):
            User.objects.create(name=f'name_{user_id}', email=f'user_{user_id}@gmail.com')

    def test_user_creation(self):
        user = User.objects.first()
        self.assertTrue(isinstance(user, User))

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_user_string_method(self):
        user = User.objects.get(id=1)
        expected_string = f'User name: {user.name}'
        self.assertEqual(str(user), expected_string)

        class UserModelTest(TestCase):
            @classmethod
            def setUpTestData(cls):
                number_of_users = 3
                for user_id in range(number_of_users):
                    User.objects.create(name=f'name_{user_id}', email=f'user_{user_id}@gmail.com')

            def test_user_creation(self):
                user = User.objects.first()
                self.assertTrue(isinstance(user, User))

            def test_user_name_max_length(self):
                user = User.objects.get(id=1)
                max_length = user._meta.get_field('name').max_length
                self.assertEqual(max_length, 100)

            def test_user_string_method(self):
                user = User.objects.get(id=1)
                expected_string = f'User name: {user.name}'
                self.assertEqual(str(user), expected_string)


class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='jacob', email='jacob@gmail.com')
        number_of_questions = 10
        for question_id in range(number_of_questions):
            Question.objects.create(title=f"question{question_id}", slug=f"slug_{question_id}",
                                    author=User.objects.first(), subject="GEN")

    def test_question_creation(self):
        question = Question.objects.first()
        self.assertTrue(isinstance(question, Question))

    def test_question_name_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_question_string_method(self):
        question = Question.objects.get(id=1)
        expected_string = f'{question.title}'
        self.assertEqual(str(question), expected_string)


class AnswerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='jacob', email='jacob@gmail.com')
        Question.objects.create(title='How to?', source='www.onet.pl', author=User.objects.first(), subject='GEN')
        number_of_answers = 3
        for answer_id in range(number_of_answers):
            Answer.objects.create(question=Question.objects.first(), answer=f'answer_{answer_id}',
                                  author=User.objects.first(), source=f'source_{answer_id}')

    def test_answer_creation(self):
        answer = Answer.objects.first()
        self.assertTrue(isinstance(answer, Answer))

    def test_answer_name_max_length(self):
        answer = Answer.objects.get(id=1)
        max_length = answer._meta.get_field('source').max_length
        self.assertEqual(max_length, 200)

    def test_answer_string_method(self):
        answer = Answer.objects.get(id=1)
        expected_string = f'{answer.answer}'
        self.assertEqual(str(answer), expected_string)