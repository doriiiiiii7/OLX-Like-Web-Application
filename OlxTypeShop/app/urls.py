from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.main, name='main'),
    path('market/', views.products, name="market"),
    path('homepage/', views.main, name="homepage"),
    path('market/category/imobiliare/', views.imobiliare, name="imobiliare"),
    path('market/category/autovehicule/', views.autovehicule, name="autovehicule"),
    path('market/category/servicii/', views.servicii, name="servicii"),
    path('market/category/electronice-si-electrocasnice/', views.electronice_si_electrocasnice, name="electronice-si-electrocasnice"),
    path('market/category/moda-si-frumusete/', views.moda_si_frumusete, name="moda-si-frumusete"),
    path('market/category/piese-auto/', views.piese_auto, name="piese-auto"),
    path('market/category/casa-si-gradina/', views.casa_si_gradina, name="casa-si-gradina"),
    path('market/category/animale-de-companie/', views.animale_de_companie, name="animale-de-companie"),
    path('market/category/alta-categorie/', views.alta_categorie, name="alta-categorie"),
    path('market/<int:myid>', views.productClicked, name="productClicked"),
    path('register/', views.registerPage, name="registerPage"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logOutPage, name="logoutPage"),
    path('myAccount/', views.userAccount, name="userAccount"),
    path('myAccount/editProfile/', views.editProfile, name="editProfile"),
    path('myAccount/myProducts/', views.myOffers, name="myProducts"),
    path('myAccount/addOffer/', views.addOffer, name="addOffer"),
    path('myAccount/editOffer/<int:myid>/', views.editOffer, name="editProduct"),
    path('myAccount/deleteOffer/<int:myid>/', views.deleteOffer, name="deleteOffer"),
    path('market/search/', views.search, name="search"),
]