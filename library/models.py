from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_born = models.DateField()
    date_of_death = models.DateField()
    occupations = models.CharField(max_length=50)
    LANGUAGE_CHOICES = (
        ('UKRAINIAN', 'ua'),
        ('RUSSIAN', 'ru'),
        ('ENGLISH', 'en'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='ENGLISH')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pub_date = models.DateField()
    LANGUAGE_CHOICES = (
        ('UKRAINIAN', 'ua'),
        ('RUSSIAN', 'ru'),
        ('ENGLISH', 'en'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='ENGLISH')

    def __str__(self):
        return self.name
