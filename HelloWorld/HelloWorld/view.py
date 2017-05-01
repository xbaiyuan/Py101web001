from django.http import HttpResponse

#定义函数
def hello(request):
    return HttpResponse("Hello world ! ")
