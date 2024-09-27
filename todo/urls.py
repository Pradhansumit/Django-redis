from django.urls import path
from todo import views

urlpatterns = [
        path("create/",views.CreateView().as_view()),
        path("list/",views.ListView().as_view()),
        path("list/<int:pk>/",views.ListDetailView().as_view()),
        path("delete/<int:pk>/",views.DeleteView().as_view()),
        ]

