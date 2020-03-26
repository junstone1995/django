from django.conf.urls import include,url
from django.contrib import admin

from bookmark.views import BookmarkLV,BookmarkDV

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),

    url(r'^bookmark/$',BookmarkLV.as_view(),name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$',BookmarkDV.as_view(),name='detail'),
]
