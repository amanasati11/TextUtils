from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'defaults')
    # Check checkbox Value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # Check checkbox is on
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyse the Text
        # return render(request, 'analyze.html', params)
    if fullcaps =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Remove Newline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcounter == "on":
        analyzed = ""
        for i in djtext:
            if i!="":
                analyzed = analyzed + i
        analyzed = "No of Character = " + str(len(analyzed))
        params = {'purpose': 'Char Counter', 'analyzed_text': analyzed}
    if removepunc != 'on' and fullcaps!= 'on' and newlineremover!='on' and spaceremover!='on'and charcounter!='on':
        return HttpResponse ("PLEASE SELECT SOME OPERATION.")
    return render(request, 'analyze.html', params)


