import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Article
from .models import Author
from .models import Human
from .models import Faculty
from .models import Writing



class ArticleMethodTests(TestCase):

    def test_was_published_recently_with_future_article(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(published_date=time)
        self.assertEqual(future_article.was_published_recently(), False)

    def returns_string(self):

        future_title = Article(title='dfgh')
        self.assertTrue(future_title == string.empty)

class AuthorMethodTests(TestCase):

    def returns_vaid_string(self):

        future_name = Author(ifirst_name='abc', second_name='dfg')
        self.assertEqual(future_name.name.isempty, False)

class HumanMethodTests(TestCase):

    def returns_vaid_string(self):

        future_name = Author(name='abc')
        self.assertEqual(future_name.name.isempty, False)

class FacultyMethodTests(TestCase):

    def returns_vaid_string(self):

        future_name = Author(name='randomname')
        self.assertEqual(name.name.isempty, False)

class WritingMethodTests(TestCase):

    def returns_vaid_string(self):

        future_name = Author(name='randomname')
        self.assertEqual(name.name.isempty, False)



