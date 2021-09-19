from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('',include('Nebula.urls')),
    path('admin/', admin.site.urls),
    
]

handler400 = "website.views.error_400"
handler403 = "website.views.error_403"
handler404 = "website.views.error_404"
handler500 = "website.views.error_500"
