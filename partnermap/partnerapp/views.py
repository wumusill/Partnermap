from django.shortcuts import render
from .models import Partner
from django.conf import settings

def home(request):

    return render(request, 'base.html')


def board(request):
    return render(request, 'board.html')


def intro(request):
    return render(request, 'intro.html')


def write(request):
    return render(request, 'write.html')


def humanity(request):

    context = {
        "api_key": settings.KAKAO_MAPS_API_KEY
    }

    partners = Partner.objects.all()

    return render(request, 'humanity.html')
    # return render(request, 'base.html', {'partners':partners})

def business(request):
    return render(request)




# def home(request):
#     # Post에 있는 모든 객체들을 가져오는 코드
#     # posts = Post.objects.all()
#     # Post의 객체를 filter를 통해 가져오는 코드
#     posts = Post.objects.filter().order_by('-date')
#     # 객체들의 목록을 끊어주는 코드
#     paginator = Paginator(posts, 5)
#     pagnum = request.GET.get('page')
#     posts = paginator.get_page(pagnum)
#     return render(request, 'index.html', {'posts':posts})
