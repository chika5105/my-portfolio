from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


# Create your views here.

def index(request):
    """
    View function for HomePage
    """
    form = ContactForm()
    context = {
        'form': form
       
        }
    return render(request, 'index.html', context = context)

def contact_me(request):
    contact = Contact()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message') 
        contact.image = request.POST.get('image')
        contact.save()
        alert = 'Your message has been sent successfully'
        context = {
            'alert': alert

        }
        return render(request, 'contact_successful.html', context = context)

    else:
        return render(request, 'index.html', context= context)