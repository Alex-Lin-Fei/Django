from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'register/$', views.register, name='register'),
    # url(r'login/$', views.user_login, name='login'),
    url(r'^register_info/$', views.register_info, name='register_info'),
    url(r'^info/(?P<username>[\w\-]+)/$', views.edit_info, name='info'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^record/$', views.show_record, name='record'),
    url(r'^get_record/$', views.get_record, name='get_record'),
    url(r'order_detail/(?P<order_id>[\d]+)/$', views.order_detail, name='order_detail'),
    url(r'^release_commodity/$', views.release_commodity, name='release_commodity'),
    url(r'com_detail/(?P<com_id>[\d]+)/$', views.detail, name='com_detail'),
    path('add_commodity/<int:com_id>/', views.add_commodity, name='add_commodity'),
    url(r'fill_order/(?P<com_id>[\d]+)/$', views.fill_order, name='fill_order'),
    url(r'get_order/$', views.get_order, name='get_order'),
    url(r'^show_order/$', views.show_order, name='order'),
    url(r'^cagetory/$', views.show_category, name='category'),
    url(r'^get_category/$', views.get_category, name='get_category'),
    url(r'^suggest/$', views.get_suggest, name='suggest'),
    url(r'like/$', views.like_commodity, name='like'),
    url(r'message/$', views.show_message, name='message'),
]