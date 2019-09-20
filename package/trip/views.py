from django.shortcuts import render
from .form import Reg , login
from .models import tb_registration
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, "trip/index.html")
def about(request):
    return render(request, "trip/about.html")
def our_tour(request):
    return render(request, "trip/tours.html")
def destination(request):
    return render(request, "trip/destinations.html")
def contact(request):
    return render(request, "trip/contacts.html")
def home(request):
    return render(request, "trip/index.html")

def register(request):
    if request.method=='POST':
        form = Reg(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data["name"]
            email1 = form.cleaned_data["email"]
            contact1 = form.cleaned_data["contact"]
            password1 = form.cleaned_data["password"]
            p = tb_registration(name = name1, email = email1, contact = contact1, password = password1 )
            p.save()
            return HttpResponse("Thanks")
        else:
            return render(request,"trip/form.html", {'form': form})
    else:
        form = Reg()
        return render(request,"trip/form.html", {'form':form})

def logedin(request):
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            u_email = form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p = tb_registration.objects.filter(email=u_email,password=u_password)
            print(p)

            if (p.count()>0):
                request.session['username'] = u_email
                if request.session.has_key('username'):
                    u_name = request.session['username']
                    print(u_name)
                    print(p[0].name)

                return HttpResponse("Thanks")
            else:
                print("try again user")
                return HttpResponseNotFound('<h1>no page found</h1>')

        else:
              print('\n\n this is else block:{0}\n\n')
              return render(request, "trip/login.html", {'form': form})
    else:
        form = login()
        return render(request, "trip/login.html", {'form': form})
