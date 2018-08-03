from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    # 方法一
    # return HttpResponse("Hello world ! ")

    # 方法二
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)