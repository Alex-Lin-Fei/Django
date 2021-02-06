from django.conf.urls import url
from . import views
from .views import IndexView

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
]