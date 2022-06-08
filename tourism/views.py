from django.http import HttpResponse
from django.shortcuts import render
from rajashtan.models import rajashtan
from assam.models import assam
from gujrat.models import gujrat
from karnataka.models import karnataka
from maharashtra.models import maharashtra
from madhya_pradesh.models import madhya_pradesh
from panjab.models import panjab
from bihar.models import bihar
from hariyana.models import hariyana
from telengana.models import telengana
from andaman_and_nicobar_island.models import andaman_and_nicobar_island
from andhra_pradesh.models import andhra_pradesh
from arunachal_pradesh.models import arunachal_pradesh
from chattisgarh.models import chattisgarh
from delhi.models import delhi
from goa.models import goa
from himachal_pradesh.models import himachal_pradesh
from jammu_and_kashmir.models import jammu_and_kashmir
from jharkhand.models import jharkhand
from kerla.models import kerla
from manipur.models import manipur
from tamilnadu.models import tamilnadu
from ladakh.models import ladakh
from sikkim.models import sikkim
from contactpage.models import contact
from famousplace.models import famousplace
from odisha.models import odisha
from nagaland.models import nagaland
from mizoram.models import mizoram
from meghalaya.models import meghalaya
def contactus(request):
    n=''
    if request.method=="POST":
       s1 = request.POST.get('name')
       s2 = request.POST.get('surname')
       s3 = request.POST.get('email')
       s4 = request.POST.get('subject')
      #  print(s1,s2)
    #    print(type(contact),type(Person))
       en = contact(name = s1,surname = s2,email=s3,subject=s4)

       en.save()
       n='Inserted Data Successfully'
    return render(request,"contactus.html",{'t':n})

def home1(request):
       return render(request,"home.html")
def about(request):
       return render(request,"about_us.html")

def home(request):
   return render(request,"home.html")

def taj(request):
      return render(request,"tajmahal.html")

def gb(request):
      return render(request,"beach.html")

def var(request):
      return render(request,"varanasi.html")
   
def amr(request):
      return render(request,"amritsar.html")

def new(request):
      return render(request,"newdelhi.html")

def jai(request):
      return render(request,"jaisalmer.html")
def famous(request):
   alldata = famousplace.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"famous.html",data)
def rajashtant(request):
   alldata = rajashtan.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"rajashtan.html",data)
def hariyanaa(request):
   alldata = hariyana.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"hariyana.html",data)
def gujratt(request):
   alldata = gujrat.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"gujrat.html",data)
def biharr(request):
   alldata = bihar.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"bihar.html",data)
def punjabb(request):
   alldata = panjab.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"punjab.html",data)
def madhya_pradeshh(request):
   alldata = madhya_pradesh.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"madhyapradesh.html",data)
def assamm(request):
   alldata = assam.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"assam.html",data)
def karnatakaa(request):
    alldata = karnataka.objects.all()
    data = {
        'alldata' : alldata
    }
    return render(request,"karnataka.html",data)
def maharashtraa(request):
    alldata = maharashtra.objects.all()
    data = {
        'alldata' : alldata
    }
    return render(request,"mahrashtra.html",data)

def telanganaa(request):
   alldata = telengana.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"telangana.html",data)

def andaman_and_nicobar_islandd(request):
   alldata = andaman_and_nicobar_island.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"andaman_and_nicobar.html",data)

def andhra_pradeshh(request):
   alldata = andhra_pradesh.objects.all()
   data = {
        'alldata' : alldata
   }
   return render(request,"andhra_pradesh.html",data)

def arunachal_pradeshh(request):
   alldata = arunachal_pradesh.objects.all()
   data = {
        'alldata' : alldata
   }   
   return render(request,"arunachal_pradesh.html",data)

def chattisgarhh(request):
   alldata = chattisgarh.objects.all()
   data = {
        'alldata' : alldata
   }   
   return render(request,"chhatisgarh.html",data)

def delhii(request):
   alldata = delhi.objects.all()
   data = {
        'alldata' : alldata
   }   
   return render(request,"delhi.html",data)

def goaa(request):
   alldata = goa.objects.all()
   data = {
        'alldata' : alldata
   }   
   return render(request,"goa.html",data)

def himachal_pradeshh(request):
   alldata = himachal_pradesh.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"himachal_pradesh.html",data)

def jammu_and_kashmirr(request):
   alldata = jammu_and_kashmir.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"jak.html",data)

def jharkhandd(request):
   alldata = jharkhand.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"jharkhand.html",data)

def kerlaa(request):
   alldata = kerla.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"kerala.html",data)

def ladakhh(request):
   alldata = ladakh.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"ladakh.html",data)

def manipurr(request):
   alldata = manipur.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"manipur.html",data)

def meghalayaa(request):
   alldata = meghalaya.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"meghalaya.html",data)

def mizoramm(request):
   alldata = mizoram.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"mizoram.html",data)

def nagalandd(request):
   alldata = nagaland.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"nagaland.html",data)

def odishaa(request):
   alldata = odisha.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"odisha.html",data)

def sikkimm(request):
   alldata = sikkim.objects.all()
   data = {
        'alldata' : alldata
   }  
   return render(request,"sikkim.html",data)

def tamilnaduu(request):
   alldata = tamilnadu.objects.all()
   data = {
        'alldata' : alldata
   } 
   return render(request,"tamilnadu.html",data)

