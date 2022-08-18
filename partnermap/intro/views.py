from django.shortcuts import get_object_or_404, render
from .models import Partner, PartnerBusiness, PartnerHumanity
from django.core.paginator import Paginator


# 총학생회
def intro(request):
    partners = Partner.objects.all()
    paginator = Paginator(partners, 5)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'intro.html', {'partners':partners})


def humanity(request):
    # 인문대 제휴
    partners = PartnerHumanity.objects.all()
    paginator = Paginator(partners, 5)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerHumanity.objects.all().order_by('-like_count')[:5]
    return render(request, 'humanity.html', {'partners':partners, 'like_partners':like_partners})


def society(request):
    return render(request, 'society.html')


def science(request):
    return render(request, 'science.html')


def business(request):
    partners = PartnerBusiness.objects.all()
    paginator = Paginator(partners, 5)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerBusiness.objects.all().order_by('-like_count')[:5]
    return render(request, 'business.html', {'partners':partners, 'like_partners':like_partners})


def engine(request):
    return render(request, 'engine.html')


def elec(request):
    return render(request, 'elec.html')


def farm(request):
    return render(request, 'farm.html')


def teacher(request):
    return render(request, 'teacher.html')


def life(request):
    return render(request, 'life.html')


def vet(request):
    return render(request, 'vet.html')


def medicine(request):
    return render(request, 'medicine.html')


def doctor(request):
    return render(request, 'doctor.html')


def mixed(request):
    return render(request, 'mixed.html')