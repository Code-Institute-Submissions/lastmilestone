from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('about_us/', include('about_us.urls')),
    path('contact/', include('contact.urls')),
    path('schedule/', include('schedule.urls')),
    path('profiles/', include('profiles.urls')),
    path('plan/', include('plan.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
