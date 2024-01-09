from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http  import HttpResponse


def school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sl=SFDO.cleaned_data['Slocation']
            sp=SFDO.cleaned_data['Sprincipal']
            e=SFDO.cleaned_data['email']
            r=SFDO.cleaned_data['renteremail']
            SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp,email=e,renteremail=r)[0]
            
            return HttpResponse('School is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'school.html',d)