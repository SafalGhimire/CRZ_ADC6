from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
   

]

urlpatterns += [
    path('app/',include('app.urls'))

]

