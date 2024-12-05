"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.project,name="project"),
    path("viewusers/",views.viewusers,name="viewusers"),
    path("home/",views.home,name="home"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("signuppage/",views.signuppage,name="signuppage"),
    path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
    path("resetpassword/",views.resetpassword,name="resetpassword"),
 
    path("bookbus/",views.bookbuspage,name="bookbuspage"),
    path("busfilter/",views.busfilter,name="busfilter"),
    path("flightfilter/",views.flightfilter,name="flightfilter"),
    path("bookflight/",views.bookflightpage,name="bookflightpage"),
    path('fpaymentpage/', views.flightpaymentpage, name='fpaymentpage'),
    path('create_order/', views.create_order, name='create_order'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('confirmpayment/', views.confirmpayment, name='confirmpayment'),

    path("bpaymentpage/<str:travels>/<int:id>",views.bpaymentpage,name="bpaymentpage"),
   
   
   
    path("viewseats/<str:travels>",views.viewseats,name="viewseats"),
   
   
    path("aboutus/",views.aboutuspage,name="aboutuspage"),
    path("flightticketdetails/<str:flight>",views.flightticketdetails,name="flightticketdetails"),
  
    path("flightticketconfirm/",views.flightticketconfirm,name="flightticketconfirm"),
  
    path("profile/",views.profile,name="profile"),
   
  
    path("booked/",views.booked,name="booked"),
    path("date/",views.demodate,name="demodate"),
    path("logout/",views.logout,name="logout"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
