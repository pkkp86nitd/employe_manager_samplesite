from . import views
from django.conf.urls import include,url
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
                url(r'^$',views.login,name = 'login'),
                url(r'home/$',views.home,name = 'home'),
                url(r'register/$',views.register,name = 'register'),
                url(r'eperformance/$',views.performance,name='performance'),
                url(r'logout/$', views.logout, name='logout'),
                url(r'viewtask/',views.view_task_detail, name = 'taskdetails'),
              ]