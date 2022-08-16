from django.shortcuts import render
from .models import Partner, PartnerBusiness, PartnerHumanity
from django.core.paginator import Paginator

# Create your views here.

# def board(request):
#     posts = Post.objects.filter().order_by('-date')
#     paginator = Paginator(posts, 5)
#     pagenum = request.GET.get('page')
#     posts = paginator.get_page(pagenum)
#     return render(request, 'board.html', {"posts":posts})

def intro(request):
    partners = Partner.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'intro.html', {'partners':partners})


def humanity(request):
    partners = PartnerHumanity.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    # return render(request, 'humanity.html')
    return render(request, 'humanity.html', {'partners':partners})

def business(request):
    partners = PartnerBusiness.objects.all()
    paginator = Paginator(partners, 10)
    pagenum = request.GET.get('page')
    partners = paginator.get_page(pagenum)
    return render(request, 'business.html', {'partners':partners})