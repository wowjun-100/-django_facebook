from django.shortcuts import render, redirect
from facebook.models import Article, Page, Comment


# Create your views here.

def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    choidogeun = '최도근'
    age = 20
    global count
    count = count + 1

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다, 4월 1일에 작성']

    return render(request, 'play2.html', { 'name': choidogeun, 'diary':diary, 'cnt': count, 'age': status })

def my_profile(request):
    return render(request, 'profile.html')

def my_event(request):
    choidogeun = '최도근'
    global count
    count+= 1
    if count == 7:
        result = '당첨!'
    else:
        result = '꽝...'

    return render(request, 'event.html', {'name': choidogeun, 'cnt': count, 'result' : result})

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )

        return redirect(f'/feed/{article.pk}')
    return render(request, 'detail_feed.html', {'feed': article})

def pages(request):
    article = Page.objects.all()
    return render(request, 'pages.html', {'articles': article})

def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != "" and request.POST['title'] != "" and request.POST['content'] != "" and request.POST['password'] !="":
            text = request.POST['content']
            text = text + '- 추신: 감사합니다.'
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )

            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')

        else:
            return redirect('/fail/')

    return render(request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')

        else:
            return redirect('/fail/')

    return render(request, 'edit_feed.html', {'feed': article})

def fail(request):
    return render(request, 'fail.html')

def page_new(request):
    if request.method == "POST":
        new_page = Page.objects.create(
            master = request.POST['master'],
            name = request.POST['name'],
            category = request.POST['category'],
            text = request.POST['text']
        )
        return redirect('/pages/')

    return render(request, 'page_new.html')

def edit_page(request, pk):
    article = Page.objects.get(pk=pk)
    if request.method == "POST":
        article.master = request.POST['master']
        article.name = request.POST['name']
        article.category = request.POST['category']
        article.text = request.POST['text']
        article.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'feed':article})

def remove_page(request, pk):
    article = Page.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', {'feed':article})

def remove_comment(request, comment_id, pk):
    article = Comment.objects.get(id=comment_id)
    article1 = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect(f'/feed/{article1.pk}')

        else:
            return redirect('/fail/')

    return render(request, 'remove_comment.html', {'feed': article})