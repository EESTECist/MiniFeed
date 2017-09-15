from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html", context={"name": "Osman", "range10": range(10)})
