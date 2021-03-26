from django.shortcuts import render

# Create your views here.
def index(request):
    content = {"text":'hello world', "number":20}
    return render(request, "index.html", context=content)

def other(request):
    return render(request, "other.html")

def relative(request):
    return render(request, "relative_url_templates.html")