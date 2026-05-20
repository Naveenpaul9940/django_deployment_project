
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',register, name="register"),
    path("login/", login, name = "login"),
    path('products/', product, name = "products"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
