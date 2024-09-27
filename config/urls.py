from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("todo.urls")),
] + debug_toolbar_urls()
