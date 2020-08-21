from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from .models import Post, Comment, CV
# Create your views here.

#Home Page
def index(request):

    #Blog Recommended
    recommend_blog_list = Post.objects.filter(recommend=True)

    #The Newest Articles
    newest_blog_articles= Post.objects.order_by('-pub_date').all()[:3]

    #Newest Comment Blogs
    newest_comment_blogs = Comment.objects.order_by('-pub_date').all()[:8]
    # Delete the same blogs
    unique_newest_comment_blogs = []
    i = []
    for blog in newest_comment_blogs:
        if blog.post.id not in i:
            unique_newest_comment_blogs.append(blog)
            i.append(blog.post.id)

    context = {
        'recommend_blog_list': recommend_blog_list,
        'newest_blog_articles': newest_blog_articles,
        'unique_newest_comment_blogs': unique_newest_comment_blogs,
    }
    return render(request, 'index.html', context)

class Search(View):
    def get(self,request):
        pass
    def post(self,request):
        keyw=request.POST.get('keywords')
        blog_list = Post.objects.filter(Q(title__contains=keyw) | Q(content__contains=keyw))
        context={
            'blog_list': blog_list,
        }
        return render(request, 'list.html', context)

#Comment

class CommentBlog(View):
    def get(self, request):
        pass
    def post(self, request, blog_id):
        if request.user.is_authenticated:
            comment = Comment()
            pub_time = datetime.now()
            content = request.POST.get('content')
            comment.post = Post.objects.get(pk=blog_id)
            comment.pub_date = pub_time
            comment.user = request.user
            comment.content = content
            comment.save()
            return HttpResponseRedirect(reverse("show_blog", kwargs={"blog_id": blog_id}))
        else:
            pass




def blog_list(request):

    blog_list=Post.objects.all()

    newest_comment_blogs = Comment.objects.order_by('-pub_date').all()[:8]
    # Delete the same blogs
    unique_newest_comment_blogs = []
    i = []
    for b in newest_comment_blogs:
        if b.post.id not in i:
            unique_newest_comment_blogs.append(b)
            i.append(b.post.id)

    context={
        'blog_list': blog_list,
        'unique_newest_comment_blogs': unique_newest_comment_blogs,

    }
    return render(request, 'list.html', context)


def show_blog(request, blog_id):
    blog= Post.objects.get(pk=blog_id)

    #renew the view number
    view_number= blog.views
    blog.views=view_number+1
    blog.save()

    #comment number

    newest_comment_blogs = Comment.objects.order_by('-pub_date').all()[:8]
    # Delete the same blogs
    unique_newest_comment_blogs = []
    i = []
    for b in newest_comment_blogs:
        if b.post.id not in i:
            unique_newest_comment_blogs.append(b)
            i.append(b.post.id)

    comment_list = Post.objects.get(pk=blog_id).comment_set.all()

    context={
        'blog':blog,
        #'new_comment_list':new_comment_list,
         'unique_newest_comment_blogs'  :unique_newest_comment_blogs,
        'comment_list':comment_list,
    }

    return render(request, 'show.html', context)



def show_cv(request, cv_id):
    cv = CV.objects.get(pk=cv_id)

    #renew the view number
    view_number= cv.views
    cv.views=view_number+1
    cv.save()

    newest_comment_blogs = Comment.objects.order_by('-pub_date').all()[:8]
    # Delete the same blogs
    unique_newest_comment_blogs = []
    i = []
    for b in newest_comment_blogs:
        if b.post.id not in i:
            unique_newest_comment_blogs.append(b)
            i.append(b.post.id)

    context={
        'cv': cv,
        'unique_newest_comment_blogs': unique_newest_comment_blogs,

    }

    return render(request, 'cv.html', context)


