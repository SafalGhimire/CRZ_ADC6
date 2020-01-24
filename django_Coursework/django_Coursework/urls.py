from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from app.views import view_authenticate_user
from app.views import view_logout

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),


]

urlpatterns += [
    path('app/',include('app.urls'))

]
urlpatterns += [
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/',view_authenticate_user)
    # path('accounts/',include('django.contrib.auth.urls')),

]
urlpatterns += [
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/logout/',view_logout)
    # path('accounts/',include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)