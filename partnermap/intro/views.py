from django.shortcuts import render
from .models import Partner, PartnerHumanity

# Create your views here.
def intro(request):
    return render(request, 'intro.html')


def humanity(request):
    partners = PartnerHumanity.objects.all()

    # return render(request, 'humanity.html')
    return render(request, 'humanity.html', {'partners':partners})

def business(request):
    return render(request)