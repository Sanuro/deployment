from django.shortcuts import render, HttpResponse, redirect


def index(request):
    location = ["Mountain View", "Pool", "Rock", "Swamp", "China"]
    language = ["Javascript", "Python", "Chinese", "English"]
    
    return render(request, "survey_form/index.html", {"location" : location, "language" : language})

def process(request):
    request.session["your_name"] = request.POST["your_name"]
    request.session["commenter"] = request.POST["commenter"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]

    return redirect("/result")

def result(request):
    return render(request, "survey_form/result.html")