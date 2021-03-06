import datetime
from .models import Question
from django.test import TestCase
from django.utils import timezone
class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time=timezone.now()+datetime.timedelta(days=30)
		future_question=Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(),False)

	def test_was_published_recently_with_recent_question(self):
		time=timezone.now()
		recent_question=Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(),True)
		


