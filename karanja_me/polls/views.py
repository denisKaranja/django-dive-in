from django.shortcuts import render
from django.shortcuts import HttpResponse

# entry point of the polls app
def index(request):
  return HttpResponse("Hello world, you're at Polls entry point")


def detail(request, question_id):
  return HttpResponse("You're looking at question {}.".format(question_id))

def results(request, question_id):
  response = "You're looking at the results of question %s"
  return HttpResponse(response % question_id)

def vote(resuest, question_id):
  return HttpResponse("You're voting on question {}".format(question_id))