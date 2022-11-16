from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return HttpResponse("Loaded")
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def settings(request):
    # return HttpResponse("Loaded")
    return render(request, 'settings.html')