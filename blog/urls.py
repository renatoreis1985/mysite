from django.urls import path # type: ignore

from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
]