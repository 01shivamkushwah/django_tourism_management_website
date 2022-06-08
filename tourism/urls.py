"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from tourism import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('rajashtan/',views.rajashtant),
    path('bihar/',views.biharr),
    path('hariyana/',views.hariyanaa),
    path('punjab/',views.punjabb),
    path('assam/',views.assamm),
    path('madhya_pradesh/',views.madhya_pradeshh),
    path('karnataka/',views.karnatakaa),
    path('gujrat/',views.gujratt),
    path('maharashtra/',views.maharashtraa),
     path('',views.home),
     path('andaman_and_nicobar/',views.andaman_and_nicobar_islandd),
     path('andhra_pradesh/',views.andhra_pradeshh),
     path('arunachal_pradesh/',views.arunachal_pradeshh),
     path('chhattisgarh/',views.chattisgarhh),
     path('delhi/',views.delhii),
     path('goa/',views.goaa),
     path('himachal_pradesh/',views.himachal_pradeshh),
     path('jammu_and_kashmir/',views.jammu_and_kashmirr),
     path('jharkhand/',views.jharkhandd),
     path('kerala/',views.kerlaa),
     path('ladakh/',views.ladakhh),
     path('manipur/',views.manipurr),
    path('meghalaya/',views.meghalayaa),
    path('mizoram/',views.mizoramm),
    path('nagaland/',views.nagalandd),
    path('odisha/',views.odishaa),
    path('sikkim/',views.sikkimm),
    path('tamilnadu/',views.tamilnaduu),
    path('telangana/',views.telanganaa),
    path('contactus/',views.contactus,name="saveenquiry"),
    path('famousplace/',views.famous),
    path('tajmahal/',views.taj),
    path('jaisalmer/',views.jai),
    path('newdelhi/',views.new),
    path('amritsar/',views.amr),
    path('varanasi/',views.var),
    path('goa_beach/',views.gb),
    path('aboutus/',views.about),
    path('home/',views.home1)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)