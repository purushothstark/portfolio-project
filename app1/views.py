from django.shortcuts import render, redirect
from app1.models import HtmlContact

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def purushothaman(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        message = request.POST.get('Message')

        print(name, email, message)
        data = HtmlContact(name=name, email=email, message=message)
        data.save()
        return redirect('/')
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')
