from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.conf import settings
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def board(request):
    posts = Post.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5)
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request, 'board.html', {"posts":posts})


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "detail.html", {'post_detail':post_detail, "comment_form":comment_form})


def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)


def postcreate(request):
    # request method가 POST일 경우
    # 입력값 저장
    if request.method == "POST" or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('board')

    # requeset method가 GET일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {"form":form})




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
