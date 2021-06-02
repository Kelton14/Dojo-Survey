from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request):
    if 'name' not in request.session:
        request.session['name'] = "Buzz Lightyear"
    if 'location' not in request.session:
        request.session['location'] = "Nowhere"
    if 'language' not in request.session:
        request.session['language'] = "English"
    if 'textbox' not in request.session:
        request.session['textbox'] = "Words"

    context = {
        "name" : request.session['name'],
        "location" : request.session['location'],
        "language" : request.session['language'],
        "textbox" : request.session['textbox'],
    }

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['textbox'] = request.POST['textbox']

    return render(request, "result.html", context, request.session)
