"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facebook.views import play, play2, my_profile, my_event, newsfeed, detail_feed, pages, new_feed, remove_feed, remove_comment, edit_feed, fail, page_new, edit_page, remove_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path('choidogeun/profile/', my_profile),
    path('event/', my_event),
    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('pages/', pages),
    path('new/', new_feed),
    path('feed/<pk>/remove', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('fail/', fail),
    path('pages/new/', page_new),
    path('pages/<pk>/edit', edit_page),
    path('pages/<pk>/remove/', remove_page),
    path('comment/<int:pk>/<int:comment_id>/', remove_comment)
]
