from django.shortcuts import get_object_or_404, render
from .models import Partner, PartnerAll, PartnerBusiness, PartnerHumanity
from django.core.paginator import Paginator


def intro(request):
    partners = Partner.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'intro.html', {'partners':partners})


def humanity(request):
    # 인문대 제휴
    partners = PartnerHumanity.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'humanity.html', {'partners':partners})


def business(request):
    partners = PartnerBusiness.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'business.html', {'partners':partners})


