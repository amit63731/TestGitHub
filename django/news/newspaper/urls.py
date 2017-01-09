from django.conf.urls import url

from newspaper import views
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from newspaper import views
from .views import SignUpViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'SignUps', views.SignUpViewSet)


urlpatterns = [
    url(r'^$',views.index ,name="index"),
    url(r'^result/$',views.result ,name="result"),
    url(r'^(?P<signup_id>\d+)/$',views.detail ,name="detail"),
    url(r'^update/(?P<signup_id>\d+)/$', views.update, name="update"), 
    url(r'^search/$', views.search, name="search"),   
    url(r'^dgraph/$', 'newspaper.views.graphultimate'),
    url(r'^csv/$', views.export_csv ,name="export_csv"),
    url(r'^angular/$', views.angular, name="angular"),
    url(r'^api/', include(router.urls)),
    #url(r'^/$'),
    #url(r'^(?P<>[0-9]+)/$'),
    
]
