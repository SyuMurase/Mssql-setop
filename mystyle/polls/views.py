from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")
def index2(request):
    return HttpResponse("Hello, world.")
def index3(request):
    return HttpResponse("!!!")