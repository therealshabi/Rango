from django.conf import settings
from django.conf.urls.static import static

from rango import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
]
