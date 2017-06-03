from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

class Human(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

@python_2_unicode_compatible  # only if you need to support Python 2

class Author(Human):
	author_type = models.CharField(max_length=24)
	def __str__(self):
		return self.first_name + " " + self.last_name

@python_2_unicode_compatible  # only if you need to support Python 2


class Faculty(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

@python_2_unicode_compatible  # only if you need to support Python 2

class Writing(models.Model):
	name = models.CharField(max_length=200)
	size = models.IntegerField(default=0)
	def __str__(self):
		return self.name

@python_2_unicode_compatible  # only if you need to support Python 2

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    atype = models.ForeignKey(Writing, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='UNDEFINED')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True);

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.published_date <= now

    def __str__(self):
        return self.title

