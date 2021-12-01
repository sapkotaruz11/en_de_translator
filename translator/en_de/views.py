from django.http.request import HttpRequest
from django.shortcuts import render
from . import translator
# Create your views here.


def home(request):
    return render(request, 'base.html')

def translate(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        method = request.POST.get('select')
        if method == "1":
            answer = translator.ger_eng_translate(question)
        else:
            answer = translator.eng_ger_translate(question)
    return render(request, 'base.html', {'question': question, 'answers' : answer})