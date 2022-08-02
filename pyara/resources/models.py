from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.email

class Answear(models.Model):
    date=models.DateField()
    slug = models.SlugField(unique=True)
    answear = models.TextField()
    source = models.URLField()
#    drawing = models.ImageField(upload_to='drawings')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.slug} - {self.author}'

class Question(models.Model):
    GENERAL = 'GEN'
    LIST = 'LIS'
    DICTIONARIE = 'DIC'
    STRING = 'STR'
    TUPLE = 'TUP'
    SET = 'SET'
    FUNCTION = 'FUN'
    OOP = 'OOP'
    FILE = 'FIL'
    ALGORITHM = 'ALG'
    SUBJECT_CHOICES = [
        (GENERAL, 'General'),
        (LIST, 'Lists'),
        (DICTIONARIE, 'Dictionaries'),
        (STRING, 'Strings'),
        (TUPLE, 'Tuples'),
        (SET, 'Sets'),
        (FUNCTION, 'Functions'),
        (OOP, 'Object Oriented Programming'),
        (FILE, 'Files handling'),
        (ALGORITHM, 'Algorithms'),
    ]
    subject = models.CharField(
        max_length = 3,
        choices = SUBJECT_CHOICES,
        default = GENERAL)
    title = models.CharField(max_length=200)
    date=models.DateField()
    slug = models.SlugField(unique=True)
    source = models.URLField()
    answear = models.ForeignKey(Answear, blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
