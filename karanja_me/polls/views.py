from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Question
# entry point of the polls app
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)


def detail(request, question_id):
  return HttpResponse("You're looking at question {}.".format(question_id))

def results(request, question_id):
  response = "You're looking at the results of question %s"
  return HttpResponse(response % question_id)

def vote(resuest, question_id):
  return HttpResponse("You're voting on question {}".format(question_id))