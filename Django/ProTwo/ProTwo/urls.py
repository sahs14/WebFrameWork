
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from appTwo import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^users/',include('appTwo.urls')),
    url(r'^admin/', admin.site.urls),
]
