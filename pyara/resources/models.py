from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.email


class Question(models.Model):
    GENERAL = 'GEN'
    BASIC = 'BAS'
    COLLECTIONS = 'COL'
    FUNCTION = 'FUN'
    OOP = 'OOP'
    FILE = 'FIL'
    ALGORITHM = 'ALG'
    SUBJECT_CHOICES = [
        (GENERAL, 'General information'),
        (BASIC, 'Basic data types and syntax'),
        (COLLECTIONS, 'Built-in data types used to store collections of data'),
        (FUNCTION, 'Functions'),
        (OOP, 'Object Oriented Programming'),
        (FILE, 'Files handling'),
        (ALGORITHM, 'Algorithms'),
    ]

    subject = models.CharField(
        max_length=3,
        choices=SUBJECT_CHOICES,
        default=GENERAL)

    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True)
    source = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    date = models.DateField(default=timezone.now)
    answer = models.TextField()
    source = models.CharField(max_length=200, blank=True)
    drawing = models.ImageField(upload_to='images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.answer}'
