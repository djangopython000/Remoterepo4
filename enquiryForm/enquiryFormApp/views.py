from django.shortcuts import render

from .models import EnquiryData
from .forms import EnquiryForm
from django.http.response import HttpResponse

def enquiryView(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            skills=eform.cleaned_data.get('skills')
            locations=eform.cleaned_data.get('locations')
            gender=eform.cleaned_data.get('gender')
            date=eform.cleaned_data.get('date')

            data=EnquiryData(
                name=name,
                email=email,
                mobile=mobile,
                skills=skills,
                locations=locations,
                gender=gender,
                date=date
            )
            data.save()
            eform=EnquiryForm()
            return render(request,'enquiryform.html',{'eform':eform})
        else:
            return HttpResponse ("user invalid data")
    else:
        eform=EnquiryForm()
        return render(request,'enquiryform.html',{'eform':eform})
