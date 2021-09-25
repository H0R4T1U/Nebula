from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView



urlpatterns = [
    path('',include('Nebula.urls')),
    path('admin/', admin.site.urls),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")))
    
]

handler400 = "website.views.error_400"
handler403 = "website.views.error_403"
handler404 = "website.views.error_404"
handler500 = "website.views.error_500"
