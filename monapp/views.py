from django.shortcuts import get_object_or_404, redirect, render,redirect
from django.contrib import messages
from .models import Category, Contact, Portfolio

# Create your views here.


def home(request, category_slug=None):
    portfolios=Portfolio.objects.all()
    categories=Category.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        portfolios=Portfolio.objects.filter(categorie=category)



    return render(request,'monapp/index.html',{'categories': categories, 'portfolios':portfolios} )



def portfolio_detail(request, my_id):
     portfolios=Portfolio.objects.get(id=my_id) 
     
     
     return render(request,'monapp/portfolio-details.html', {'portfolios': portfolios})





def service(request):


    return render(request,'monapp/service.html')



    def video(request):
        videos=Video.objects.all()
        return render(request, 'monapp/index.html', { 'videos':videos})













def vue_contact(request):
    message = "" 
    if request.method == 'POST':
        nom = request.POST.get('nom') 
        email = request.POST.get('email') 
        sujet = request.POST.get('sujet') 
        description = request.POST.get('description')
        contact = Contact.objects.create(nom=nom, email=email, sujet=sujet, description=description)
        contact.save()
        message= "Message envoyé avec succès"  # Utilisation de messages.success()
        # return redirect('contact')  # Redirection après l'envoi du formulaire

    return render(request, 'monapp/contact.html', {'message': message })
