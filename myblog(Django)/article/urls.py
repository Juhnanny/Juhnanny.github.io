from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(\d*)$', views.index),
    url(r'^categories/(\d*)/(\d*)$', views.categories),
    url(r'^tags/$', views.tags),
    url(r'^tags/(?P<TagName>.+)/', views.tag_articles),
    url(r'^archives/(\d*)$', views.archives),
    url(r'^showDetails/(\d*)/(\d*)$', views.showDetails),
    url(r'^search/$', views.search),
    url(r'^add-likes/(\d*)', views.addLikes),
]