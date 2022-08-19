from django.shortcuts import get_object_or_404, render
from .models import Partner, PartnerBusiness, PartnerDoctor, PartnerElec, PartnerEngine, PartnerFarm, PartnerHumanity, PartnerLife, PartnerMedicine, PartnerMixed, PartnerScience, PartnerSociety, PartnerTeacher, PartnerVet
from django.core.paginator import Paginator


# 총학생회
def intro(request):
    partners = Partner.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = Partner.objects.all().order_by('-like_count')[:3]
    return render(request, 'intro.html', {'partners':partners, 'like_partners':like_partners})


def humanity(request):
    # 인문대 제휴
    partners = PartnerHumanity.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerHumanity.objects.all().order_by('-like_count')[:3]
    return render(request, 'humanity.html', {'partners':partners, 'like_partners':like_partners})


def society(request):
    partners = PartnerSociety.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerSociety.objects.all().order_by('-like_count')[:3]
    return render(request, 'society.html', {'partners':partners, 'like_partners':like_partners})



def science(request):
    partners = PartnerScience.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerScience.objects.all().order_by('-like_count')[:3]
    return render(request, 'science.html', {'partners':partners, 'like_partners':like_partners})


def business(request):
    partners = PartnerBusiness.objects.all()
    paginator = Paginator(partners, 40)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerBusiness.objects.all().order_by('-like_count')[:3]
    return render(request, 'business.html', {'partners':partners, 'like_partners':like_partners})


def engine(request):
    partners = PartnerEngine.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerEngine.objects.all().order_by('-like_count')[:3]
    return render(request, 'engine.html', {'partners':partners, 'like_partners':like_partners})


def elec(request):
    partners = PartnerElec.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerElec.objects.all().order_by('-like_count')[:3]
    return render(request, 'elec.html', {'partners':partners, 'like_partners':like_partners})


def farm(request):
    partners = PartnerFarm.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerFarm.objects.all().order_by('-like_count')[:3]
    return render(request, 'farm.html', {'partners':partners, 'like_partners':like_partners})


def teacher(request):
    partners = PartnerTeacher.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerTeacher.objects.all().order_by('-like_count')[:3]
    return render(request, 'teacher.html', {'partners':partners, 'like_partners':like_partners})


def life(request):
    partners = PartnerLife.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerLife.objects.all().order_by('-like_count')[:3]
    return render(request, 'life.html', {'partners':partners, 'like_partners':like_partners})


def vet(request):
    partners = PartnerVet.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerVet.objects.all().order_by('-like_count')[:3]
    return render(request, 'vet.html', {'partners':partners, 'like_partners':like_partners})



def medicine(request):
    partners = PartnerMedicine.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerMedicine.objects.all().order_by('-like_count')[:3]
    return render(request, 'medicine.html', {'partners':partners, 'like_partners':like_partners})


def doctor(request):
    partners = PartnerDoctor.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerDoctor.objects.all().order_by('-like_count')[:3]
    return render(request, 'doctor.html', {'partners':partners, 'like_partners':like_partners})


def mixed(request):
    partners = PartnerMixed.objects.all()
    paginator = Paginator(partners, 15)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)

    like_partners = PartnerMixed.objects.all().order_by('-like_count')[:3]
    return render(request, 'mixed.html', {'partners':partners, 'like_partners':like_partners})