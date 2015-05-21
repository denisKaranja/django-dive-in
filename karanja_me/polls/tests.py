import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionMethodTest(TestCase):

  def test_was_published_recently_with_future_question(self):
    """
    was_published_recenlty() should return False for questions that the
    pub_date is in the future
    """
    time = timezone.now() + datetime.timedelta(days = 30)
    future_question = Question(pub_date = time)
    self.assertEqual(future_question_was_published_recently(), False)

