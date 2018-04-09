from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import *
from django.db.models import Q
import datetime

# Create your views here.
def index(request, pindex):
    if pindex == '':
        pindex = '1'
    blogs = Article.objects.all()
    paginator = Paginator(blogs, 5)
    page = paginator.page(int(pindex))

    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))

    tags = Tag.objects.values('name')

    context = {'page': page, 'tags': tags, 'list2': list2}
    return render(request, 'article/index.html', context)

def showDetails(request, index, pindex):
    if pindex == '':
        pindex = '1'
    blog = Article.objects.get(id=index)
    blog.views = blog.views + 1
    blog.save()
    tags = Tag.objects.values('name').distinct()
    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))
    indexList = int(index)
    if request.method == 'POST':
        comment_content = request.POST['comment_content']
        if comment_content != '':
            newcomment = Comment()
            newcomment.content = comment_content
            newcomment.article = blog
            newcomment.created_time = datetime.datetime.now()
            newcomment.save()
            print(comment_content)
        else:
            pass
    else:
        pass
    comments = blog.comment_set.all()  # 选出当前页面显示的博客所对应的评论
    paginator = Paginator(comments, 10)
    page = paginator.page(int(pindex))
    context = {'blog': blog, 'tags': tags, 'list2': list2, 'index': index, 'indexList': indexList, 'page': page, 'comments': comments}
    return render(request, 'article/showDetails.html', context)

def categories(request, index, pindex):
    if index == '':
        index = '1'
    if pindex == '':
        pindex = '1'
    activeIndex = int(index)
    categories = Category.objects.all()
    blogs = Article.objects.filter(category_id=index)
    paginator = Paginator(blogs, 3)
    page = paginator.page(int(pindex))
    tags = Tag.objects.values('name')
    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))
    context = {'categories': categories, 'page': page, 'index': index, 'tags': tags, 'activeIndex': activeIndex, 'list2': list2}
    return render(request, 'article/categories.html', context)

def archives(request, pindex):
    if pindex == '':
        pindex = '1'
    blogs = Article.objects.all()
    paginator = Paginator(blogs, 30)
    page = paginator.page(int(pindex))
    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))
    tags = Tag.objects.values('name')
    context = {'page': page, 'tags': tags, 'list2': list2}
    return render(request, 'article/archives.html', context)

def tags(request):
    tags = Tag.objects.values('name')
    count_list = []
    for key in tags:
        for value in key.values():
            tag = Tag.objects.get(name=value)
            tag_articles = tag.article_set.all()
            count_list.append(len(tag_articles))

    date_list = Article.objects.values('created_time')
    listMonth = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            listMonth.append(strdate)
            listMonth2 = list(set(listMonth))

    context = {'tags': tags, 'tag_articles': tag_articles, 'count_list': count_list, 'listMonth': listMonth2}
    return render(request, 'article/tags.html', context)

def tag_articles(request, TagName):
    tags = Tag.objects.values('name')
    tag = Tag.objects.get(name=TagName)
    tag_articles = tag.article_set.all()
    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))
    context = {'tag_articles': tag_articles, 'tags': tags, 'list2': list2}
    return render(request, 'article/tag_articles.html', context)


def search(request):
    search_keywords = request.POST['keywords']
    if search_keywords == '':
        redirect('/')
    starttime = datetime.datetime.now()
    search_results = Article.objects.filter(Q(title__icontains=search_keywords)|Q(content__icontains=search_keywords))
    endtime = datetime.datetime.now()
    timedelta = (endtime - starttime).total_seconds()
    date_list = Article.objects.values('created_time')
    list1 = []
    for key in date_list:
        for value in key.values():
            strdate = value.strftime("%Y年%m月%d %H:%M:%S")[0:8]
            list1.append(strdate)
            list2 = list(set(list1))
    tags = Tag.objects.values('name')
    context = {'search_results': search_results, 'timedelta': timedelta, 'tags': tags, 'list2': list2}
    return render(request, 'article/search.html', context)

def addLikes(request, index):
    blog = Article.objects.get(id=index)
    blog.likes += 1
    blog.save()
    return redirect('/')
