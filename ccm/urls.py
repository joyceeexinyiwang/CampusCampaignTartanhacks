from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$',  views.Menu),
    url(r'^mlk/$', views.MLK),
    url(r'^sa/$', views.SA)
]

#if ever need more pages, admin need to add them.