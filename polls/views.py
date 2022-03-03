from urllib import response
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world . Your're at the polls index.")

# Create your views here.
def detail(request, question_id):
    return HttpResponse("you're looking at question %s."% question_id)

def results(request, question_id):
    response = "your're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)