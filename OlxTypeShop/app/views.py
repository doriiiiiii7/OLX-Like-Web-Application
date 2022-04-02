from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm, UpdateMyCustomerForm, AddOfferForm

import datetime

TEMPLATE_DIR = (
    'os.path.join(BASE_DIR, "templates")'
)


# Create your views here.


def search(request):
    if request.method == 'GET':
        name = request.GET.get('mysearch')
        print(name)
        result = Product.objects.all().filter(title__icontains=name) | Product.objects.all().filter(category__name__icontains=name) | Product.objects.all().filter(description__icontains=name)
        context = {'products': result}
    else:
        context = {}

    return render(request, 'marketplace/market.html', context)


def main(request):
    products = Product.objects.all()[:3]
    return render(request, 'marketplace/homepage.html', {'products': products})


def products(request):
    products = Product.objects.all()
    return render(request, 'marketplace/market.html', {'products': products})


def imobiliare(request):
    products = Product.objects.filter(category__name='Imobiliare')
    return render(request, 'marketplace/market.html', {'products': products})


def autovehicule(request):
    products = Product.objects.filter(category__name='Autovehicule')
    return render(request, 'marketplace/market.html', {'products': products})


def servicii(request):
    products = Product.objects.filter(category__name='Servicii')
    return render(request, 'marketplace/market.html', {'products': products})


def electronice_si_electrocasnice(request):
    products = Product.objects.filter(category__name='Electronice si electrocasnice')
    return render(request, 'marketplace/market.html', {'products': products})


def moda_si_frumusete(request):
    products = Product.objects.filter(category__name='Moda si frumusete')
    return render(request, 'marketplace/market.html', {'products': products})


def piese_auto(request):
    products = Product.objects.filter(category__name='Piese auto')
    return render(request, 'marketplace/market.html', {'products': products})


def casa_si_gradina(request):
    products = Product.objects.filter(category__name='Casa si gradina')
    return render(request, 'marketplace/market.html', {'products': products})


def animale_de_companie(request):
    products = Product.objects.filter(category__name='Animale de companie')
    return render(request, 'marketplace/market.html', {'products': products})


def alta_categorie(request):
    products = Product.objects.filter(category__name='Alta categorie')
    return render(request, 'marketplace/market.html', {'products': products})


def productClicked(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'marketplace/product.html', {'product': product})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('app:homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                new_phone_number = form.cleaned_data.get('phone_number')

                Customer.objects.create(
                    user=user,
                    name=user.username,
                    phone_number=new_phone_number
                )

                messages.success(request, 'Account was created for ' + username)

                return redirect('app:loginPage')

        context = {'form': form}
        return render(request, 'marketplace/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('app:homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('app:homepage')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'marketplace/login.html', context)


def logOutPage(request):
    logout(request)
    return redirect('app:homepage')


@login_required(login_url='/login')
def userAccount(request):
    context = {}
    return render(request, 'marketplace/main2.html', context)


@login_required(login_url='/login')
def myOffers(request):
    products = Product.objects.filter(added_by=request.user.customer)
    context = {'products': products}
    return render(request, 'marketplace/myproducts.html', context)


@login_required
def editProfile(request):
    form = UpdateMyCustomerForm(instance=request.user.customer)
    if request.method == 'POST':
        form = UpdateMyCustomerForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            return redirect('app:userAccount')
    context = {'form': form}
    return render(request, 'marketplace/editprofile.html', context)


@login_required
def editOffer(request, myid):
    form = AddOfferForm(instance=Product.objects.get(id=myid))
    if request.method == 'POST':
        form = AddOfferForm(request.POST, instance=Product.objects.get(id=myid))
        if form.is_valid():
            item = form.save()
            return redirect('app:myProducts')
    context = {'form': form}
    return render(request, 'marketplace/editoffer.html', context)


@login_required
def addOffer(request):
    form = AddOfferForm()
    if request.method == 'POST':
        form = AddOfferForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user.customer
            item.save()
            return redirect('app:myProducts')
    context = {'form': form}
    return render(request, 'marketplace/addoffer.html', context)


@login_required
def deleteOffer(request, myid):
    Product.objects.filter(id=myid).delete()
    return render(request, 'marketplace/myproducts.html', {})
